import fobjects

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

if __name__ == '__main__':
    test_module1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule1.f90')
    file1 = open(test_module1, 'r') 
    file_code = file1.readlines() 

    for i, line in enumerate(file_code):
        file_code[i] = line.replace('\n', '')
    file = fobjects.Ffile('TestModule1', file_code)
    print(file)