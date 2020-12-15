module Gragg_Burlisch_Stoer 
    
    use ODE_interface
    use Linear_systems
    implicit none
   
    real, save :: Tolerance = 0  
    integer, save :: N_GBS_effort = 0 
 
    
    contains     
    
subroutine set_GBS_tolerance( eps)
      real, intent(in) :: eps
     
      Tolerance = eps
      
end subroutine

integer function get_GBS_effort() result(N) 
     
      N = N_GBS_effort
      
end function 


    
!*******************************************************************************
!    Modified Midpoint scheme
!    given an interval [t0,t] divided in 2n = number of steps in the interval 
!    and an initial value U(t0),
!    Gives back the value U(t) = Un
!
!    Francisco Javier Escoto Lopez
!*******************************************************************************  
subroutine Modified_midpoint_scheme( F, t0, t, U0, Un, n )   
       procedure (ODES) ::    F
       real, intent(in) ::    t0, t , U0(:)
       real, intent(out) ::   Un(:)
       integer, intent(in) :: n
   
       real :: ti, h, U( size(U0), 0:2*n+1 )
       integer ::  i 

        h = (t - t0) / ( 2*n )

        U(:,0) = U0 
        U(:,1) = U(:,0) + h * F( U(:,0), t0 ) 

        do i=1, 2*n 
            ti = t0 + i*h 
            U(:, i+1)  = U(:, i-1) + 2*h* F( U(:,i), ti ) 
        end do
        
        Un = ( U(:, 2*n-1) + 2 *  U(:, 2*n) + U(:, 2*n+1)  )/4.  
        
        N_GBS_effort = N_GBS_effort + 2*n + 1 
       
end subroutine
    
!*******************************************************************************
!    Richardson coefficients to compute Richardson's extrapolation given
!    a sequence of levels
!    Francisco Javier Escoto Lopez
!*******************************************************************************    
subroutine GBS_Richardson_coefficients(n, b) 
      integer, intent(in) :: n(:) 
      real, intent(out) :: b(:) 
      
      real :: ones( size(n)-1 ), A( size(n)-1, size(n)-1)  
      integer :: i, j, q 
     
    ! *** A^T computation
          q = size(n) - 1 
    
          do i = 1, q
             do j = 1, q
              A(j,i) = ( ( 1./n(i))**(2*j) - (1./n(i+1))**(2*j)  )
            end do
         end do
      
    ! *** Vector b computation
          ones = 1.  
          call LU_factorization( A )    
          b = Solve_LU( A , ones )
             
end subroutine     
    
!*******************************************************************************
!    Gragg-Bulirsch-Stoer (GBS) scheme
!    Francisco Javier Escoto Lopez
!    javier.escoto.lopez@gmail.com (2019) 
!    juanantonio.hernandez@upm.es  (2020)
!******************************************************************************* 
subroutine GBS_Scheme( F, t1, t2, U1, U2, ierr) 
      procedure (ODES) ::   F 
      real, intent(in) ::   t1, t2, U1(:)
      real, intent(out) ::  U2(:)
      integer, intent(out) :: ierr
      
     real, allocatable :: U(:, :), dU(:, :), b(:)
     integer, allocatable :: n(:)
     real :: Error( size( U1) )
     integer :: i, Nv, N_levels, Nmax = 9 
     
     Nv = size(U1) 
     if (Tolerance==0) Tolerance = 0.1
            
     N_levels = 1; Error = 10
     do while (norm2(Error) > Tolerance)
          
         if (N_levels > Nmax) then 
             write(*,*) "ERROR GBS Tolerance not reached", norm2(Error); exit
         end if
         N_levels = N_levels + 1     
         allocate( U( Nv, N_Levels ), dU( Nv, N_Levels-1 ) )
         allocate( n(N_Levels), b(N_Levels-1) )
     
   ! *** Partition sequence definition
         n = [(i, i=1, N_levels)]
         
   ! *** Richardson extrapolation coeffcicients
         call GBS_Richardson_coefficients(n, b) 
        
   ! *** Modified midpoint scheme for each level
         do i = 1, N_Levels
            call Modified_midpoint_scheme( F, t1, t2, U1, U(:, i), n(i) )
         end do
         
   ! *** Error by means of the difference between solutions j and j+1  
         do i = 1, N_Levels - 1
              dU(:, i)  = U(:, i+1) - U(:, i)
         end do
         Error(:) = matmul( dU(:,:) , b )
     
   ! *** Solution correction j=1
         U(:, 1) = U(:, 1) + Error(:)
        
   ! *** Final solution
         U2 = U(:, 1); ierr = 0
         deallocate( U, dU, n, b)
          
     end do
end subroutine

end module 