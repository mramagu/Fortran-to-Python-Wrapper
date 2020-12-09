import fobjects

import os

def library_maker(files, comment_style='before', **kwargs):
    """
        Makes a library out fortran files.

        Args:
            files (list): List of strings with the files directories.
            comment_style (string): Style in which functions and subroutines are commented. 'after' or 'before'
                default =  'before'

        Returns:
            A Flibrary made up of all the fortran files. 
    """
    terminal_present = False
    if 'terminal' in kwargs:
        terminal_present = True
        terminal = kwargs['terminal']
        terminal.add_line('')
    fortran_files = list()
    try:
        for file_dir in files:
            if terminal_present:
                terminal.add_line('Reading file {}'.format(file_dir))
            else:
                print('Reading file {}'.format(file_dir))
            file = open(file_dir, 'r') 
            file_code = file.readlines() 
            for i, line in enumerate(file_code):
                file_code[i] = line.replace('\n', '')
            file.close()
            fortran_files.append(fobjects.Ffile(file_dir, file_code, comment_style=comment_style))
        
        if terminal_present:
            terminal.add_line('Generating Library')
        else:
            print('Generating Library')
        Lib=fobjects.Flibrary(fortran_files)
        if terminal_present:
            terminal.add_line('Library Generated Correctly')
        else:
            print('Library Generated Correctly')
        return Lib
    except Exception as e:
        if terminal_present:
            terminal.add_line('Error: ' + str(e), number=2)
        else:
            print(e)
        return None

def interface_writer(lib, modules, **kwargs):
    """
        Generates an intermediate interface for f2py from certain modules.

        Args:
            lib (fparser.Flibrary): Library from which to make the interface.
            modules (list): List of strings  

        Returns:
            A string with the interface to print on a file.
    """
    terminal_present = False
    if 'terminal' in kwargs:
        terminal_present = True
        terminal = kwargs['terminal']
        terminal.add_line('')
    interface = list()
    try:
        if terminal_present:
            terminal.add_line('Generating Inerface', number=2)
            terminal.add_line('Selected Modules: ' + ' ,'.join(modules))
        else:
            print('Generating Inerface')
            print('Selected Modules: ' + ' ,'.join(modules))
        writing_modules = [m for m in lib.modules if m.name in modules]
        for m in writing_modules:
            interface += m.write_interface()
            print('\n'.join(interface))
        if terminal_present:
            terminal.add_line('Inerface Generated Correctly', number=2)
        else:
            print('Inerface Generated Correctly')
        return '\n'.join(interface)
    except Exception as e:
        if terminal_present:
            terminal.add_line('Error: ' + str(e), number=2)
        else:
            print(e)
        return None


def py_interface_writer(lib, modules, lib_name, **kwargs):
    """
        Generates an intermediate interface for f2py from certain modules.

        Args:
            lib (fparser.Flibrary): Library from which to make the interface.
            modules (list): List of strings  

        Returns:
            A string with the interface to print on a file.
    """
    terminal_present = False
    if 'terminal' in kwargs:
        terminal_present = True
        terminal = kwargs['terminal']
        terminal.add_line('')
    try:
        interface = list()
        interface.append('import {}'.format(lib_name))
        writing_modules = [m for m in lib.modules if m.name in modules]
        for m in writing_modules:
            interface += m.write_py_interface(lib_name)
            print('\n'.join(interface))
        return '\n'.join(interface)
    except Exception as e:
        if terminal_present:
            terminal.add_line('Error: ' + str(e), number=2)
        else:
            print(e)
        return None

if __name__ == '__main__':
    test_module1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule1.f90')
    test_module2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule2.f90')
    test_module3 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule3.f90')
    Lib = library_maker([test_module1, test_module2] ) #, test_module3])
    interface_writer(Lib, ['test_module_1', 'test_module_12', 'test_module_2', 'test_module_3'])
    py_interface_writer(Lib, ['test_module_1', 'test_module_12', 'test_module_2', 'test_module_3'], 'nh')