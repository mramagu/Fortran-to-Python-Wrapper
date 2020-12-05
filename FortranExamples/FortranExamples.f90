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
end program FortranExamples