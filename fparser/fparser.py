import fobjects

import os

def library_maker(files, comment_style='before'):
    """
        Makes a library out fortran files.

        Args:
            files (list): List of strings with the files directories.
            comment_style (string): Style in which functions and subroutines are commented. 'after' or 'before'
                default =  'before'

        Returns:
            A Flibrary made up of all the fortran files. 
    """
    fortran_files = list()
    for file_dir in files:
        print('Reading file {}'.format(file_dir))
        file = open(file_dir, 'r') 
        file_code = file.readlines() 
        for i, line in enumerate(file_code):
            file_code[i] = line.replace('\n', '')
        file.close()
        fortran_files.append(fobjects.Ffile(file_dir, file_code, comment_style=comment_style))
    print('Generating Library')
    Lib=fobjects.Flibrary(fortran_files)
    print('Library Generated Correctly')
    return Lib

def interface_writer(lib, modules):
    """
        Generates an intermediate interface for f2py from certain modules.

        Args:
            lib (fparser.Flibrary): Library from which to make the interface.
            modules (list): List of strings  

        Returns:
            A string with the interface to print on a file.
    """
    interface = list()
    writing_modules = [m for m in lib.modules if m.name in modules]
    for m in writing_modules:
        interface += m.write_interface()
    return '\n'.join(interface)

if __name__ == '__main__':
    test_module1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule1.f90')
    test_module2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule2.f90')
    test_module3 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule3.f90')
    Lib = library_maker([test_module1, test_module2, test_module3])
    print(interface_writer(Lib, ['test_module_1', 'test_module_12', 'test_module_2', 'test_module_3']))