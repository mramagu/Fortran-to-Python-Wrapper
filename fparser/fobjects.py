import fparsertools

class Flibrary:
    """
        Fortran Library Class
    """
    def __init__(self, files):
        """
            Fortran Library Class initiator. 
            Builds Library from Fortran files

            Args:
                filename (files): Fortran Library files 
        """
        self.modules = list()
        for f in files:
            self.modules += f.modules
        self.solve_fake_names()
        self.module_reordering()

    def module_reordering(self):
        """
            Reorders all modules in the Library to match dependencies.
        """
        self.modules = [x for x in sorted(self.modules, key=lambda m: len(self.find_dependencies(m)))]

    def find_dependencies(self, module):
        """
            Finds all uses of a certain module.

            Args:
                module (Module): Module in which to search for dependencies.

            Returns:
                Returns a list of dependencies for the module.
        """
        dependencies = list(module.uses)
        for use in module.uses:
            counter = 0
            while counter + 1 <= len(self.modules):
                if self.modules[counter].name.lower() == use.lower():
                    if bool(self.modules[counter].uses):
                        temp_dependencies = self.find_dependencies(self.modules[counter])
                        for temp in temp_dependencies:
                            if not temp in dependencies:
                                dependencies.append(temp)
                    break
                counter += 1
            else:
                raise Exception('Could not find module {} declared in module {} within library'.format(use, module.name))
        return dependencies

    def solve_fake_names(self):
        """
            Solves fake names contradictions for the library.
        """
        for m in self.modules:
            og_module_names = [i.name for i in self.modules]
            og_func_names = [j.name for i in self.modules for j in i.contents]
            other_fake_modules = [i.fake_name for i in self.modules if i != m]
            other_fake_func = [j.fake_name for i in self.modules if i != m for j in i.contents]
            forbidden_names = og_module_names + other_fake_modules + og_func_names
            m.change_fake_name(fparsertools.name_generator(m.fake_name, forbidden_names))
            for f in m.contents:
                other_fake_func_names = [i.name for i in m.contents if i != f]
                f_variables = [i.name for i in f.variables]
                forbidden_names2 = forbidden_names + other_fake_func_names + f_variables + [m.fake_name]
                f.change_fake_name(fparsertools.name_generator(f.fake_name, forbidden_names2))

    def write_f2py_interface(self):
        """
            Generates the code for the library interface 

            Returns:
                A list of strings with to print on a file.
        """
        interface = list()
        for m in self.modules:
            interface += m.write_f2py_interface()
        return interface

class Ffile:
    """
        Fortran File Class
    """
    def __init__(self, filename, file_code, comment_style='before'):
        """
            Fortran File Class initiator

            Args:
                filename (string): Name of the file 
                file_code (list): List of string of the fortran code
        """
        self.filename = filename
        self.file_code = file_code
        self.comment_style = comment_style
        self.modules = self.module_finder(file_code)

    def module_finder(self, code):
        """
        Function that finds all modules within a fortran file

        Returns:
            list: A list with all module objects
        """
        modules_str = fparsertools.section(code, 'module')
        modules = list()
        for m in modules_str:
            modules.append(Module(m, self.comment_style))
        return modules

