# H.8 Comparing methods
# --------------------------------------------------------------------



# Codercise H.8.1. (a)
dev = qml.device("default.qubit", wires=1)

def exact_result_XandZ(alpha, beta, time):
    """Exact circuit for evolving a qubit with H = alpha Z + beta X.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        
    Returns: 
        array[complex]: The exact state after evolution.
    """
    root = np.sqrt(alpha**2 + beta**2)
    c_0 = np.cos(root*time) - (alpha/root)*np.sin(root*time)*1.j
    c_1 = -(beta/root)*np.sin(root*time)*1.j
    return np.array([c_0, c_1])
    
@qml.qnode(dev)
def trotter_XandZ(alpha, beta, time, n):
    """Trotterized circuit for evolving a qubit with H = alpha Z + beta X.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        n (int): The number of steps in our Trotterization.
        
    Returns: 
        array[complex]: The state after applying the Trotterized circuit.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    t = time
    for i in range(n):
        qml.PauliRot(2*t/n*alpha,"Z" , wires=0)
        qml.PauliRot(2*t/n*beta,"X" , wires=0)
    return qml.state()

def trotter_error_XandZ(alpha, beta, time, n):
    """Difference between the exact and Trotterized result.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        n (int): The number of steps in our Trotterization.
        
    Returns: 
        float: The distance between the exact and Trotterized result.
    """
    diff = np.abs(trotter_XandZ(alpha, beta, time, n) - exact_result_XandZ(alpha, beta, time))
    return np.sqrt(sum(diff*diff))




#Codercise H.8.1. (b)
@qml.qnode(dev)
def trotter_2_XandZ(alpha, beta, time, n):
    """Second-order Trotter circuit for the Hamiltonian H = alpha Z +  beta X.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        n (int): The number of steps in our Trotterization.
        
    Returns: 
        array[complex]: The state after applying the second-order circuit.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    t = time
    for i in range(n):
        qml.PauliRot(2*t/(2*n)*alpha,"Z" , wires=0)
        qml.PauliRot(2*t/(2*n)*beta,"X" , wires=0)
        qml.PauliRot(2*t/(2*n)*beta,"X" , wires=0)
        qml.PauliRot(2*t/(2*n)*alpha,"Z" , wires=0)

    return qml.state()

def trotter_2_error_XandZ(alpha, beta, time, n):
    """Difference between the exact and second-order Trotter result.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        n (int): The number of steps in our Trotterization.
        
    Returns: 
        float: The distance between the exact and second-order result.
    """
    diff = np.abs(trotter_2_XandZ(alpha, beta, time, n) - exact_result_XandZ(alpha, beta, time))
    return np.sqrt(sum(diff*diff))











#Codercise H.8.1. (c)
# try to use recursion to calculate the order-2k trotter circuit
@qml.qnode(dev)
def trotter_k_XandZ(alpha, beta, time, n, k):
    """
    Order-2k Trotter circuit for the Hamiltonian H = alpha Z + beta X.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        n (int): The number of steps in our Trotterization.
        k (int): The order of our Trotterization formula divided by 2.
        
    Returns: 
        array[complex]: The state after applying the order-2k circuit.
    """
    def U(alpha, beta, time, n, k):
        if k == 1:
            qml.RZ(alpha*time/n, wires=[0])
            qml.RX(2*beta*time/n, wires=[0])
            qml.RZ(alpha*time/n, wires=[0])
        else:
            ##################
            # YOUR CODE HERE #
            ##################
            s = 1/(4-4**(1/(2*k-1)))
            U(alpha,beta,s*time,n,k-1)
            U(alpha,beta,s*time,n,k-1)
            U(alpha,beta, (1-4*s)*time,n,k-1)
            U(alpha,beta,s*time,n,k-1)
            U(alpha,beta,s*time,n,k-1)
           
    for _ in range(n):
        U(alpha, beta, time, n, k)
    return qml.state()

def trotter_k_error_XandZ(alpha, beta, time, n, k):
    """
    Difference between the exact and order-2k Trotter result.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        n (int): The number of steps in our Trotterization.
        k (int): The order of our Trotterization formula divided by 2.
        
    Returns: 
        float: The distance between the exact and order-2k result.
    """
    diff = np.abs(trotter_k_XandZ(alpha, beta, time, n, k) - exact_result_XandZ(alpha, beta, time))
    return np.sqrt(sum(diff*diff))





