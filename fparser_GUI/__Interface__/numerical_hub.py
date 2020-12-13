import numerical_hubf
class Fourier_interpolation:
    def FFT2(N,U):
        """
            !*************************************************************************
            ! Cooley-Tukey FFT
            !            Fast Fourier Transform
            !
            !    Inputs:
            !              - N        : number of collocation points(must be N=2^r)
            !              - U(0:N-1) : collocation points 
            !                           u_0, u_1,.. u_N-1
            !
            !    Outputs:
            !              - U(0:N-1) : discrete fourier coefficients 
            !                           N *(c_0, c_1, ... c_N/2, c_N/2-1, ..., c_-1)
            !
            !
            !  Author: Juan A. Hernandez, Feb, 2018    
            !*************************************************************************
            N (integer): None
            U (complex): None
        """
        numerical_hubf.Fourier_interpolation_py.FFT2_py(N,U)
class Jacobian_module:
    def Jacobian(FunctionRN_RN,xp):
        """
            !**********************************************************************
            !*  Jacobian of a vector of functions F ( x in ) 
            !*
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !**********************************************************************
            FunctionRN_RN (Function): None
            xp (real): None
        """
        def FunctionRN_RN_py(i,x):
            global global_FunctionRN_RN_var
            if i == 1:
                global_FunctionRN_RN_var = FunctionRN_RN(x)
            return global_FunctionRN_RN_var[i]
        return numerical_hubf.Jacobian_module_py.Jacobian_py(FunctionRN_RN_py,xp)
    def Jacobianc(FunctionRN_RNE,xp):
        """
            !**********************************************************************
            !*  Jacobian of a vector of functions F ( x inout )  
            !*
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !**********************************************************************
            FunctionRN_RNE (Function): None
            xp (real): None
        """
        def FunctionRN_RNE_py(i,x):
            global global_FunctionRN_RNE_var
            if i == 1:
                global_FunctionRN_RNE_var = FunctionRN_RNE(x)
            return global_FunctionRN_RNE_var[i]
        return numerical_hubf.Jacobian_module_py.Jacobianc_py(FunctionRN_RNE_py,xp)