class Module:
    """
        Fortran Module Class
    """
    def __init__(self, code, comment_style='before'):
        """
            Fortran Module Class initiator

            Args:
                filename (str): Name of the file 
                module_code (list): List of str of the fortran code
        """
        self.name = self.module_name(code)
        self.fake_name = self.name + '_py'
        self.uses = self.find_uses(code)
        self.contents = self.find_functionals(code)
        self.find_and_set_descriptions(code, comment_style)
        self.private_public_solver(code)

    def change_fake_name(self, new_fake_name):
        """
            Method to change the method's fake name
            
            Args:
                new_fake_name (str): New fake name
        """
        self.fake_name = new_fake_name

    def module_name(self, code):
        """
            Finds out the name of the fortran module

            Returns:
                string: name of the module
        """
        name = code[0] # First line of the module code where the name is defined
        module_position = name.lower().find('module') # First instance of module in line
        return name[module_position + len('module'):].strip() # Line from first instance onwards and space deletion

    def find_uses(self, code):
        """
            Finds all the module uses within this module

            Returns:
                list of strings with the name of said modules or None
        """
        uses = list()
        counter = 1 # Starts search at the second line of the code
        while counter <= len(code): # Studies line of the code
            use = fparsertools.find_command(code[counter], 'use')
            if use != None:
                line_no_comment = code[counter].split('!')[0] # Separates code in two fragments where a comment migh be declared and stores the first one
                pure_use = line_no_comment.split(',')[0] # Separates code into two fragments in case a use only is being declared and stores the first one
                uses.append(pure_use[use + len('use'):].strip()) # Line from first instance onwards and space deletion
            elif fparsertools.find_command(code[counter], 'contains') != None or \
                fparsertools.find_command(code[counter], 'implicit') != None: # Once one of these commands has been declared no more uses will appear
                break 
            counter += 1
        return uses

    def find_functionals(self, code):
        """
            Finds all the module functionals (subroutines or functions) within this module

            Returns:
                list of functionals of the module
        """
        functions_str = fparsertools.section(code, 'function') # Sections all functions in the code
        functions = [Function(f) for f in functions_str] # Processes all functions in the module
        del functions_str

        subroutines_str = fparsertools.section(code, 'subroutine') # Sections all subroutines in the code
        subroutines = [Subroutine(s) for s in subroutines_str] # Processes all subroutines in the module
        del subroutines_str

        contents = functions + subroutines
        return contents

    def find_and_set_descriptions(self, code, description_format):
        """
            Sets descriptions for all the elements of a module.

            Args:
                code (list): Code of the module.
                description_format (string): Type of description format (before, after).
        """
        functionals = list(self.contents)
        for i, line in enumerate(code): # Iterates over every line in the code
            for j, f in enumerate(functionals): # Iterates over every functional not yet described
                # command for each type of functional
                if type(f) == Function:
                    search = 'function'
                elif type(f) == Subroutine:
                    search = 'subroutine'
                else:
                    raise Exception('Type {} functional not supported in set descriptions'.format(f))

                # Finds definition of functional
                if fparsertools.find_command(line, search) != None and  fparsertools.find_command(line, f.name) != None:
                    # Adds description according to format
                    if description_format == 'before': # Looks for description before function definition
                        temp_code = list(code[0:i])
                        temp_code.reverse()
                        comments = fparsertools.block_comments(temp_code)
                        del temp_code
                        comments.reverse()
                    elif description_format == 'after': # Looks for description before function definition
                        comments = fparsertools.block_comments(code[i+1:])
                    else:
                        raise Exception('Description format {} not supported in set descriptions'.format(description_format))

                    f.set_comments(comments) # Adds description
                    functionals.pop(j) # Once described it no longer needs to be found so it removes it from the search list
                    break # Exits loop to search for next definition
            # If all functionals have been described it exits the loop
            if not bool(functionals):
                break

    def private_public_solver(self, code):
        """
            Solves problems with private/public definitions. Deletes all private functions from the module

            Args:
                code (list): Code of the module.
        """
        private_module = False
        for line in code:
            if fparsertools.find_command(line, 'private') !=None:
                private_module = True
                break

        if private_module:
            public_functions = list()
            for line in code:
                if fparsertools.find_command(line, 'public') !=None:
                    if fparsertools.identify_comment(line) != None:
                        line = line.replace(fparsertools.identify_comment(line), '')
                    line = line[len('public'):].split(',')
                    public_functions += [i.strip() for i in line]
        else:
            public_functions = [c.name for c in self.contents]
        
        functions = self.contents
        self.contents = list()
        for func in functions:
            if func.name in public_functions:
                self.contents.append(func)



    def write_f2py_interface(self):
        """
            Generates the code for the module interface 

            Returns:
                A list of strings with to print on a file.
        """
        interface = list()
        interface.append('module {}'.format(self.fake_name))
        interface.append('use {}'.format(self.name))
        interface.append('implicit none')
        interface.append('contains')
        for c in self.contents:
            interface += c.write_f2py_interface()
        interface.append('end module')
        return interface

    def write_py_interface(self, lib_name):
        """
            Generates the code for the module python interface 

            Args:
                lib_name (string): Name of the f2py generated library

            Returns:
                A list of strings with to print on a file.
        """
        interface = list()
        interface.append('class {}:'.format(self.name))
        for c in self.contents:
            interface += fparsertools.tabing_tool(c.write_py_interface(lib_name, self.fake_name))
        return interface