# Codercise H.8.1. (d) 
def trotter_steps_XandZ(alpha, beta, time, error, k):
    """
    Computes the number of Trotter steps needed for a given order k and error.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        error (float): The size of the tolerated simulation error.
        k (int): The order of our Trotterization formula divided by 2.
        
    Returns: 
        int: The number of steps needed to achieve a given error.
    """
    n = 1
    ##################
    # YOUR CODE HERE #
    ##################
    while True:
        e =  trotter_k_error_XandZ(alpha, beta, time, n, k)
        if e <= error:
            break
        n+=1
    return n

error = 1e-6
optimal_k = 3 # MODIFY THIS AFTER LOOKING AT THE PLOT 
n = trotter_steps_XandZ(1, 1, 1, error, optimal_k)
depth = qml.specs(trotter_k_XandZ)(1, 1, 1, n, optimal_k)['depth']
print("The Trotter circuit of order", 2*optimal_k, "uses a circuit of depth", depth, "gates to achieve error ε =", error, ".")



#Codercise H.8.2. (a) 
def truncation_XandZ(alpha, beta, time, K_bits):
    """
    Generates unitaries and coefficients for the truncated X and Z evolution.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        K_bits (int): The index of the truncation order, K = 2^K_bits.
        
    Returns: 
        [array[complex], array[array(complex)]]: Coefficients and unitaries.
    """
    root = np.sqrt(alpha**2 + beta**2)
    coeff_list = [0]*2**K_bits
    U_list = [0]*2**K_bits
    V = (alpha*qml.PauliZ(wires=0).compute_matrix() + beta*qml.PauliX(wires=0).compute_matrix())/root

    for k in range(2**(K_bits-1)):
        
        coeff_list[2*k] = ((time*np.sqrt(alpha**2+beta**2))**(2*k))/fact(2*k) # MODIFY THIS
        coeff_list[2*k + 1] = ((time*np.sqrt(alpha**2+beta**2))**(2*k+1))/fact(2*k+1)# MODIFY THIS
        U_list[2*k] = np.eye(2)*(-1)**k # MODIFY THIS
        U_list[2*k + 1] = (-1)**k*(-1j)*V # MODIFY THIS

    return [coeff_list, U_list]



#Codercise H.8.2. (b)
def LCU_XandZ(alpha, beta, time, K_bits):
    """
    LCU circuit for simulating the Hamiltonian H = alpha Z + beta X.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        K_bits (int): The index of the truncation order, K = 2^K_bits.
        
    Returns: 
        array[complex]: The state after applying the LCU circuit.
    """
    aux = range(K_bits) # The auxiliary qubits
    main = range(K_bits, K_bits + 1) # The main system
    dev2 = qml.device("default.qubit", wires=K_bits + 1, shots=None)
    [coeff_list, U_list] = truncation_XandZ(alpha, beta, time, K_bits)
    
    @qml.qnode(dev2)
    def LCU_circuit():
        qml.QubitUnitary(PREPARE_matrix(coeff_list),wires= aux)
        SELECT(U_list)
        qml.adjoint(qml.QubitUnitary)(PREPARE_matrix(coeff_list),wires= aux)

        return qml.state()

    unnormed = LCU_circuit()[:2] # Unnormalized state of main qubit
    normed = unnormed/np.sqrt(sum(np.conjugate(unnormed)*unnormed)) # Normalize!
    
    return normed


#Codercise H.8.2. (c) 
def LCU_error_XandZ(alpha, beta, time, K_bits):
    """
    Difference between the exact and LCU simulation result.
    
    Args:
        alpha (float): The coefficient of Z in the Hamiltonian.
        beta (float): The coefficient of X in the Hamiltonian.
        time (float): The time we evolve the state for.
        K_bits (int): The index of the truncation order, K = 2^K_bits.
        
    Returns: 
        float: The distance between the exact and LCU result.
    """

    diff = np.abs(LCU_XandZ(alpha, beta, time, K_bits) - exact_result_XandZ(alpha, beta, time))
    # MODIFY THIS

    return np.sqrt(sum(diff*diff))



#Codercise H.8.3.
alpha, error = 1, 1e-2 # VARY THIS

print("For α =", alpha, "and error ε =", error, 
      "the optimal Trotter circuit has depth",  trotter_depth(alpha, error),
      "and the optimal LCU circuit depth", LCU_depth(alpha, error), ".")

alpha_trotter, error_trotter = 1, 1e-6 # RECORD PARAMETERS FOR WHICH TROTTER IS BEST
alpha_LCU, error_LCU = 2, 0.01 # RECORD PARAMETERS FOR WHICH LCU IS BEST
