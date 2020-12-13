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
module test_module_2_py
use test_module_2
implicit none
contains
pure function test_function_2_py(x,y)
real(8), intent(in) :: x
real(8), intent(in) :: y
real(8) :: test_function_2_py
test_function_2_py = test_function_2(x,y)
end function
subroutine test_subroutine_1_py(x,y,z,comp,char,True)
real,dimension(10), intent(in)  :: x
integer,dimension(10) :: y
real,dimension(2), intent(inout)  :: z
complex :: comp
character(len=10) :: char
logical :: True
call test_subroutine_1(x,y,z,comp,char,True)
end subroutine
end module