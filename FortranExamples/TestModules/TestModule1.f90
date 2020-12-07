modUle test_module_1
implicit none

contains
real  function test_function_1(x, y)
    real(8):: x, y ! Definicion de x e y
    test_function_1 = x +&
        y 
end function

end module
    
Module test_module_12
use test_module_1 
implicit none

contains
real  function test_function_12(x, y)
    real(8):: x, y
    test_function_12 = x +&
        y
end function

    end module
    