class Ffunctional:
    """
        Fortran Functional Class
    """
    def __init__(self, code, name):
        """
            Fortran Functional class initiator

            Args:
                code (str): Functional element code
        """
        self.name = name
        self.fake_name = name + '_py'
        self.variables = self.read_variables(code)
        self.additional_variables = list()
        self.solve_assume_shape()
        self.procedures = list()
        self.commentary = list()

    def change_fake_name(self, new_fake_name):
        """
            Method to change the function's fake name
            
            Args:
                new_fake_name (str): New fake name
        """
        self.fake_name = new_fake_name

    def set_comments(self, comment):
        """
            Method to add a block comment to a Ffunctional.

            Args:
                comment (list): Comment of functional element
        """
        self.commentary = comment

    def add_additional_variables(self, var_name, var_type):
        """
            Method to add an additional optional variable.

            Args:
                var_name (string): Name of the variable.
                var_type (string): Type of new variable
        """
        self.additional_variables.append(Variable(var_name, '{}, intent(in), optional :: {}'.format(var_type, var_name)))

    def read_variables(self, code):
        """
            Method to identify and classify API variables of a functional

            Args:
                code (str): Functional element code

            Returns:
                list of variables
        """
        variables = list()
        pos_function = fparsertools.find_command(code[0], self.name) # Position of function name in code
        var_def_start = code[0][pos_function + len(self.name):].lower().find('(')
        var_def_end = fparsertools.find_closing_parenthesis(code[0],pos_function + len(self.name)+var_def_start)
        entries = code[0][pos_function + len(self.name) + var_def_start + 1: var_def_end]
        for entry in entries.split(','):
            for i, line in enumerate(code[1:]):
                if fparsertools.find_command(line, entry.strip()) != None:
                    if fparsertools.find_command(line, 'function') != None:
                        variables.append(Function(code[i+1:]))
                    elif fparsertools.find_command(line, 'subroutine') != None:
                        variables.append(Subroutine(code[i+1:]))
                    elif any(fparsertools.find_command(line, possible_type) != None for possible_type in Variable.types()):
                        variables.append(Variable(entry.strip(), line))
                    else:
                        raise Exception('Could not find defnition for variable {} in {}. First instance: \n {}'.format(entry, self.name, line))
                    break
                if i == len(code[1:]):
                    raise Exception('Could not find variable definition {} in Ffunctional {}: \n{}'.format(entry, self.name, '\n'.join(code)))
        return variables

    def solve_assume_shape(self):
        """
            Method to identify variables that have a assume shape definition and altering them to fit f2py.
        """
        for v in self.variables: # Iterates thorugh all explicit function variables
            if isinstance(v, Variable): # If instance is a variable it solves its shape
                if v.dimensions != None: # If variable has dimension definition
                    for index, d in enumerate(v.dimensions):
                        if ':' in d: # If a sub-section has an interval in it proceeds to analyze it
                            a = (d.strip()).split(':') # Subsection is split at interval and spaces are eliminated
                            if len(a) != 2: # All subsections should contain just 1 :, if more then raises error
                                raise Exception('Error solving assume shape of variable {} in {}:\n {}'.format(self.name, v.name, v.dimensions))
                            elif not bool(a[0]) or not bool(a[1]): # If either side of the interval is empty then the shape will be assumed
                                d = fparsertools.name_generator('N_' + v.name, # Generates a new optional integer to define its size.
                                    [self.name] + [w.name for w in self.variables + self.additional_variables]) 
                                v.change_dimension(d, index)
                                self.add_additional_variables(d, 'integer')
            elif isinstance(v,Function) or isinstance(v, Subroutine): # If instance is another functional it solves the shape of the function too
                v.solve_assume_shape()
            else:
                raise Exception('Cannot solve the shape of {} in function {}'.format(v.name, self.name))

