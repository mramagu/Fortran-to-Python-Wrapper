import fobjects

import os

if __name__ == '__main__':
    test_module1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule1.f90')
    test_module2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      '../FortranExamples/TestModules/TestModule2.f90')
    file1 = open(test_module1, 'r') 
    file_code = file1.readlines() 
    for i, line in enumerate(file_code):
        file_code[i] = line.replace('\n', '')
    file_1 = fobjects.Ffile('TestModule2', file_code)
    file1.close()
    file2 = open(test_module2, 'r') 
    file_code = file2.readlines() 
    for i, line in enumerate(file_code):
        file_code[i] = line.replace('\n', '')
    file_2 = fobjects.Ffile('TestModule2', file_code)
    file2.close()
    Lib = fobjects.Flibrary([file_2, file_1])
    print(Lib)