module Linear_systems 

implicit none 
! private 
! public ::               & 
!   LU_factorization,     & ! A  = L U (lower, upper triangle matrices)
!   Solve_LU,             & ! It solves L U x = b   
!   Gauss,                & ! It solves A x = b by Guass elimination
!   Condition_number,     & ! Kappa(A)  = norm2(A)  * norm2( inverse(A) )
!   Tensor_product,       & ! A_ij = u_i v_j 
!   Power_method,         & ! It determines to largest eigenvalue of A 
!   Inverse_Power_method, & ! It determines the smallest eigenvalue of A
!   Eigenvalues_PM,       & ! All eigenvalue of A by the power method
!   SVD                     ! A = U S transpose(V)  


contains 
!***************************************************************************
!*   Factorization of A by means of upper and lower triangle matrices 
!*          input  : A matrix 
!*          output : A  holds L U 
!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
!***************************************************************************
subroutine LU_factorization( A ) 
      real, intent(inout) :: A(:, :) 

  integer :: N
  integer :: k, i, j 
  N =size(A, dim =1) 
 
  A(1, :) = A(1,:) 
  A(2:N,1) = A(2:N,1)/A(1,1) 

  do k=2, N 
   do j=k, N
       A(k,j) =  A(k,j) - dot_product( A(k, 1:k-1), A(1:k-1, j) )
   end do   
   
   do i=k+1, N
       A(i,k) = (A(i,k) - dot_product( A(1:k-1, k), A(i, 1:k-1) ) )/A(k,k) 
   end do 
  end do 
end subroutine

!***************************************************************************
!* LU x = b 
!***************************************************************************
function Solve_LU( A, b ) 
  real, intent(in) :: A(:, :), b(:) 
  real :: Solve_LU( size(b) )  

   real :: y (size(b)), x(size(b))
   integer :: i, N
  
   N = size(b) 

   y(1) = b(1)
   do i=2,N
          y(i) = b(i) - dot_product( A(i, 1:i-1), y(1:i-1) )
   enddo

    x(N) = y(N) / A(N,N)
    do i=N-1, 1, -1
     x(i) = (y(i) - dot_product( A(i, i+1:N), x(i+1:N) ) )/ A(i,i)
    end do

    Solve_LU = x 

end function 


!***************************************************************************
!* Classical Gaussian elimination 
!***************************************************************************
function  Gauss( A, b ) 
  real, intent(inout) :: A(:, :), b(:)  
  real :: Gauss(size(b)) 

  integer :: N
  integer :: k, i, j, i_max(1), ip
  real :: l ! multiplier   
  real :: x(size(b)) 

  
 N =size(A, dim =1) 
 do k=1, N 

   i_max = maxloc( abs( A(k:N,k) ) ) 
   ip = i_max(1) 
   if ( A(ip, k) == 0 ) then 
                               write(*,*) " error:  Matrix is singular! "
                               stop 
                           endif
   call Swap( A(k,:), A(ip,:) ) 
   call Swap( b(k:k), b(ip:ip) )                           
   

   do i = k + 1, N  ! for all rows below pivot:
     l = A(i, k) / A(k,k)  
     A(i, 1:k) = 0 
     do j = k+1, N
         A(i, j) = A(i, j) - l * A(k, j) 
     end do     
     b(i) = b(i) - l * b(k) 
   enddo 

 enddo 

 x(N) = b(N) / A(N,N) 
 do i = N-1, 1, -1  
   x(i) = ( b(i) - dot_product( A(i,i+1:N), x(i+1:N) ) )/ A(i,i) 
 enddo 

 Gauss = x 

end function
!***************************************************************************
!* Swap two vectors 
!***************************************************************************
subroutine Swap( A, B ) 
  real, intent(inout) :: A(:), B(:)  

  real :: temp( size(A) ) 

   temp = A
   A = B
   A = temp 

end subroutine






