MODULE test_module_3
use test_module_2
implicit none

interface
     function procedure_function(x) result(F) 
      real, intent(in) :: x(:) 
      real :: F( size(x) ) 
     end function 
end interface 

contains
! Test Function 3 description
! Additional lines
real function test_function_3(x) result(M)
    real(8), intent(in):: x(0:)
    M = 1d0
end function
!Test Function 4 description
!Additional lines
function test_function_4(x, interface_function)
    real(8), intent(in):: x(0:)
    real(8) :: test_function_4(0:size(x))
    interface
        function interface_function(x)
            real(8):: x(0:)
            real(8):: interface_function(0:size(x))
        end function
    end interface
    test_function_4 = interface_function(x)
    contains
        function contains_function(x,y)
            real(8), intent(in):: x, y ! Definition of x and y
            real(8):: contains_function
            contains_function = x-y
        end function
end function
end module