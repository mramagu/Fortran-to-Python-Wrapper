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
implicit none


! Variables
real(8):: x, y
! Body of FortranExamples
x = 3d0
y = 4d0
print *, test_function_1(x, y)
read *, x

! Test Function 2 description
! Additional lines
pure function test_function_2(x, y)
    real(8), intent(in):: x, y ! Definition of x and y
    real(8):: test_function_2
contains

  function test_function_3(x,y)
   test_function_3 = x-y
  end function
  
    test_function_2 = x + y
contains
  function test_function_4(x,y)
   test_function_4 = x*y
  end function
  
end function

end program FortranExamples