!****************************************************************
!* Power method  to obtain the largest eigenvalue of a square matrix A 
!*          input  : A matrix 
!*
!*          output : lambda eigenvalue 
!*                   U eigenvector 
!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
!****************************************************************
subroutine Power_method(A, lambda, U) 
      real, intent(in) :: A(:,:)
      real, intent(out) :: lambda, U(:) 
  
  integer :: N, k, k_max = 10000 
  real, allocatable :: U0(:), V(:)  
  
    N = size( A, dim=1) 
    allocate( U0(N), V(N) ) 
    U = [ (k, k=1, N) ] 
    
    k = 1 
    do while( norm2(U-U0) > 1d-12 .and. k < k_max )  
         U0 = U
         V = matmul( A, U ) 
         U = V / norm2(V) 
         k = k + 1         
    end do 
    
    lambda = dot_product( U, matmul(A, U) )    
    
    
end subroutine 

!****************************************************************
! Inverse Power method to obtain the smallest eigenvalue of a square matrix A 
!*          input  : A matrix 
!*
!*          output : lambda eigenvalue 
!*                   U eigenvector 
!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
!****************************************************************
subroutine Inverse_power_method(A, lambda, U) 
      real, intent(inout) :: A(:,:)
      real, intent(out) :: lambda, U(:) 
  
  integer :: N, k, k_max = 10000 
  real, allocatable :: U0(:), V(:), Ac(:, :)   
 
  
    N = size(U) 
    allocate ( Ac(N,N), U0(N), V(N) ) 
  
    Ac = A 
    call LU_factorization(Ac) 
    U = [ (k, k=1, N) ] 

    k = 1 
    do while( norm2(U-U0) > 1d-12 .and. k < k_max )  
        
         U0 = U 
         V = solve_LU(Ac, U) 
         U = V / norm2(V) 
         k = k + 1         
    end do 
    
    lambda = norm2(matmul(A, U))      
    
    
end subroutine 

!****************************************************************
!* Eigenvalues of a square matrix A.
!* It calculates by the power method the largest eigenvalue. 
!* Then, it builds a new matrix by removing the last eigenvalue. 
!*
!*          input  : A(:,:) 
!*
!*          output : lambda(k), k  eigenvalue
!*                   U(:,k),  eigenvector associated to lambda(k)
!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
!****************************************************************
subroutine Eigenvalues_PM(A, lambda, U) 
      real, intent(inout) :: A(:,:)
      real, intent(out) :: lambda(:), U(:,:) 
  
      integer :: i, j, k, N 
      
      N = size(A, dim=1) 
      
      do k=1, N 
          
          call Power_method(A, lambda(k), U(:, k) ) 
       
          A = A - lambda(k) * Tensor_product( U(:, k), U(:, k) )  
          
      end do 
      
end subroutine 


!****************************************************************
! SVD decomposition of a real matrix A 
!*                   A = U S transpose(V)  
!*
!*    input  : A(:,:) 
!*
!*    output : 
!*            sigma(k) singular values
!*                     sigma(k)**2 are  eigenvalues of transpose(A) * A 
!*            V(:,k)   eigenvector of transpose(A) * A 
!*            U(:,k)   eigenvector of  A * transpose(A) 
!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
!****************************************************************
subroutine SVD(A, sigma, U, V) 
      real, intent(in) :: A(:,:)
      real, intent(out) :: sigma(:), U(:,:), V(:,:)  
  
      integer :: i, N 
      real, allocatable :: B(:,:) 
      
      N = size(A, dim=1) 
      
      B = matmul( transpose(A), A ) 
      call Eigenvalues_PM( B, sigma, V ) 
      sigma = sqrt(sigma)
      
      do i=1, N 
         
          if ( abs(sigma(i)) > 1d-10 ) then 
                U(:,i) = matmul( A, V(:, i) ) / sigma(i)
          else 
                write(*,*) " Singular value is zero" 
                stop 
          end if 
          
      end do     
        
    
end subroutine 



!****************************************************************
!* Condition number of a real  matrix A 
!*                   Kappa(A)  = norm2(A)  * norm2( inverse(A) ) 
!*
!* The norm2 of a real matrix A is its largest singular value 
!* From the SVD decomposition of a matrix
!*      A = U D transpose(V), 
!*      inverse(A) = V inverse(D) transpose(U) 
!* Hence, norm2( inverse(A) ) is the smallest singular value. 
!* The smallest value is calculated by means of the Inverse power method. 
!*
!*    input  : A(:,:) 
!*
!*    output : 
!*            Condition_number 

