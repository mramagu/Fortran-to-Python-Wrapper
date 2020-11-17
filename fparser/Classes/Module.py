class Module:
    """
        Fortran Mdule Class
    """
    def __init__(self, filename, module_code):
        """
            Fortran Mdule Class

            Args:
                filename (str): Name of the file 
                module_code (list): List of str of the fortran code
        """
        self.filename = filename
        self.code = module_code