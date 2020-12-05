MODULE test_module_3
use test_module_2
implicit none

    contains
! Test Function 3 description
! Additional lines
real function test_function_3(x) result(M)
    real(8), intent(in):: x(0:)
    M = 1d0
end function
! Test Function 4 description
! Additional lines
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
end function
end module