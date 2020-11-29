import fobjects

import os

if __name__ == '__main__':
    test_module1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule2.f90')
    file1 = open(test_module1, 'r') 
    file_code = file1.readlines() 

    for i, line in enumerate(file_code):
        file_code[i] = line.replace('\n', '')
    file = fobjects.Ffile('TestModule2', file_code)
    print(file)