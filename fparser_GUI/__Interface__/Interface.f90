module test_module_1_py
use test_module_1
implicit none
contains
real function test_function_1_py(x,y)
real(8) :: x
real(8) :: y
test_function_1_py = test_function_1(x,y)
end function
end module
module test_module_12_py
use test_module_12
implicit none
contains
real function test_function_12_py(x,y)
real(8) :: x
real(8) :: y
test_function_12_py = test_function_12(x,y)
end function
end module