class Lagrange_interpolation:
    def Lagrange_polynomials(x,xp):
        """
            !*******************************************************************************************************************************************
            !                                           Lagrange polynomials
            !
            !  Recurrence relation  to obtain derivatives and integral values of the Lagrange polynomials at xp from a set of nodes x(0:N)
            !  
            !
            !      lagrange_j{N+1} (x) = (x-x0)(x-x1)(x-2)........(x-xn) / (xj- x0)(xj-x1)(xj-x2).......(xj-xn), j=0...N
            !      lagrange_j{N+1} (x) = (x -xn)/(xj-xn) lagrange_j{N} (x) 
            !
            !      d^k lagrange_j{r+1} (x) /dx^k  = ( d^k lagrange_j{r} (x) /dx^k (x-xr) + k d^(k-1) lagrange_j{r} (x) /dx^(k-1) ) / (xj -xr ), r=0...N  
            !
            !      integral( lagrange_j{N+1}(x), from x0 to xp ) = integral ( l(xp) + dl/dx(xp) ( x -xp) +....... d^N l/dx^N(xp) * (x- xp)**N / N! ) 
            !                                                    = sum_k (  -  dl^k/dx^k (xp) ( xj - xp )**(k+1) /(k+1)! )  
            ! 
            !      k = -1 means integral value of lagrange_j{N+1} (x) from xj to xp (xj  nearest node from xp)
            !      k =  0 means value of lagrange_j{N+1} (x) at xp 
            !      k > 1    means derivative value of lagrange_j{N+1} (x) at xp 
            !
            ! It returns Lagrange_polynomials(k,j) 
            !
            !     k: meaning given above 
            !     j: corresponding wth L_j(x) (this polynomial equals to one in x_j and vanishes at the rest of nodes) 
            !
            ! Author : Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !*****************************************************************************************************************************************
            x (real): None
            xp (real): None
        """
        return numerical_hubf.Lagrange_interpolation_py.Lagrange_polynomials_py(x,xp)
    def Stencilv(Order,N):
        """
            !******************************************************************************
            !* Vector of Stencils of each interpolant 
            !
            !    0,0,...,0,0,1,2,3,4,5,6,..... N-Order, N-Order, ..N - Order 
            !
            !******************************************************************************
            Order (integer): None
            N (integer): None
        """
        return numerical_hubf.Lagrange_interpolation_py.Stencilv_py(Order,N)
    def Lagrange_error_polynomial(x,xp):
        """
            !***************************************************************************************************************************************
            !                                           Lagrange error polynomials
            !
            !  Recurrence relation  to obtain derivatives and integral values of the Lagrange error polynomials at xp from a set of nodes x(0:N)
            !  
            !
            !      pi{N+1} (x) = (x-x0)(x-x1)(x-2)........(x-xn) 
            !      pi{N+1} (x) = (x -xn) pi{N} (x) 
            !
            !      d^k pi{r+1} (x) /dx^k  = ( d^k pi{r} (x) /dx^k (x-xr) + k d^(k-1) pi{r} (x) /dx^(k-1) ), r=0...N  
            !
            !      k =  0 means value of pi{N+1} (x) at xp 
            !      k > 1    means derivative value of pi{N+1} (x) at xp 
            !
            !*****************************************************************************************************************************************
            x (real): None
            xp (real): None
        """
        return numerical_hubf.Lagrange_interpolation_py.Lagrange_error_polynomial_py(x,xp)
    def Lebesgue_functions(x,xp):
        """
            !*******************************************************************************************************************************************
            !                                           Lebesgue function 
            !
            !      Definition: Lebesgue_function =  |Lagrange_0(x)| + |Lagrange_1(x)| + ....  + |Lagrange_N(x)|
            !  
            !      Inputs: 
            !               x(0:N) nodes 
            !               xp(0:M) points where the Lebesgue function is evaluated 
            !
            !       Outputs: 
            !               Lebesgue_functions(k,i)
            !                    k = -1 means integral value of lagrange_j{N+1} (x) from xj to xp (xj  nearest node from xp)
            !                    k =  0 means value of lagrange_j{N+1} (x) at xp 
            !                    k > 1    means derivative value of lagrange_j{N+1} (x) at xp 
            !
            !                    i: index of the xp point where lebesgue function is evaluated 
            !
            ! Author : Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !*****************************************************************************************************************************************
            x (real): None
            xp (real): None
        """
        return numerical_hubf.Lagrange_interpolation_py.Lebesgue_functions_py(x,xp)
    def PI_error_polynomial(x,xp):
        """
            !*******************************************************************************************************************************************
            !                                           PI error polynomial 
            !
            !      Definition: pi(x) =  |(x-x0)| |(x-x1)| ..... |(x-xN)|
            !  
            !      Inputs: 
            !               x(0:N) nodes 
            !               xp(0:M) points where the pi error polynomial function is evaluated 
            !
            !       Outputs: 
            !               PI_error_polynomial(k,i)
            !                    k = -1 means integral value of lagrange_j{N+1} (x) from xj to xp (xj  nearest node from xp)
            !                    k =  0 means value of lagrange_j{N+1} (x) at xp 
            !                    k > 1    means derivative value of lagrange_j{N+1} (x) at xp 
            !
            !                    i: index of the xp point where error polynomial is evaluated 
            !
            ! Author : Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !*****************************************************************************************************************************************
            x (real): None
            xp (real): None
        """
        return numerical_hubf.Lagrange_interpolation_py.PI_error_polynomial_py(x,xp)
