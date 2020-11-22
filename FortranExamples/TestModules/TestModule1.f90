modUle test_module_1
implicit none

contains
real  function test_function_1(x, y)
    real(8):: x, y
    test_function_1 = x + y 
end function

end module
    
Module test_module_2
use &
    test_module_1
implicit none

contains
real  function test_function_2(x, y)
    real(8):: x, y
    test_function_2 = x + y
end function

end module