MODULE test_module_4
use test_module_2
implicit none

contains
! Test Subroutine 4 description
! Additional lines
subroutine test_subroutine_4(x, y, Solution, interface_function)
    real(8), intent(in):: x(0:) ! Description of x
    real(8), intent(in) :: y(0:) ! Description of y
    real(8), intent(inout) :: Solution(0:size(x)-1, 0:size(y)-1) ! Description of output
    interface
        function interface_function(x, y)
            real(8):: x(0:)
            real(8):: y(0:)
            real(8):: interface_function(0:size(x)-1, 0:size(y)-1)
        end function
    end interface
    Solution = interface_function(x, y)
end subroutine

integer function test_empty() result(N)
    N = 5
end function
end module