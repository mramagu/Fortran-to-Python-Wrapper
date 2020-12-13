import test_interfacef
class test_module_1:
    def test_function_1(x,y):
        """
            x (real(8)): ! Definicion de x e y
            y (real(8)): ! Definicion de x e y
        """
        return test_interfacef.test_module_1_py.test_function_1_py(x,y)
class test_module_12:
    def test_function_12(x,y):
        """
            x (real(8)): None
            y (real(8)): None
        """
        return test_interfacef.test_module_12_py.test_function_12_py(x,y)
class test_module_2:
    def test_function_2(x,y):
        """
            ! Test Function 2 description
            ! Additional lines
            x (real(8)): ! Definition of x and y
            y (real(8)): ! Definition of x and y
        """
        return test_interfacef.test_module_2_py.test_function_2_py(x,y)
    def test_subroutine_1(x,y,z,comp,char,True):
        """
            ! Test Subroutine 1 description
            ! Additional lines
            x (real): ! X variable description
            y (integer): None
            z (real): None
            comp (complex): None
            char (character(len=10)): None
            True (logical): None
        """
        test_interfacef.test_module_2_py.test_subroutine_1_py(x,y,z,comp,char,True)