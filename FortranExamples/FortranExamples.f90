!  FortranExamples.f90 
!
!  FUNCTIONS:
!  FortranExamples - Entry point of console application.
!

!****************************************************************************
!
!  PROGRAM: FortranExamples
!
!  PURPOSE:  Entry point for the console application.
!
!****************************************************************************


program FortranExamples
use test_module_1
use test_module_2
use test_module_3
use test_module_4
implicit none


! Variables
real(8):: x, y
! Body of FortranExamples
x = 3d0
y = 4d0
print *, test_function_1(x, y)
read *, x

contains

  function test_function_31(x,y)
  real(8), intent(in):: x, y ! Definition of x and y
    real(8):: test_function_31
   test_function_31 = x-y
  end function

  function test_function_41(x,y)
    real(8), intent(in):: x, y ! Definition of x and y
    real(8):: test_function_41
   test_function_41 = x*y
  end function

end program FortranExamples
