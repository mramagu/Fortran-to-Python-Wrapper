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
        self.modules = self.module_finder()

    def module_finder(self):
        """
        Function that finds all modules within a fortran file

        Returns:
            list: A list with all module objects
        """
        modules = list()
        module_str = list()
        module_line = False
        for i, line in enumerate(self.file_code):
            if module_line:
                module_str.append(line)

            if 'module' in line and 'end' not in line.lower():
                module_line = True
                module_str.append(line)
            elif 'module' in line and 'end' in line.lower():
                module_line = False
                modules.append(Module(module_str))
                module_str = list()
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

class Ffunctional:
    """
        Fortran Functional Class
    """
    def __init__(self, code):
        """
            Fortran Functional class initiator

            Args:
                code (str): Functional element code

            Returns:
                string: name of the module
        """
        self.code = code
        self.variables = list()

class Subrutine(Ffunctional):
    """
        Fortran Subrutine Class
    """
    def __init__(self, code):
        """
            Fortran Functional class initiator

            Args:
                code (str): Functional element code

            Returns:
                string: name of the module
        """
        super().__init__(code)