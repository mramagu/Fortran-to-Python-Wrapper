import fobjects
import fparsertools

import os
import copy

def library_maker(files, comment_style='before', **kwargs):
    """
        Makes a library out fortran files.

        Args:
            files (list): List of strings with the files directories.
            comment_style (string): Style in which functions and subroutines are commented. 'after' or 'before'
                default =  'before'

        Kwargs:
            terminal: Terminal in which to write what the program is doing and the problems its encountering.

        Returns:
            A Flibrary made up of all the fortran files. 
    """
    terminal_present = False
    if 'terminal' in kwargs:
        terminal_present = True
        terminal = kwargs['terminal']
        terminal.add_line('')
        terminal.add_line('Generating Library...')
    else:
        print('Generating Library...')
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
            fortran_files.append(fobjects.Ffile(file_dir, fparsertools.multiple_and_remover(file_code), comment_style=comment_style))

        Lib=fobjects.Flibrary(fortran_files)
        if terminal_present:
            terminal.add_line('Success: Library Generated')
        else:
            print('Success: Library Generated')
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
            lib (fobjects.Flibrary): Library from which to make the interface.
            modules (list): List of strings  

        Kwargs:
            terminal: Terminal in which to write what the program is doing and the problems its encountering.

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
            terminal.add_line('Generating f2py Interface...', number=2)
            terminal.add_line('Selected Modules: ' + ' ,'.join(modules))
        else:
            print('Generating f2py Interface...')
            print('Selected Modules: ' + ' ,'.join(modules))
        writing_modules = [m for m in lib.modules if m.name in modules]
        for m in writing_modules:
            add_interface = m.write_f2py_interface()
            if len(add_interface) > 5:
                interface += add_interface
            else:
                if terminal_present:
                    terminal.add_line('Warning: Not generating interface for module {}. Empty contents.'.format(m.name))
                else:
                    print('Warning: Not generating interface for module {}. Empty contents.'.format(m.name))       
        if terminal_present:
            terminal.add_line('Success: f2py Interface Generated', number=2)
        else:
            print('Success: f2py Interface Generated')
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
            lib (fobjects.Flibrary): Library from which to make the interface.
            modules (list): List of strings.

        Kwargs:
            terminal: Terminal in which to write what the program is doing and the problems its encountering.

        Returns:
            A string with the interface to print on a file.
    """
    terminal_present = False
    if 'terminal' in kwargs:
        terminal_present = True
        terminal = kwargs['terminal']
        terminal.add_line('')
        terminal.add_line('Generating Python Interface...', number=2)
        terminal.add_line('Selected Modules: ' + ' ,'.join(modules))
    else:
        print('Generating Python Interface...')
        print('Selected Modules: ' + ' ,'.join(modules))

    try:
        interface = list()
        lib_copy = copy.deepcopy(lib)
        interface.append('import {}'.format(lib_name))
        writing_modules = [m for m in lib_copy.modules if m.name in modules]
        for m in writing_modules:
            m.solve_keywords()
            add_interface = m.write_py_interface(lib_name)
            if len(add_interface) > 1:
                interface += add_interface
            else:
                if terminal_present:
                    terminal.add_line('Warning: Not generating interface for module {}. Empty contents.'.format(m.name))
                else:
                    print('Warning: Not generating interface for module {}. Empty contents.'.format(m.name))     
        if terminal_present:
            terminal.add_line('Success: Python Interface Generated', number=2)
        else:
            print('Success: Python Interface Generated')
        return '\n'.join(interface)
    except Exception as e:
        if terminal_present:
            terminal.add_line('Error: ' + str(e), number=2)
        else:
            print(e)
        return None

def increase_precision(code, var_type, new_precision, **kwargs):
    """
        Function to increase the precision of a variable type in the fortran code.

        Args:
            code (list): List of strings containing the code.
            var_type (string): Type of variable to change the precision.  
            new_precision (int): New Variable precision

        Kwargs:
            terminal: Terminal in which to write what the program is doing and the problems its encountering.

        Returns:
            An altered list of strings with the new precision.
    """
    terminal_present = False
    if 'terminal' in kwargs:
        terminal_present = True
        terminal = kwargs['terminal']
        terminal.add_line('')
        terminal.add_line('Increasing precision of {} variables to {}...'.format(var_type, new_precision))
    else:
        print('Increasing precision of {} variable to {}...'.format(var_type, new_precision))
    try:
        for i, line in enumerate(code):
            position = fparsertools.find_command(line, var_type)
            if position != None:
                position += len(var_type)
                if line[position] == '(' and line[position + 1].lower() != 'k':
                    position += 1
                    closing_parenthesis = fparsertools.find_closing_parenthesis(line, position)
                    old_precision = int(line[position:closing_parenthesis])
                    final_position = closing_parenthesis
                elif line[position] == '(' and line[position + 1].lower() == 'k':
                    position += len('(kind=')
                    closing_parenthesis = fparsertools.find_closing_parenthesis(line, position)
                    old_precision = int(line[position: closing_parenthesis])
                    final_position = closing_parenthesis
                elif line[position] == '*':
                    position += 1
                    next_item = (line.find(' ', position), line.find(',', position),
                        line.find(':', position))
                    min = len(line)
                    for j in next_item:
                        if j < min and j != -1:
                            min = j
                    old_precision = int(line[position: min])
                    final_position = min - 1
                else:
                    old_precision = 0
                    position += 1
                    final_position = position
                    if old_precision < new_precision:
                        code[i] = line[:position-1] + '()' + line[position-1:]
                    
                if old_precision < new_precision:
                    code[i] = code[i][:position] + '{}'.format(new_precision) + code[i][final_position + len(str(old_precision)) - 1:]

        if terminal_present:
            terminal.add_line('Success: Increased Precision')
        else:
            print('Success: Increased Precision')
        return code
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
    test_module4 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule4.f90')
    Lib = library_maker([test_module1, test_module2, test_module3, test_module4])
    print(interface_writer(Lib, ['test_module_1', 'test_module_12', 'test_module_2', 'test_module_3', 'test_module_4']))
    print(py_interface_writer(Lib, ['test_module_1', 'test_module_12', 'test_module_2', 'test_module_3', 'test_module_4'], 'nh'))
