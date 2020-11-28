import fparsertools

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
        self.uses = self.find_uses(code)
        self.functionals = self.find_functionals(code)

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
        print(code)
        for i, line in enumerate(code[1:]):
            if 'use' in line.lower():
                use_position = line.lower().find('use') # First instance of use in line
                uses.append(line[use_position + len('use'):].strip()) # Line from first instance onwards and space deletion
            else: # Once all uses have beew written in a Fortran module no more will appear
                break 
        return uses

    def find_contains(self):
        pass

    def find_functionals(self, code):
        """
            Finds all the module functionals (subroutines or functions) within this module

            Returns:
                list of functionals of the module
        """
        functions_str = fparsertools.section(code, 'function')
        functions = list()
        for f in functions_str:
            functions.append(Function(f))
        del functions_str, f

        subroutines_str = fparsertools.section(code, 'subroutine')
        subroutines = list()
        for s in subroutines_str:
            subroutines.append(Subroutine(s))
        del subroutines_str

        functionals = functions + subroutines
        return functionals

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
        self.variables = self.read_variables(code)
        self.procedures = list()
        self.commentary = list()

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
                    print(variables)
                    break
                if i == len(code[1:]):
                    raise Exception('Could not find variable definition {} in Ffunctional {}: \n{}'.format(entry, self.name, code))
        return variables


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
        super().__init__(code, self.read_name(code))

    def read_name(self, code):
        """
            Determines the name of the fortran function

            Args:
                code (list): Code of the function

            Returns:
                string: name of the function
        """
        name = code[0] # First line of the function where the name is defined
        func_position = name.lower().find('subroutine') # First instance of function in line
        variable_def_position = name.lower().find('(') # Function name stops when variables are defined
        return name[func_position + len('subroutine'):variable_def_position].strip() # Function name and space deletion

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
        super().__init__(code, self.read_name(code))

    def read_name(self, code):
        """
            Determines the name of the fortran function

            Args:
                code (list): Code of the function

            Returns:
                string: name of the function
        """
        name = code[0] # First line of the function where the name is defined
        func_position = name.lower().find('function') # First instance of function in line
        variable_def_position = name.lower().find('(') # Function name stops when variables are defined
        return name[func_position + len('function'):variable_def_position].strip() # Function name and space deletion

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
            dimension.join(variable_definition[dim_position + len('dimension') + dim_def_start + 1:\
                dim_position + len('dimension') + dim_def_end])

        written_variable = code_line.split("::")[1] # Extracts the definition of the variable after ::
        vposition = fparsertools.find_command(written_variable, self.name)  # Finds variable name in line
        if vposition == None:
            raise Exception('Variable {} not found in expected line: \n{}'.format(self.name, code_line))
        elif vposition + len(self.name) != len(written_variable): # Checks if additional dimensions are declared
            if written_variable[vposition + len(self.name):].strip()[0] == '(': 
                dim_def_start = written_variable[vposition + len(self.name):].lower().find('(')
                dim_def_end = written_variable[vposition + len(self.name):].lower().find(')')
                dimension.join(variable_definition[vposition + len(self.name) + dim_def_start + 1:\
                    vposition + len(self.name) + dim_def_end])

        if dimension == '': # If no dimensions have been declared returns None
            return None
        else: # If not it returns the string of dimensions
            return dimension.strip()