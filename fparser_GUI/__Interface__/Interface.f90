module Lagrange_interpolation_py
use Lagrange_interpolation
implicit none
contains
pure function Lagrange_polynomials_py(x,xp,N_x)
real,dimension(N_x), intent(in)  :: x
real, intent(in)  :: xp
integer, intent(in) :: N_x
real,dimension(-1:size(x)-1,0:size(x)-1) :: Lagrange_polynomials_py
Lagrange_polynomials_py = Lagrange_polynomials(x,xp)
end function
function Stencilv_py(Order,N)
integer, intent(in)  :: Order
integer, intent(in)  :: N
integer,dimension(0:N) :: Stencilv_py
Stencilv_py = Stencilv(Order,N)
end function
function Lagrange_error_polynomial_py(x,xp,N_x)
real,dimension(N_x), intent(in)  :: x
real, intent(in)  :: xp
integer, intent(in) :: N_x
real,dimension(0:size(x)) :: Lagrange_error_polynomial_py
Lagrange_error_polynomial_py = Lagrange_error_polynomial(x,xp)
end function
pure function Lebesgue_functions_py(x,xp,N_x,N_xp)
real,dimension(N_x), intent(in)  :: x
real,dimension(N_xp), intent(in)  :: xp
integer, intent(in) :: N_x
integer, intent(in) :: N_xp
real,dimension(-1:size(x)-1, 0:size(xp)-1) :: Lebesgue_functions_py
Lebesgue_functions_py = Lebesgue_functions(x,xp)
end function
function PI_error_polynomial_py(x,xp,N_x,N_xp)
real,dimension(N_x), intent(in)  :: x
real,dimension(N_xp), intent(in)  :: xp
integer, intent(in) :: N_x
integer, intent(in) :: N_xp
real,dimension(0:size(x)-1, 0:size(xp)-1) :: PI_error_polynomial_py
PI_error_polynomial_py = PI_error_polynomial(x,xp)
end function
end module
module Linear_systems_py
use Linear_systems
implicit none
contains
function Solve_LU_py(A,b,N_A,N_Aq,N_b)
real,dimension(N_A,N_Aq), intent(in)  :: A
real,dimension(N_b), intent(in)  :: b
integer, intent(in) :: N_A
integer, intent(in) :: N_Aq
integer, intent(in) :: N_b
real,dimension(size(b)) :: Solve_LU_py
Solve_LU_py = Solve_LU(A,b)
end function
function Gauss_py(A,b,N_A,N_Ai,N_b)
real,dimension(N_A,N_Ai), intent(inout)  :: A
real,dimension(N_b), intent(inout)  :: b
integer, intent(in) :: N_A
integer, intent(in) :: N_Ai
integer, intent(in) :: N_b
real,dimension(size(b)) :: Gauss_py
Gauss_py = Gauss(A,b)
end function
real function Condition_number_py(A,N_A,N_Ao)
real,dimension(N_A,N_Ao), intent(in)  :: A
integer, intent(in) :: N_A
integer, intent(in) :: N_Ao
Condition_number_py = Condition_number(A)
end function
function Solve_LU_band_py(A,b,rj,N_A,N_Ab,N_b)
real,dimension(N_A,N_Ab), intent(in)  :: A
real,dimension(N_b), intent(in)  :: b
integer, intent (in)  :: rj
integer, intent(in) :: N_A
integer, intent(in) :: N_Ab
integer, intent(in) :: N_b
real,dimension(size(b)) :: Solve_LU_band_py
Solve_LU_band_py = Solve_LU_band(A,b,rj)
end function
function Tensor_product_py(u,v,N_u,N_v)
real,dimension(N_u), intent(in)  :: u
real,dimension(N_v), intent(in)  :: v
integer, intent(in) :: N_u
integer, intent(in) :: N_v
real,dimension(size(u), size(v)) :: Tensor_product_py
Tensor_product_py = Tensor_product(u,v)
end function
subroutine LU_factorization_py(A,N_A,N_As)
real,dimension(N_A,N_As), intent(inout)  :: A
integer, intent(in) :: N_A
integer, intent(in) :: N_As
call LU_factorization(A)
end subroutine
subroutine Swap_py(A,B,N_A,N_B)
real,dimension(N_A), intent(inout)  :: A
real,dimension(N_B), intent(inout)  :: B
integer, intent(in) :: N_A
integer, intent(in) :: N_B
call Swap(A,B)
end subroutine
subroutine Power_method_py(A,lambda,U,N_A,N_Ay,N_U)
real,dimension(N_A,N_Ay), intent(in)  :: A
real, intent(out)  :: lambda
real,dimension(N_U), intent(out)  :: U
integer, intent(in) :: N_A
integer, intent(in) :: N_Ay
integer, intent(in) :: N_U
call Power_method(A,lambda,U)
end subroutine
subroutine Inverse_power_method_py(A,lambda,U,N_A,N_Aw,N_U)
real,dimension(N_A,N_Aw), intent(inout)  :: A
real, intent(out)  :: lambda
real,dimension(N_U), intent(out)  :: U
integer, intent(in) :: N_A
integer, intent(in) :: N_Aw
integer, intent(in) :: N_U
call Inverse_power_method(A,lambda,U)
end subroutine
subroutine Eigenvalues_PM_py(A,lambda,U,N_A,N_Ax,N_lambda,N_U,N_Ud)
real,dimension(N_A,N_Ax), intent(inout)  :: A
real,dimension(N_lambda), intent(out)  :: lambda
real,dimension(N_U,N_Ud), intent(out)  :: U
integer, intent(in) :: N_A
integer, intent(in) :: N_Ax
integer, intent(in) :: N_lambda
integer, intent(in) :: N_U
integer, intent(in) :: N_Ud
call Eigenvalues_PM(A,lambda,U)
end subroutine
subroutine SVD_py(A,sigma,U,V,N_A,N_As,N_sigma,N_U,N_Ux,N_V,N_Vr)
real,dimension(N_A,N_As), intent(in)  :: A
real,dimension(N_sigma), intent(out)  :: sigma
real,dimension(N_U,N_Ux), intent(out)  :: U
real,dimension(N_V,N_Vr), intent(out)  :: V
integer, intent(in) :: N_A
integer, intent(in) :: N_As
integer, intent(in) :: N_sigma
integer, intent(in) :: N_U
integer, intent(in) :: N_Ux
integer, intent(in) :: N_V
integer, intent(in) :: N_Vr
call SVD(A,sigma,U,V)
end subroutine
subroutine LU_band_factorization_py(A,rj,N_A,N_Aw)
real,dimension(N_A,N_Aw), intent(inout)  :: A
integer, intent (in)  :: rj
integer, intent(in) :: N_A
integer, intent(in) :: N_Aw
call LU_band_factorization(A,rj)
end subroutine
end module
module ODE_Interface_py
use ODE_Interface
implicit none
contains
end module
module Jacobian_module_py
use Jacobian_module
implicit none
contains
function Jacobian_py(FunctionRN_RN,xp,N_xp)
real,dimension(N_xp), intent(in)  :: xp
integer, intent(in) :: N_xp
real,dimension(size(xp), size(xp)) :: Jacobian_py
interface
function FunctionRN_RN(i,x,N_x)
integer :: i
real,dimension(N_x), intent(in)  :: x
integer, intent(in) :: N_x
real :: FunctionRN_RN
end function
end interface
Jacobian_py = Jacobian(FunctionRN_RN_py,xp)
contains
function FunctionRN_RN_py(x)
real,dimension(:), intent(in)  :: x
real,dimension(size(x)) :: FunctionRN_RN_py
integer::i
do i=1,size(x)
FunctionRN_RN_py(i) = FunctionRN_RN(i,x,size(x(:)))
end do
end function
end function
function Jacobianc_py(FunctionRN_RNE,xp,N_xp)
real,dimension(N_xp), intent(in)  :: xp
integer, intent(in) :: N_xp
real,dimension(size(xp), size(xp)) :: Jacobianc_py
interface
function FunctionRN_RNE(i,x,N_x)
integer :: i
real,dimension(N_x), target  :: x
integer, intent(in) :: N_x
real :: FunctionRN_RNE
end function
end interface
Jacobianc_py = Jacobianc(FunctionRN_RNE_py,xp)
contains
function FunctionRN_RNE_py(x)
real,dimension(:), target  :: x
real,dimension(size(x)) :: FunctionRN_RNE_py
integer::i
do i=1,size(x)
FunctionRN_RNE_py(i) = FunctionRN_RNE(i,x,size(x(:)))
end do
end function
end function
end module
module Temporal_scheme_interface_py
use Temporal_scheme_interface
implicit none
contains
end module
module Embedded_RKs_py
use Embedded_RKs
implicit none
contains
integer function get_eRK_effort_py()
get_eRK_effort_py = get_eRK_effort()
end function
real function Step_size_py(dU,tolerance,q,h,N_dU)
real,dimension(N_dU), intent(in)  :: dU
real, intent(in)  :: tolerance
integer, intent(in)  :: q
real, intent(in)  :: h
integer, intent(in) :: N_dU
Step_size_py = Step_size(dU,tolerance,q,h)
end function
subroutine set_eRK_name_py(name)
character(len=*), intent(in)  :: name
call set_eRK_name(name)
end subroutine
subroutine set_eRK_tolerance_py(eps)
real, intent(in)  :: eps
call set_eRK_tolerance(eps)
end subroutine
subroutine ERK_scheme_py(F,t1,t2,U1,U2,ierr,N_U1,N_U2)
procedure (ODES) :: F
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
call ERK_scheme(F,t1,t2,U1,U2,ierr)
end subroutine
subroutine RK_scheme_py(name,tag,F,t1,t2,U1,U2,N_U1,N_U2)
character(len=*), intent(in)  :: name
character(len=*), intent(in)  :: tag
procedure (ODES) :: F
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
call RK_scheme(name,tag,F,t1,t2,U1,U2)
end subroutine
subroutine Butcher_array_py(name,Ne)
character(len=*), intent(in)  :: name
integer, intent(out)  :: Ne
call Butcher_array(name,Ne)
end subroutine
end module
module Wrappers_py
use Wrappers
implicit none
contains
integer function get_weRK_effort_py()
get_weRK_effort_py = get_weRK_effort()
end function
integer function get_wGBS_effort_py()
get_wGBS_effort_py = get_wGBS_effort()
end function
integer function get_wABM_effort_py()
get_wABM_effort_py = get_wABM_effort()
end function
subroutine set_weRK_name_py(name)
character(len=*), intent(in)  :: name
call set_weRK_name(name)
end subroutine
subroutine set_weRK_tolerance_py(eps)
real, intent(in)  :: eps
call set_weRK_tolerance(eps)
end subroutine
subroutine set_wGBS_tolerance_py(eps)
real, intent(in)  :: eps
call set_wGBS_tolerance(eps)
end subroutine
subroutine set_wABM_tolerance_py(eps)
real, intent(in)  :: eps
call set_wABM_tolerance(eps)
end subroutine
subroutine WERK_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call WERK(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine WODEX_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call WODEX(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine WODE113_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call WODE113(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
end module
module Gragg_Burlisch_Stoer_py
use Gragg_Burlisch_Stoer
implicit none
contains
integer function get_GBS_effort_py()
get_GBS_effort_py = get_GBS_effort()
end function
subroutine set_GBS_tolerance_py(eps)
real, intent(in)  :: eps
call set_GBS_tolerance(eps)
end subroutine
subroutine Modified_midpoint_scheme_py(F,t0,t,U0,Un,n,N_U0,N_Un)
procedure (ODES) :: F
real, intent(in)  :: t0
real, intent(in)  :: t
real,dimension(N_U0), intent(in)  :: U0
real,dimension(N_Un), intent(out)  :: Un
integer, intent(in)  :: n
integer, intent(in) :: N_U0
integer, intent(in) :: N_Un
call Modified_midpoint_scheme(F,t0,t,U0,Un,n)
end subroutine
subroutine GBS_Richardson_coefficients_py(n,b,N_n,N_b)
integer,dimension(N_n), intent(in)  :: n
real,dimension(N_b), intent(out)  :: b
integer, intent(in) :: N_n
integer, intent(in) :: N_b
call GBS_Richardson_coefficients(n,b)
end subroutine
subroutine GBS_Scheme_py(F,t1,t2,U1,U2,ierr,N_U1,N_U2)
procedure (ODES) :: F
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
call GBS_Scheme(F,t1,t2,U1,U2,ierr)
end subroutine
end module
module Non_Linear_Systems_py
use Non_Linear_Systems
implicit none
contains
subroutine Newton_py(FunctionRN_RN,x0,N_x0)
real,dimension(N_x0), intent(inout)  :: x0
integer, intent(in) :: N_x0
interface
function FunctionRN_RN(i,x,N_x)
integer :: i
real,dimension(N_x), intent(in)  :: x
integer, intent(in) :: N_x
real :: FunctionRN_RN
end function
end interface
call Newton(FunctionRN_RN_py,x0)
contains
function FunctionRN_RN_py(x)
real,dimension(:), intent(in)  :: x
real,dimension(size(x)) :: FunctionRN_RN_py
integer::i
do i=1,size(x)
FunctionRN_RN_py(i) = FunctionRN_RN(i,x,size(x(:)))
end do
end function
end subroutine
subroutine Newtonc_py(FunctionRN_RNE,x0,N_x0)
real,dimension(N_x0), intent(inout)  :: x0
integer, intent(in) :: N_x0
interface
function FunctionRN_RNE(i,x,N_x)
integer :: i
real,dimension(N_x), target  :: x
integer, intent(in) :: N_x
real :: FunctionRN_RNE
end function
end interface
call Newtonc(FunctionRN_RNE_py,x0)
contains
function FunctionRN_RNE_py(x)
real,dimension(:), target  :: x
real,dimension(size(x)) :: FunctionRN_RNE_py
integer::i
do i=1,size(x)
FunctionRN_RNE_py(i) = FunctionRN_RNE(i,x,size(x(:)))
end do
end function
end subroutine
end module
module Adams_Bashforth_Moulton_py
use Adams_Bashforth_Moulton
implicit none
contains
integer function get_ABM_effort_py()
get_ABM_effort_py = get_ABM_effort()
end function
integer function Factorial_py(n)
integer, intent(in)  :: n
Factorial_py = Factorial(n)
end function
subroutine set_ABM_tolerance_py(eps)
real, intent(in)  :: eps
call set_ABM_tolerance(eps)
end subroutine
subroutine PC_ABM_py(F,t1,t2,U1,U2,ierr,N_U1,N_U2)
procedure (ODES) :: F
real, intent(in)      :: t1
real, intent(in)      :: t2
real,dimension(N_U1), intent(in)      :: U1
real,dimension(N_U2), intent(out)     :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
call PC_ABM(F,t1,t2,U1,U2,ierr)
end subroutine
subroutine Predictor_AB_py(F,t1,t2,U1,U2,ierr,N_U1,N_U2)
procedure (ODES) :: F
real, intent(in)      :: t1
real, intent(in)      :: t2
real,dimension(N_U1), intent(in)      :: U1
real,dimension(N_U2), intent(out)     :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
call Predictor_AB(F,t1,t2,U1,U2,ierr)
end subroutine
subroutine Corrector_AM_py(F,t1,t2,U1,Up,U2,ierr,N_U1,N_Up,N_U2)
procedure (ODES) :: F
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_Up), intent(in)  :: Up
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_Up
integer, intent(in) :: N_U2
call Corrector_AM(F,t1,t2,U1,Up,U2,ierr)
end subroutine
subroutine set_ABM_IC_py(F,U0,t0,h,N_U0)
procedure(ODES) :: F
real,dimension(N_U0), intent (in)  :: U0
real, intent (in)  :: t0
real, intent (in)  :: h
integer, intent(in) :: N_U0
call set_ABM_IC(F,U0,t0,h)
end subroutine
subroutine Initial_conditions_py(F,U0,t0,h,N_U0)
procedure (ODES) :: F
real,dimension(N_U0), intent(in)  :: U0
real, intent(in)  :: t0
real, intent(in)  :: h
integer, intent(in) :: N_U0
call Initial_conditions(F,U0,t0,h)
end subroutine
end module
module Temporal_Schemes_py
use Temporal_Schemes
implicit none
contains
integer function get_effort_py()
get_effort_py = get_effort()
end function
subroutine Euler_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Euler(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Inverse_Euler_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Inverse_Euler(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Crank_Nicolson_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Crank_Nicolson(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Runge_Kutta2_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Runge_Kutta2(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Runge_Kutta4_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Runge_Kutta4(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Leap_Frog_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Leap_Frog(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Adams_Bashforth2_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Adams_Bashforth2(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Adams_Bashforth3_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Adams_Bashforth3(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine Predictor_Corrector1_py(ODES,t1,t2,U1,U2,ierr,N_U1,N_U2)
real, intent(in)  :: t1
real, intent(in)  :: t2
real,dimension(N_U1), intent(in)  :: U1
real,dimension(N_U2), intent(out)  :: U2
integer, intent(out)  :: ierr
integer, intent(in) :: N_U1
integer, intent(in) :: N_U2
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Predictor_Corrector1(ODES_py,t1,t2,U1,U2,ierr)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
subroutine set_tolerance_py(tolerance)
real, intent(in)  :: tolerance
call set_tolerance(tolerance)
end subroutine
subroutine set_solver_py(family_name,scheme_name)
character(len=*), intent(in)  :: family_name
character(len=*), intent(in), optional  :: scheme_name
call set_solver(family_name,scheme_name)
end subroutine
end module
module Cauchy_Problem_py
use Cauchy_Problem
implicit none
contains
subroutine Cauchy_ProblemS_py(Time_Domain,ODES,Solution,Scheme,N_Time_Domain,N_Solution,N_Solutionu)
real,dimension(N_Time_Domain), intent(in)  :: Time_Domain
real,dimension(N_Solution,N_Solutionu), intent(out)  :: Solution
procedure (Temporal_Scheme), optional  :: Scheme
integer, intent(in) :: N_Time_Domain
integer, intent(in) :: N_Solution
integer, intent(in) :: N_Solutionu
interface
function ODES(i,U,t,N_U)
integer :: i
real,dimension(N_U) :: U
real :: t
integer, intent(in) :: N_U
real :: ODES
end function
end interface
call Cauchy_ProblemS(Time_Domain,ODES_py,Solution,Scheme)
contains
function ODES_py(U,t)
real,dimension(:) :: U
real :: t
real,dimension(size(U)) :: ODES_py
integer::i
do i=1,size(U)
ODES_py(i) = ODES(i,U,t,size(U(:)))
end do
end function
end subroutine
end module