class Subroutine(Ffunctional):
    """
        Fortran Subrutine Class
    """
    def __init__(self, code):
        """
            Fortran Functional class initiator

            Args:
                code (str): Functional element code
        """
        super().__init__(code, self.read_name(code[0]))

    def read_name(self, first_line):
        """
            Determines the name of the fortran subroutine

            Args:
                code (first_line): Definition of the subroutine

            Returns:
                string: name of the subroutine
        """
        subr_position = fparsertools.find_command(first_line.lower(), 'subroutine') # First instance of Subroutine in line
        if subr_position == None:
            raise Exception('Subroutine name cannot be read from: \n {}'.format(first_line))
        variable_def_position = first_line[subr_position + len('subroutine'):].lower().find('(') # Subroutine name stops when variables are defined
        return first_line[subr_position + len('subroutine'): subr_position + len('subroutine') + variable_def_position].strip() # Subroutine name and space deletion

    def write_interface(self):
        """
            Method to write the subroutine as part of a fortran interface.
        """
        interface = self.write_f2py_interface()
        interface[0].replace(self.fake_name, self.name)
        interface.pop(-2)
        return interface
    
    def write_f2py_interface(self):
        """
            Generates the code for the interface of the subroutine.

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        interface = list()
        interface.append('subroutine {}({})'.format(self.fake_name, ','.join(
            [v.name for v in self.variables + self.additional_variables])))
        for v in self.variables + self.additional_variables:
            interface += v.write_f2py_interface()
        interface.append('call {}({})'.format(self.name, ','.join([v.name for v in self.variables])))
        interface.append('end subroutine')
        return interface

    def write_py_interface(self, lib_name, module_name):
        """
            Generates the code for the python interface of the subroutine.

            Args:
                lib_name (string): Name of the f2py generated library
                module_name (string): Name of the f2py generated module with the function

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        interface = list()
        interface.append('\"""')
        interface += fparsertools.tabing_tool(self.commentary)
        interface += fparsertools.tabing_tool(['{} ({}): {}'.format(v.name, v.type, v.comment) for v in self.variables])
        interface.append('\"""')
        interface.append('{}.{}.{}({})'.format(lib_name, module_name, self.fake_name, ','.join([v.name for v in self.variables])))
        interface = fparsertools.tabing_tool(interface)
        interface.insert(0, 'def {}({}):'.format(self.name, ','.join([v.name for v in self.variables])))
        return interface