!*
!*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es)  
!****************************************************************
real function Condition_number(A) 
      real, intent(in) :: A(:,:)
    
  
      integer :: i, j, k, N 
      real, allocatable :: B(:,:), U(:) 
      real :: sigma_max, sigma_min, lambda  
      
      N = size(A, dim=1)
      allocate( U(N), B(N,N) ) 
      B = matmul( transpose(A), A ) 
      
      
     call Power_method( B,  lambda, U ) 
     sigma_max = sqrt(lambda) 
     
     call Inverse_power_method( B,  lambda, U )
     sigma_min = sqrt(lambda) 
     
     Condition_number = sigma_max / sigma_min  
   
    
end function  



!************************************************************************
!* Band width = 2 * rj  + 1 
!************************************************************************
subroutine LU_band_factorization( A , rj) 
  real, intent(inout) :: A(:, :) 
  integer, intent (in) :: rj 
  
  integer :: N, r
  integer :: k, i, j
  
      
      N =size(A, dim =1) 
      r= rj+1
    
  A(1, :) = A(1,:) 
  A(2:N,1) = A(2:N,1)/A(1,1) 

 
  do k=2, r
      
     do i=k, N
         A(k,i) = A(k,i) - dot_product( A(k, 1:k-1), A(1:k-1, i)  )
     end do 
     
     do j=k+1, N
         A(j,k) = ( A(j,k) - dot_product( A(1:k-1, k), A(j, 1:k-1) ) )/A(k,k)
     end do     
    
  end do
     
  do k=r+1, N-r

   do i=k, k+r     
      A(k,i) = A(k,i) - dot_product(A(k, k-r:k-1), A(k-r:k-1, i) )
   end do 
   
   do j=k+1, k+r-1
      A(j,k) = (A(j,k)-dot_product(A(k-r+1:k-1, k), A(j, k-r+1:k-1) ))/A(k,k)
   end do     
   
  end do 
 
   do k=N-r+1, N
      
    do i=k, N     
        A(k,i) =  A(k,i) - dot_product(A(k, 1:k-1), A(1:k-1, i)  ) 
    end do 
    
    do j=k+1, N
       A(j,k) = (A(j,k) - dot_product(A(1:k-1, k), A(j, 1:k-1) ) )/A(k,k)                     
    end do 
                      
   end do

end subroutine


!************************************************************************
!* Band width = 2 * rj  + 1 
!************************************************************************
function Solve_LU_band( A, b, rj) 
  real, intent(in) :: A(:, :), b(:) 
  real :: Solve_LU_band( size(b) )
  integer, intent (in) :: rj

   real :: y (size(b)), x(size(b))
   integer :: i, N, r
  
   N = size(b) 
   r = rj +1

   y(1) = b(1)
   
   do i=2,r
          y(i) = b(i) - dot_product( A(i, 1:i-1), y(1:i-1) )   
   enddo
   
    do i=r+1,N
          y(i) = b(i) - dot_product( A(i, i-r:i-1), y(i-r:i-1) )
   enddo

   x(N) = y(N) / A(N,N)

   do i=N-1, N-r, -1
     x(i) = (y(i) - dot_product( A(i, i+1:N), x(i+1:N) ) )/ A(i,i)
   end do
    
   do i=N-r-1, 1, -1
     x(i) = (y(i) - dot_product( A(i, i+1:i+r), x(i+1:i+r) ) )/ A(i,i)
   end do

   Solve_LU_band = x 

end function 


!************************************************************************
!* Tensor product A_ij = u_i v_j 
!************************************************************************
function Tensor_product(u, v) result(A) 
     real, intent(in) :: u(:), v(:) 
     real A( size(u), size(v) ) 

     integer ::i, j, N, M 
     
     N = size(u) 
     M = size(v) 
     
     
     do i=1, N; do j=1, M 
         
         A(i,j) = u(i) * v(j) 
         
     end do;  end do 
     
     

end function 


end module 
