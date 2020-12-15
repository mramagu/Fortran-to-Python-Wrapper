module Jacobian_module

  implicit none    
    
    
interface  
    function FunctionRN_RN(x) result(F) 
      real, intent(in) :: x(:) 
      real :: F( size(x) ) 
     end function 
end interface  

interface  
    function FunctionRN_RNE(x) result(F) 
      real, target :: x(:) 
      real :: F( size(x) ) 
     end function 
end interface 


contains 

!**********************************************************************
!*  Jacobian of a vector of functions F ( x in ) 
!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
!**********************************************************************
function Jacobian( F, xp ) 
  procedure (FunctionRN_RN) :: F 
  real, intent(in) :: xp(:)
  real :: Jacobian( size(xp), size(xp) ) 

   integer ::  j, N  
   real :: xj( size(xp) ) 

    N = size(Xp) 
  
    do j = 1, N 
       xj = 0
       xj(j) = 1d-3
       Jacobian(:,j) =  ( F(xp + xj) - F(xp - xj) )/norm2(2*xj);
    enddo 

end function 


!**********************************************************************
!*  Jacobian of a vector of functions F ( x inout )  
!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
!**********************************************************************
function Jacobianc( F, xp )
 procedure (FunctionRN_RNE) :: F 
  
  real, intent(in) :: xp(:)
  real :: Jacobianc( size(xp), size(xp) ) 

   integer ::  i, j, N  
   real :: xj( size(xp) ) 


    N = size(xp) 
    
    do j = 1, N 
       xj = 0
       xj(j) = 1d-3
       Jacobianc(:,j) =  ( F(xp + xj) - F(xp - xj) )/norm2(2*xj);
      
    enddo 
    
   ! do i = 1, N 
   !    write(*,'(a15,100f9.3)' ) " J = ", Jacobianc(i, :)
   ! enddo 
   !read(*,*) 
      


end function




end module 