class Function(Ffunctional):
    """
        Fortran Function Class
    """
    def __init__(self, code):
        """
            Fortran Functional class initiator

            Args:
                code (list): Functional element code
        """
        super().__init__(code, self.read_name(code[0]))
        self.func_type = self.find_function_type(code[0])
        self.result = self.find_result(code)

    def read_name(self, first_line):
        """
            Determines the name of the fortran function

            Args:
                first_line (string): Code of the function

            Returns:
                string: name of the function
        """
        func_position = fparsertools.find_command(first_line.lower(), 'function') # First instance of function in line
        if func_position == None:
            raise Exception('Function name cannot be read from: \n {}'.format(first_line))
        variable_def_position = first_line[func_position + len('function'):].lower().find('(') # Function name stops when variables are defined
        return first_line[func_position + len('function'): func_position + len('function') + variable_def_position].strip() # Function name and space deletion

    def find_function_type(self, first_line):
        """
            Finds additional information on the type of function

            Args:
                first_line (string): Code of the function

            Returns:
                string with type of the function or none
        """
        func_position = fparsertools.find_command(first_line, 'function') # First instance of function in line
        if bool(first_line[0:func_position].strip()):
            return first_line[0:func_position].strip()
        else:
            return None

    def find_result(self, code):
        """
            Finds the result of the function type and dimensions

            Args:
                code (list): Code of the function

            Returns:
                Variable for the result of the function
        """
        options = Variable.types() # Fortran variable types
        if self.func_type == None: # If no func type has been declared it skips the loop to determine if the output has been defined
            counter = len(options)
        else:
            counter = 0

        while counter +1 <= len(options): # Loop to determine if the output type has been defined.
            if options[counter] in self.func_type: 
                result = Variable(self.name, '{}::{}'.format(options[counter], self.name))
                break
            counter += 1
        else:
            pos_result = fparsertools.find_command(code[0], 'result') # Position of result in line
            if pos_result != None:
                res_def_start = code[0][pos_result + len('result'):].lower().find('(')
                res_def_end = fparsertools.find_closing_parenthesis(code[0],pos_result + len('result')+res_def_start)
                result_name = code[0][pos_result + len('result') + res_def_start + 1:res_def_end].strip()
            else:
                result_name = self.name
            for i, line in enumerate(code[1:]):
                if fparsertools.find_command(line, result_name) != None:
                    result = Variable(result_name, line)
                    break
                if i == len(code[1:]):
                    raise Exception('Could not find function definition in Function {}: \n{}'.format(self.name, '\n'.join(code)))
        return result

    def write_interface(self):
        """
            Method to write the subroutine as part of a fortran interface.

            Returns:
                 A list of strings to be added to the rest of the function interface.
        """
        interface = self.write_f2py_interface()
        for i, line in enumerate(interface):
            if fparsertools.find_command(line, self.fake_name):
                interface[i] = interface[i].replace(self.fake_name, self.name)
        interface.pop(-2)
        return interface

    def write_f2py_interface(self):
        """
            Generates the code for the interface of the function.

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        interface = list()
        if self.func_type != None:
            interface.append('{} function {}({})'.format(self.func_type, self.fake_name, ','.join(
                [v.name for v in self.variables + self.additional_variables])))
        else:
            interface.append('function {}({})'.format(self.fake_name, ','.join(
                [v.name for v in self.variables + self.additional_variables])))

        procedures = list()
        for v in self.variables + self.additional_variables:
            if isinstance(v, Variable):
                interface += v.write_f2py_interface()
            else:
                procedures.append(v)
        
        if self.func_type != None:
            if not any(var_type in self.func_type for var_type in Variable.types()): # If definition of function is included in func_type it does not write it
                interface += [('\n'.join(self.result.write_f2py_interface())).replace(self.result.name, self.fake_name)] # If not defines the output of the function
        else:
            interface += [('\n'.join(self.result.write_f2py_interface())).replace(self.result.name, self.fake_name)]

        if bool(procedures):
            interface.append('interface')
            for v in procedures:
                interface += v.write_interface()
            interface.append('end interface')

        interface.append('{} = {}({})'.format(self.fake_name, self.name, ','.join([v.name for v in self.variables])))
        interface.append('end function')
        return interface

    def write_py_interface(self, lib_name, module_name):
        """
            Generates the code for the python interface of the subroutine.

            Args:
                lib_name (string): Name of the f2py generated library
                module_name (string): Name of the f2py generated module with the function

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        interface = list()
        interface.append('\"""')
        interface += fparsertools.tabing_tool(self.commentary)
        interface += fparsertools.tabing_tool(['{} ({}): {}'.format(v.name, v.type, v.comment) for v in self.variables])
        interface.append('\"""')
        interface.append('return {}.{}.{}({})'.format(lib_name, module_name, self.fake_name, ','.join([v.name for v in self.variables])))
        interface = fparsertools.tabing_tool(interface)
        interface.insert(0, 'def {}({}):'.format(self.name, ','.join([v.name for v in self.variables])))
        return interface

