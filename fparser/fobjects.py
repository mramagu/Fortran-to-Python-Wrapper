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
        dependencies = module.uses
        for use in module.uses:
            counter = 0
            while counter + 1 <= len(self.modules):
                if self.modules[counter].name.lower() == use.lower():
                    if bool(self.modules[counter].uses):
                        temp_dependencies = self.find_dependencies(self.modules[counter])
                        for temp in temp_dependencies:
                            if not temp in dependencies:
                                dependencies += temp
                    break
                counter += 1
            else:
                raise Exception('Could not find module {} within library'.format(use))
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

    def write_interface(self):
        """
            Generates the code for the library interface 

            Returns:
                A list of strings with to print on a file.
        """
        interface = list()
        for m in self.modules:
            interface += m.write_interface()
        return interface

class Ffile:
    """
        Fortran File Class
    """
    def __init__(self, filename, file_code):
        """
            Fortran File Class initiator

            Args:
                filename (string): Name of the file 
                file_code (list): List of string of the fortran code
        """
        self.filename = filename
        self.file_code = file_code
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
            modules.append(Module(m))
        return modules

class Module:
    """
        Fortran Module Class
    """
    def __init__(self, code):
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
        self.find_and_set_descriptions(code, 'before')

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

    def write_interface(self):
        """
            Generates the code for the module interface 

            Returns:
                A list of strings with to print on a file.
        """
        interface = list()
        interface.append('module {}'.format(self.fake_name))
        interface.append('use {}'.format(self.name))
        for c in self.contents:
            interface += c.write_interface()
        interface.append('end module')
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
        #self.solve_assume_shape(code)
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
        self.additional_variables.append(Variable(var_name, '{}, optional:: {}'.format(var_type, var_name)))

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
        var_def_end = code[0][pos_function + len(self.name):].lower().find(')')
        entries = code[0][pos_function + len(self.name) + var_def_start + 1: pos_function + len(self.name) + var_def_end]
        for entry in entries.split(','):
            for i, line in enumerate(code[1:]):
                if bool(fparsertools.find_command(line, entry.strip())):
                    variables.append(Variable(entry.strip(), line))
                    break
                if i == len(code[1:]):
                    raise Exception('Could not find variable definition {} in Ffunctional {}: \n{}'.format(entry, self.name, code))
        return variables

    def solve_assume_shape(self):
        """
            Method to identify variables that have a assume shape definition and altering them to fit f2py.
        """
        for v in self.variables: # Iterates thorugh all explicit function variables
            if v.dimensions != None: # If variable has dimension definition
                dimensions = (v.dimensions).split(',') # Dimensions are split into sub-sections
                for d in dimensions:
                    if ':' in d: # If a sub-section has an interval in it proceeds to analyze it
                        a = (d.strip()).split(':') # Subsection is split at interval and spaces are eliminated
                        if len(a) != 2: # All subsections should contain just 1 :, if more then raises error
                            raise Exception('Error solving assume shape of variable {} in {}:\n {}'.format(self.name, v.name, v.dimensions))
                        elif not bool(a[0]) or not bool(a[1]): # If either side of the interval is empty then the shape will be assumed
                            d = fparsertools.name_generator('N_' + v.name, # Generates a new optional integer to define its size.
                                [self.name] + [w.name for w in self.variables + self.additional_variables]) 
                            self.add_additional_variables(d, 'integer')

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
            Generates the code for the interface of the subroutine.

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        interface = list()
        interface.append('subroutine {}({})'.format(self.fake_name, ','.join([v.name for v in self.variables])))
        for v in self.variables:
            interface += v.write_interface()
        interface.append('call {}({})'.format(self.name, ','.join([v.name for v in self.variables])))
        interface.append('end subroutine')
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

    def read_name(self, first_line):
        """
            Determines the name of the fortran function

            Args:
                first_line (list): Code of the function

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
                first_line (list): Code of the function

            Returns:
                string with type of the function or none
        """
        func_position = fparsertools.find_command(first_line, 'function') # First instance of function in line
        if bool(first_line[0:func_position].strip()):
            return first_line[0:func_position]
        else: 
            return None

    def write_interface(self):
        """
            Generates the code for the interface of the function.

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        interface = list()
        interface.append('{} function {}({})'.format(self.func_type, self.fake_name, ','.join([v.name for v in self.variables])))
        for v in self.variables:
            interface += v.write_interface()
        interface.append('{} = {}({})'.format(self.fake_name, self.name, ','.join([v.name for v in self.variables])))
        interface.append('end function')
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

    def identify_vtype(self, code_line):
        """
            Identifies the type of fortran variable.
            Options(integer, real, complex, logical, character) 

            Args:
                code_line (string): Line in which the variable is defined

            Returns:
                string that contains either integer, real, complex, logical or character and their variations.
        """
        variable_definition = code_line.split("::")[0] # Extracts the definition of the variable before ::
        variable_definition = variable_definition.split(',') # Divides definition into elemental blocks
        options = ['integer', 'real', 'complex', 'logical', 'character']
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
        dimension = ''
        variable_definition = code_line.split("::")[0] # Extracts the definition of the variable before ::
        if 'dimension' in variable_definition.lower(): # If dimension in definition, adds dim_def
            dim_position = variable_definition.lower().find('dimension')
            dim_def_start = variable_definition[dim_position + len('dimension'):].lower().find('(')
            dim_def_end = variable_definition[dim_position + len('dimension'):].lower().find(')')
            dimension += variable_definition[dim_position + len('dimension') + dim_def_start + 1:\
                dim_position + len('dimension') + dim_def_end]

        written_variable = code_line.split("::")[1] # Extracts the definition of the variable after ::
        vposition = fparsertools.find_command(written_variable, self.name)  # Finds variable name in line
        if vposition == None:
            raise Exception('Variable {} not found in expected line: \n{}'.format(self.name, code_line))
        elif vposition + len(self.name) != len(written_variable): # Checks if additional dimensions are declared
            if bool(written_variable[vposition + len(self.name):].strip()):
                if written_variable[vposition + len(self.name):].strip()[0] == '(': 
                    dim_def_start = written_variable[vposition + len(self.name):].lower().find('(')
                    dim_def_end = written_variable[vposition + len(self.name):].lower().find(')')
                    add_d = written_variable[vposition + len(self.name) + dim_def_start + 1:\
                            vposition + len(self.name) + dim_def_end]
                    if bool(dimension):
                        dimension += ',' + add_d
                    else:
                        dimension += add_d

        if dimension == '': # If no dimensions have been declared returns None
            return None
        else: # If not it returns the string of dimensions
            return dimension.strip()

    def identify_other_def(self, code_line):
        """
            Identifies other details in variable definition not explicitely defined.

            Args:
                code_line (string): Line in which the variable is defined

            Returns:
                list of strings with additional code definitions.
        """
        variable_definition = code_line.split("::")[0] # Extracts the definition of the variable before ::
        definitions = variable_definition.split(",") # Divides it into smaller sections
        other_def = list()
        for d in definitions:
            if not self.type.lower() in d.lower() and 'dimension' not in d.lower():
                other_def.append(d)
        return other_def

    def write_interface(self):
        """
            Generates the code for the interface of the variable definition

            Returns:
                A list of strings to be added to the rest of the module interface.
        """
        definition = list()
        definition += [self.type]
        if self.dimensions != None:
            definition += ['dimension({})'.format(self.dimensions)]
        if self.other_def != None:
            definition += self.other_def
        interface = ['{} :: {}'.format(','.join(definition), self.name)]
        return interface