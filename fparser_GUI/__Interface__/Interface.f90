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
real,dimension(10,2), intent(inout)  :: z
complex :: comp
character(len=10) :: char
logical :: True
call test_subroutine_1(x,y,z,comp,char,True)
end subroutine
end module