from Classes import Module

import os

def example_add_func(x, y):
    """
    Adds two numbers together

    Args:
        x (float): Number to add
        y (float): Number to add

    Returns:
        float: a sum of both numbers
    """

    return x + y

def find_modules(filename, file_code):
    """
    Function that finds all modules within a fortran file

    Args:
        filename (string): Name of the file
        file_code (string): Code within said file

    Returns:
        list: A list with all module objects
    """
    modules = list()
    modules_code = list()
    module_str = list()
    module_line = False
    for i, line in enumerate(file_code):
        if module_line:
            module_str.append(line)

        if 'module' in line and 'end' not in line:
            module_line = True
            module_str.append(line)
        elif 'module' in line and 'end' in line:
            module_line = False
            modules_code.append(module_str)
            module_str = list()
    
    for i in modules_code:
        modules.append(Module.Module(filename, i))
    return modules

if __name__ == '__main__':
    test_module1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule1.f90')
    file1 = open(test_module1, 'r') 
    file_code = file1.readlines() 

    for i, line in enumerate(file_code):
        file_code[i] = line.replace('\n', '')
    modules = find_modules('TestModule1', file_code)
    for m in modules:
        print(m.code)