class Linear_systems:
    def Solve_LU(A,b):
        """
            !***************************************************************************
            !* LU x = b 
            !***************************************************************************
            A (real): None
            b (real): None
        """
        return numerical_hubf.Linear_systems_py.Solve_LU_py(A,b)
    def Gauss(A,b):
        """
            !***************************************************************************
            !* Classical Gaussian elimination 
            !***************************************************************************
            A (real): None
            b (real): None
        """
        return numerical_hubf.Linear_systems_py.Gauss_py(A,b)
    def Condition_number(A):
        """
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
            A (real): None
        """
        return numerical_hubf.Linear_systems_py.Condition_number_py(A)
    def Solve_LU_band(A,b,rj):
        """
            !************************************************************************
            !* Band width = 2 * rj  + 1 
            !************************************************************************
            A (real): None
            b (real): None
            rj (integer): None
        """
        return numerical_hubf.Linear_systems_py.Solve_LU_band_py(A,b,rj)
    def Tensor_product(u,v):
        """
            !************************************************************************
            !* Tensor product A_ij = u_i v_j 
            !************************************************************************
            u (real): None
            v (real): None
        """
        return numerical_hubf.Linear_systems_py.Tensor_product_py(u,v)
    def LU_factorization(A):
        """
            !***************************************************************************
            !*   Factorization of A by means of upper and lower triangle matrices 
            !*          input  : A matrix 
            !*          output : A  holds L U 
            !*
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !***************************************************************************
            A (real): None
        """
        numerical_hubf.Linear_systems_py.LU_factorization_py(A)
    def Swap(A,B):
        """
            !***************************************************************************
            !* Swap two vectors 
            !***************************************************************************
            A (real): None
            B (real): None
        """
        numerical_hubf.Linear_systems_py.Swap_py(A,B)
    def Power_method(A,lambda,U):
        """
            !****************************************************************
            !* Power method  to obtain the largest eigenvalue of a square matrix A 
            !*          input  : A matrix 
            !*
            !*          output : lambda eigenvalue 
            !*                   U eigenvector 
            !*
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !****************************************************************
            A (real): None
            lambda (real): None
            U (real): None
        """
        numerical_hubf.Linear_systems_py.Power_method_py(A,lambda,U)
    def Inverse_power_method(A,lambda,U):
        """
            !****************************************************************
            ! Inverse Power method to obtain the smallest eigenvalue of a square matrix A 
            !*          input  : A matrix 
            !*
            !*          output : lambda eigenvalue 
            !*                   U eigenvector 
            !*
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !****************************************************************
            A (real): None
            lambda (real): None
            U (real): None
        """
        numerical_hubf.Linear_systems_py.Inverse_power_method_py(A,lambda,U)
    def Eigenvalues_PM(A,lambda,U):
        """
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
            A (real): None
            lambda (real): None
            U (real): None
        """
        numerical_hubf.Linear_systems_py.Eigenvalues_PM_py(A,lambda,U)
    def SVD(A,sigma,U,V):
        """
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
            A (real): None
            sigma (real): None
            U (real): None
            V (real): None
        """
        numerical_hubf.Linear_systems_py.SVD_py(A,sigma,U,V)
    def LU_band_factorization(A,rj):
        """
            !************************************************************************
            !* Band width = 2 * rj  + 1 
            !************************************************************************
            A (real): None
            rj (integer): None
        """
        numerical_hubf.Linear_systems_py.LU_band_factorization_py(A,rj)
class ODE_Interface:
class Temporal_scheme_interface:
class Chebyshev_interpolation:
    def DCT2(N,U):
        """
            !***************************************************************
            ! Discrete cosine Fourier Transform 
            !***************************************************************
            N (integer): None
            U (complex): None
        """
        numerical_hubf.Chebyshev_interpolation_py.DCT2_py(N,U)
    def Chebyshev_Derivative(C,C1):
        """
            !***************************************************************
            ! Derivative of Chebyshev expansion 
            !***************************************************************
            C (complex): None
            C1 (complex): None
        """
        numerical_hubf.Chebyshev_interpolation_py.Chebyshev_Derivative_py(C,C1)
