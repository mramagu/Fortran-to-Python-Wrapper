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
real,dimension(10,2), intent(inout)  :: z
complex :: comp
character(len=10) :: char
logical :: True
call test_subroutine_1(x,y,z,comp,char,True)
end subroutine
end module
module test_module_3_py
use test_module_3
implicit none
contains
real function test_function_3_py(x,N_x)
real(8),dimension(N_x), intent(in) :: x
integer, intent(in), optional  :: N_x
test_function_3_py = test_function_3(x)
end function
function test_function_4_py(x,interface_function,N_x)
real(8),dimension(N_x), intent(in) :: x
integer, intent(in), optional  :: N_x
real(8),dimension(0:size(x)) :: test_function_4_py
interface
function interface_function(x,N_x)
real(8),dimension(N_x) :: x
integer, intent(in), optional  :: N_x
real(8),dimension(0:size(x)) :: interface_function
end function
end interface
test_function_4_py = test_function_4(x,interface_function)
end function
end module