class Variable:
    """
        Fortran Variable Class
    """
    def __init__(self, name, code_line):
        """
            Fortran Variable class initiator

            Args:
                code (list): Functional element code
        """
        self.name = name
        self.type = self.identify_vtype(code_line)
        self.dimensions = self.identify_dimensions(code_line)
        self.other_def = self.identify_other_def(code_line)
        self.comment = fparsertools.identify_comment(code_line)

    def types():
        """
            Returns a list of accepted variable types
        """
        return ['integer', 'real', 'complex', 'logical', 'character', 'procedure']

    def var_splitter(self, code_line):
        """
            Function to split variable definitions appropriately

            Args:
                code_line (string): Variable definition code
        """
        if len(code_line.split("::")) == 2:
            variable_definition = code_line.split("::")[0] # Extracts the definition of the variable before ::
            written_variable = code_line.split("::")[1] # Extracts the definition of the variable after ::
        elif len(code_line.split("::")) == 1:
            var_pos = fparsertools.find_command(code_line, self.name)
            variable_definition = code_line[0:var_pos]
            written_variable = code_line[var_pos:]
        else:
            raise Exception('Error in variable {} definition in code: \n    {}'.format(self.name, code_line))
        return (variable_definition, written_variable)

    def change_dimension(self, new_dim, index):
        """
            Fortran Variable class initiator

            Args:
                new_dim (string): New value for the dimension
                index (integer): Dimension position index
        """
        self.dimensions[index] = new_dim

    def identify_vtype(self, code_line):
        """
            Identifies the type of fortran variable.
            Options(integer, real, complex, logical, character) 

            Args:
                code_line (string): Line in which the variable is defined

            Returns:
                string that contains either integer, real, complex, logical or character and their variations.
        """
        variable_definition = self.var_splitter(code_line)[0] # Extracts the definition of the variable before ::
        variable_definition = variable_definition.split(',') # Divides definition into elemental blocks
        options = Variable.types()
        breaker = False
        for type in options:
            for d in variable_definition: 
                if type in d: # Finds definition within elemental blocks
                    vtype = d
                    breaker = True
                    break
            if breaker: # If definition is found breaks cycle
                break 

        if 'vtype' not in vars():
            raise Exception('Fparser was not able to interpret variable \'{}\' type in line \n {}'.format(self.name, code_line))
        return vtype.strip()

    def identify_dimensions(self, code_line):
        """
            Identifies the dimension of a fortran variable

            Args:
                code_line (string): Line in which the variable is defined

            Returns:
                string that defines the dimension of the variable
        """
        dimension = []
        variable_definition = self.var_splitter(code_line)[0]
        written_variable = self.var_splitter(code_line)[1]
        
        if 'dimension' in variable_definition.lower(): # If dimension in definition, adds dim_def
            dim_position = variable_definition.lower().find('dimension')
            dim_def_start = variable_definition[dim_position + len('dimension'):].lower().find('(')
            dim_def_end = fparsertools.find_closing_parenthesis(variable_definition + written_variable, 
                            dim_position + len('dimension') + dim_def_start)
            dimension += variable_definition[dim_position + len('dimension') + dim_def_start + 1: dim_def_end].strip().split(',')

        vposition = fparsertools.find_command(written_variable, self.name)  # Finds variable name in line
        if vposition == None:
            raise Exception('Variable {} not found in expected line: \n{}'.format(self.name, code_line))
        elif vposition + len(self.name) != len(written_variable): # Checks if additional dimensions are declared
            if bool(written_variable[vposition + len(self.name):].strip()):
                if written_variable[vposition + len(self.name):].strip()[0] == '(': 
                    dim_def_start = written_variable[vposition + len(self.name):].lower().find('(')
                    dim_def_end = fparsertools.find_closing_parenthesis(variable_definition + written_variable, 
                                    len(variable_definition) + vposition + len(self.name) + dim_def_start + dim_def_start) \
                                       - len(variable_definition)
                    dimension += written_variable[vposition + len(self.name) + dim_def_start + 1:dim_def_end].strip().split(',')

        if not bool(dimension): # If no dimensions have been declared returns None
            return None
        else: # If not it returns the string of dimensions
            return dimension

    def identify_other_def(self, code_line):
        """
            Identifies other details in variable definition not explicitely defined.

            Args:
                code_line (string): Line in which the variable is defined

            Returns:
                list of strings with additional code definitions.
        """
        variable_definition = self.var_splitter(code_line)[0] # Extracts the definition of the variable before ::
        definitions = variable_definition.split(",") # Divides it into smaller sections
        other_def = list()
        for d in definitions:
            if not self.type.lower() in d.lower() and 'dimension' not in d.lower():
                other_def.append(d)
        return other_def

    def write_f2py_interface(self):
        """
            Generates the code for the interface of the variable definition

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        definition = list()
        definition += [self.type]
        if self.dimensions != None:
            definition += ['dimension({})'.format(','.join(self.dimensions))]
        if self.other_def != None:
            definition += self.other_def
        interface = ['{} :: {}'.format(','.join(definition), self.name)]
        return interface