class Embedded_RKs:
    def get_eRK_effort():
        """
        """
        return numerical_hubf.Embedded_RKs_py.get_eRK_effort_py()
    def Step_size(dU,tolerance,q,h):
        """
            ! ******************************************************************
            ! It calculates the new step size as a function of estimated error 
            !
            !  dU(Error) = k h**(q+1) 
            !  Tolerance = k Step_size **(q+1)  
            !  INPUTS: 
            !          dU(:)     : Estimated error 
            !          Tolerance : max permitted error 
            !          q         : order of the error 
            ! OUTPUTS: 
            !           Step_size : new temporal step 
            !******************************************************************
            dU (real): None
            tolerance (real): None
            q (integer): None
            h (real): None
        """
        return numerical_hubf.Embedded_RKs_py.Step_size_py(dU,tolerance,q,h)
    def set_eRK_name(name):
        """
            name (character(len=*)): None
        """
        numerical_hubf.Embedded_RKs_py.set_eRK_name_py(name)
    def set_eRK_tolerance(eps):
        """
            eps (real): None
        """
        numerical_hubf.Embedded_RKs_py.set_eRK_tolerance_py(eps)
    def ERK_scheme(F,t1,t2,U1,U2,ierr):
        """
            !**************************************************************************
            ! It calculates one time step of a system of ODES by means of 
            ! Embedded Runge Kutta with variable step selection. 
            ! To detemine the time step, the estimated error is calculated based on two RKs.
            ! One with order q and one with order q-1.
            ! The method and the tolerance can be previously selected
            !
            ! Inputs: 
            !         F      : system of equations 
            !         t1, t2 : time step to integrate 
            !         U1     : initial conditions 
            !
            ! Outputs: 
            !         U1     : solution at time t2 with error less than tolerance 
            !
            ! Authors: 
            !         Francisco Javier Escoto Lopez (2018)
            !         Juan A. Hernandez Ramos       (2019)
            !***************************************************************************  
            F (procedure (ODES)): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        numerical_hubf.Embedded_RKs_py.ERK_scheme_py(F,t1,t2,U1,U2,ierr)
    def RK_scheme(name,tag,F,t1,t2,U1,U2):
        """
            !*******************************************************************************
            !  Runke-Kutta formulas for explicit schemes based on Butcher array 
            !  First RK scheme creates Butcher's array and calculates k_i values
            !  Second RK scheme uses k_i previously calculated
            !*******************************************************************************  
            name (character(len=*)): None
            tag (character(len=*)): None
            F (procedure (ODES)): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
        """
        numerical_hubf.Embedded_RKs_py.RK_scheme_py(name,tag,F,t1,t2,U1,U2)
    def Butcher_array(name,Ne):
        """
            ! ******************************************************************
            ! Butcher array for different Runge-Kutta names
            !******************************************************************
            name (character(len=*)): None
            Ne (integer): None
        """
        numerical_hubf.Embedded_RKs_py.Butcher_array_py(name,Ne)
class Wrappers:
    def get_weRK_effort():
        """
        """
        return numerical_hubf.Wrappers_py.get_weRK_effort_py()
    def get_wGBS_effort():
        """
        """
        return numerical_hubf.Wrappers_py.get_wGBS_effort_py()
    def get_wABM_effort():
        """
        """
        return numerical_hubf.Wrappers_py.get_wABM_effort_py()
    def set_weRK_name(name):
        """
            !*********************************************************
            ! Runge Kutta wrapper selection, tolerance and time steps 
            !*********************************************************    
            name (character(len=*)): None
        """
        numerical_hubf.Wrappers_py.set_weRK_name_py(name)
    def set_weRK_tolerance(eps):
        """
            eps (real): None
        """
        numerical_hubf.Wrappers_py.set_weRK_tolerance_py(eps)
    def set_wGBS_tolerance(eps):
        """
            !*********************************************
            ! GBS wrapper tolerance and time steps 
            !********************************************* 
            eps (real): None
        """
        numerical_hubf.Wrappers_py.set_wGBS_tolerance_py(eps)
    def set_wABM_tolerance(eps):
        """
            !********************************************
            ! ABM wrapper tolerance and time steps 
            !****************************************** 
            eps (real): None
        """
        numerical_hubf.Wrappers_py.set_wABM_tolerance_py(eps)
    def WERK(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Wrapper of dopri5
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): !intent out changed for test
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Wrappers_py.WERK_py(ODES_py,t1,t2,U1,U2,ierr)
    def WODEX(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Wrapper of ODEX
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Wrappers_py.WODEX_py(ODES_py,t1,t2,U1,U2,ierr)
    def WODE113(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Wrapper of ODE113
            !*******************************************************************************
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Wrappers_py.WODE113_py(ODES_py,t1,t2,U1,U2,ierr)
class Gragg_Burlisch_Stoer:
    def get_GBS_effort():
        """
        """
        return numerical_hubf.Gragg_Burlisch_Stoer_py.get_GBS_effort_py()
    def set_GBS_tolerance(eps):
        """
            eps (real): None
        """
        numerical_hubf.Gragg_Burlisch_Stoer_py.set_GBS_tolerance_py(eps)
    def Modified_midpoint_scheme(F,t0,t,U0,Un,n):
        """
            !*******************************************************************************
            !    Modified Midpoint scheme
            !    given an interval [t0,t] divided in 2n = number of steps in the interval 
            !    and an initial value U(t0),
            !    Gives back the value U(t) = Un
            !
            !    Francisco Javier Escoto Lopez
            !*******************************************************************************  
            F (procedure (ODES)): None
            t0 (real): None
            t (real): None
            U0 (real): None
            Un (real): None
            n (integer): None
        """
        numerical_hubf.Gragg_Burlisch_Stoer_py.Modified_midpoint_scheme_py(F,t0,t,U0,Un,n)
    def GBS_Richardson_coefficients(n,b):
        """
            !*******************************************************************************
            !    Richardson coefficients to compute Richardson's extrapolation given
            !    a sequence of levels
            !    Francisco Javier Escoto Lopez
            !*******************************************************************************    
            n (integer): None
            b (real): None
        """
        numerical_hubf.Gragg_Burlisch_Stoer_py.GBS_Richardson_coefficients_py(n,b)
    def GBS_Scheme(F,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            !    Gragg-Bulirsch-Stoer (GBS) scheme
            !    Francisco Javier Escoto Lopez
            !    javier.escoto.lopez@gmail.com (2019) 
            !    juanantonio.hernandez@upm.es  (2020)
            !******************************************************************************* 
            F (procedure (ODES)): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        numerical_hubf.Gragg_Burlisch_Stoer_py.GBS_Scheme_py(F,t1,t2,U1,U2,ierr)
class Non_Linear_Systems:
    def Newton(FunctionRN_RN,x0):
        """
            !***************************************************************************
            !*  Newton solver 
            !*                x0   : initial guess and output value 
            !*                F(X) : vector function 
            !*
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !***************************************************************************
            FunctionRN_RN (Function): None
            x0 (real): None
        """
        def FunctionRN_RN_py(i,x):
            global global_FunctionRN_RN_var
            if i == 1:
                global_FunctionRN_RN_var = FunctionRN_RN(x)
            return global_FunctionRN_RN_var[i]
        numerical_hubf.Non_Linear_Systems_py.Newton_py(FunctionRN_RN_py,x0)
    def Newtonc(FunctionRN_RNE,x0):
        """
            !***************************************************************************
            !*  This version allows to solve: (see examples test_Newtonc)
            !*           x(1) = x(2) 
            !*           F(1) = 0
            !*           F(2) = x(1) + x(2) - 1 
            !*       
            !*
            !*  Newton solver 
            !*                x0   : initial guess and output value 
            !*                F(X) : vector function 
            !*
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !***************************************************************************
            FunctionRN_RNE (Function): None
            x0 (real): None
        """
        def FunctionRN_RNE_py(i,x):
            global global_FunctionRN_RNE_var
            if i == 1:
                global_FunctionRN_RNE_var = FunctionRN_RNE(x)
            return global_FunctionRN_RNE_var[i]
        numerical_hubf.Non_Linear_Systems_py.Newtonc_py(FunctionRN_RNE_py,x0)
class Adams_Bashforth_Moulton:
    def get_ABM_effort():
        """
        """
        return numerical_hubf.Adams_Bashforth_Moulton_py.get_ABM_effort_py()
    def Factorial(n):
        """
            n (integer): None
        """
        return numerical_hubf.Adams_Bashforth_Moulton_py.Factorial_py(n)
    def set_ABM_tolerance(eps):
        """
            !******************************************************************
            !*  TODO: error tolerance allow to determine Steps and h (time step) 
            !******************************************************************  
            eps (real): None
        """
        numerical_hubf.Adams_Bashforth_Moulton_py.set_ABM_tolerance_py(eps)
    def PC_ABM(F,t1,t2,U1,U2,ierr):
        """
            !******************************************************************
            !*  Predictor Corrector based on Adams-Bashforth and Adams-Moulton  
            !******************************************************************
            F (procedure (ODES)): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        numerical_hubf.Adams_Bashforth_Moulton_py.PC_ABM_py(F,t1,t2,U1,U2,ierr)
    def Predictor_AB(F,t1,t2,U1,U2,ierr):
        """
            !********************************************************
            !* Predictor Adams Bashforth 
            !********************************************************
            F (procedure (ODES)): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        numerical_hubf.Adams_Bashforth_Moulton_py.Predictor_AB_py(F,t1,t2,U1,U2,ierr)
    def Corrector_AM(F,t1,t2,U1,Up,U2,ierr):
        """
            !********************************************************
            !* Corrector Adams Moulton 
            !********************************************************
            F (procedure (ODES)): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            Up (real): None
            U2 (real): None
            ierr (integer): None
        """
        numerical_hubf.Adams_Bashforth_Moulton_py.Corrector_AM_py(F,t1,t2,U1,Up,U2,ierr)
    def set_ABM_IC(F,U0,t0,h):
        """
            !*******************************************************************************
            !    Computes the mabtix B and coefficients r_i for a multivalue method
            !    Author:  
            !       Francisco Javier Escoto Lopez 2019 
            !       Juan A Hernandez Ramos        2019 
            !******************************************************************************* 
            F (procedure(ODES)): None
            U0 (real): None
            t0 (real): None
            h (real): None
        """
        numerical_hubf.Adams_Bashforth_Moulton_py.set_ABM_IC_py(F,U0,t0,h)
    def Initial_conditions(F,U0,t0,h):
        """
            !*******************************************************************************
            !    Computes the initial conditions for Y1 which are derivatives 
            !******************************************************************************* 
            F (procedure (ODES)): None
            U0 (real): None
            t0 (real): None
            h (real): None
        """
        numerical_hubf.Adams_Bashforth_Moulton_py.Initial_conditions_py(F,U0,t0,h)
class Interpolation:
    def Integral(x,y,degree):
        """
            !************************************************************************************************************
            !* Computes the piecewise polynomial integration of y(x) from the data x(:) and y(:).
            !*  The optional value "degree" is the degree of the polynomial used, if it is not present it takes the value 2.
            !**************************************************************************************************************
            x (real): None
            y (real): None
            degree (integer): None
        """
        return numerical_hubf.Interpolation_py.Integral_py(x,y,degree)
    def Interpolant(x,y,degree,xp):
        """
            !*************************************************************************************************************
            !* Computes the piecewise polynomial interpolation of I(xp) from the data x(:) and y(:). 
            !  The optional value "degree" is the degree of the polynomial used, if it is not present it takes the value 2.
            !*************************************************************************************************************
            x (real): None
            y (real): None
            degree (integer): None
            xp (real): None
        """
        return numerical_hubf.Interpolation_py.Interpolant_py(x,y,degree,xp)
class Temporal_Schemes:
    def get_effort():
        """
        """
        return numerical_hubf.Temporal_Schemes_py.get_effort_py()
    def Euler(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Explicit Euler  
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Euler_py(ODES_py,t1,t2,U1,U2,ierr)
    def Inverse_Euler(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Implicit Inverse Euler    
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Inverse_Euler_py(ODES_py,t1,t2,U1,U2,ierr)
    def Crank_Nicolson(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Crank Nicolson scheme    
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Crank_Nicolson_py(ODES_py,t1,t2,U1,U2,ierr)
    def Runge_Kutta2(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Runge Kutta 2 stages 
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Runge_Kutta2_py(ODES_py,t1,t2,U1,U2,ierr)
    def Runge_Kutta4(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Runge Kutta 4 stages 
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Runge_Kutta4_py(ODES_py,t1,t2,U1,U2,ierr)
    def Leap_Frog(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            !   Leap Frog 
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Leap_Frog_py(ODES_py,t1,t2,U1,U2,ierr)
    def Adams_Bashforth2(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Second order Adams Bashforth    
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Adams_Bashforth2_py(ODES_py,t1,t2,U1,U2,ierr)
    def Adams_Bashforth3(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Third order Adams-Bashforth    
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Adams_Bashforth3_py(ODES_py,t1,t2,U1,U2,ierr)
    def Predictor_Corrector1(ODES,t1,t2,U1,U2,ierr):
        """
            !*******************************************************************************
            ! Predictor- corrector with variable time step 
            !*******************************************************************************  
            ODES (Function): None
            t1 (real): None
            t2 (real): None
            U1 (real): None
            U2 (real): None
            ierr (integer): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Temporal_Schemes_py.Predictor_Corrector1_py(ODES_py,t1,t2,U1,U2,ierr)
    def set_tolerance(tolerance):
        """
            tolerance (real): None
        """
        numerical_hubf.Temporal_Schemes_py.set_tolerance_py(tolerance)
    def set_solver(family_name,scheme_name):
        """
            family_name (character(len=*)): None
            scheme_name (character(len=*)): None
        """
        numerical_hubf.Temporal_Schemes_py.set_solver_py(family_name,scheme_name)
class Cauchy_Problem:
    def Cauchy_ProblemS(Time_Domain,ODES,Solution,Scheme):
        """
            !************************************************************************************************
            ! It integrates the following Cauchy problem 
            !
            !       dU/dt = F(U, t),      U(0) = U^0 (CI)   
            !
            !     Inputs: 
            !            Time_Domain(:)        : time discretization 
            !            Differential_operator : vector values function F(U, t)
            !            Scheme                : Optional Temporal numerical scheme ( default: Runge_Kutta4)
            !            Solution(0,:)         : Initial condition 
            !
            !     Outputs: 
            !            Solution(:,:)         : first index represents time 
            !                                    second index  represents the i-component of solution
            !     
            !*  Author: Juan A Hernandez (juanantonio.hernandez@upm.es) 
            !***************************************************************************************************
            Time_Domain (real): None
            ODES (Function): None
            Solution (real): None
            Scheme (procedure (Temporal_Scheme)): None
        """
        def ODES_py(i,U,t):
            global global_ODES_var
            if i == 1:
                global_ODES_var = ODES(U,t)
            return global_ODES_var[i]
        numerical_hubf.Cauchy_Problem_py.Cauchy_ProblemS_py(Time_Domain,ODES_py,Solution,Scheme)