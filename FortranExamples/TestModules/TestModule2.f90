MODULE test_module_3
use test_module_2
use test_module_1
implicit none

contains
! Test Function 3 description
! Additional lines
pure function test_function_3(x, y)
    real(8), intent(in):: x, y ! Definition of x and y
    real(8):: test_function_3
    test_function_3 = x + y
end function

! Test Subroutine 1 description
! Additional lines

subroutine test_subroutine_1(x, y, z, comp, char, True)
    real, dimension(10), intent(in) :: x ! X variable description
    integer, dimension(10) :: y, z(2)
    complex :: comp
    character(len=10) :: char
    logical:: True 
    y(1) = int(test_function_2(x(1), 1d0))
end subroutine
end module