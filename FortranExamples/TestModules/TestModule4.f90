MODULE test_module_4
use test_module_3
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

! Test Subroutine 4 description
! Additional lines
subroutine test_multiple_dimensions(x, y, Solution, interface_function)
    real(8), intent(in):: x(0:, 0:) ! Description of x
    real(8), intent(in) :: y(0:) ! Description of y
    real(8), intent(inout) :: Solution(0:size(x)-1, 0:size(y)-1) ! Description of output
    interface
        function interface_function(x, y)
            real(8):: x(0:, 0:)
            real(8):: y(0:)
            real(8):: interface_function(0:size(x)-1, 0:size(y)-1)
        end function
    end interface
    Solution = interface_function(x, y)
end subroutine

function test_procedures(F, x) result(U)
  procedure (FunctionRN_RN) :: F 
  real, intent(in) :: x(:)
  real :: U( size(x), size(x) ) 

   integer ::  j, N  
   real :: xj( size(x) ) 

    N = size(X) 
  
    do j = 1, N 
       xj = 0
       xj(j) = 1d-3
       U(:,j) =  ( F(x + xj) - F(x - xj) )/norm2(2*xj);
    enddo 

end function 
end module