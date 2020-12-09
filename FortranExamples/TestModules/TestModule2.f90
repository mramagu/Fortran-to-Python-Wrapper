MODULE test_module_2
use test_module_12, only: test_function_12
use test_module_1
implicit none

private
public test_function_2, test_subroutine_1

contains
! Test Function 2 description
! Additional lines
pure function test_function_2(x, y)
    real(8), intent(in):: x, y ! Definition of x and y
    real(8):: test_function_2
    test_function_2 = x + y
end function

! Test Subroutine 1 description
! Additional lines

subroutine test_subroutine_1(x, y, z, comp, char, True)
    real, dimension(10), intent(in) :: x ! X variable description
    real, dimension(10), intent(inout) ::z(2)
    integer, dimension(10) :: y 
    complex :: comp
    character(len=10) :: char
    logical:: True, False
    print*, x, y, z, comp, char, True
    z = 1.
end subroutine
end module