# H.9 Qubitization

# Codercise H.9.1. (a)

k_bits = 2 # number of bits in the O register
main_bits = 2 # number of bits in the main register
all_bits = k_bits + main_bits # total number of bits

# define wire ranges for each of the three registers
k_wires = range(k_bits) # O register
main_wires = range(k_bits, all_bits) # main register
dev = qml.device("default.qubit", wires=all_bits)  

def walk(alpha_list, U_list):
    """Create a subcircuit for the walk operator in qubitization.
    
    Args:
        alpha_list (array[float]): A list of coefficients.
        U_list (list[array[complex]]): A list of unitary matrices, stored as complex arrays.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    SELECT(U_list)
    prep = PREPARE_matrix(alpha_list)
    R = np.zeros(prep.shape)
    for i in range(len(R)):
        if i ==0:
            R[i][i]=1
            continue
        R[i][i] =-1
    '''
        if i ==0:
            R[i][i]=1
        else:
            R[i][i] =-1
    '''
        
    R_hat = np.conj(prep).T.dot(R).dot(prep)
    qml.QubitUnitary(R_hat,wires=k_wires)
    

# (b) 
@qml.qnode(dev)
def walk_circuit(alpha_list, U_list, steps):
    """Create a subcircuit for the walk operator in qubitization.
    
    Args:
        alpha_list (array[float]): A list of coefficients.
        U_list (list[array[complex]]): A list of unitary matrices, stored as complex arrays.
        steps (int): The number of times to iterate the walk operator.

    Returns:
        array[complex]: The quantum state after applying the circuit.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    P = PREPARE_matrix(alpha_list)
    qml.QubitUnitary(P,wires=k_wires)
    for i in range(steps):
        walk(alpha_list, U_list)
    return qml.state()




# Codercise H.9.2. (a) 
targ_bits = k_bits + main_bits
targ_wires = range(targ_bits)
k_wires = range(k_bits)

def eigenstate_prep(alpha_list, U_list, E):
    """Create a subcircuit which prepares the + eigenstate of the walk operator.
    
    Args:
        alpha_list (array[float]): A list of coefficients.
        U_list (list[array[complex]]): A list of unitary matrices.
        E (float): Our guess at the energy of the state.
    """
    alpha = sum(alpha_list)

    ##################
    # YOUR CODE HERE #
    ##################

    # DEFINE c_+/- 
    c_plus = np.sqrt(2*(1+E/alpha))**(-1)
    c_minus = np.sqrt(2*(1-E/alpha))**(-1)
    c = [c_plus, c_minus] 

    qml.QubitUnitary(PREPARE_matrix(alpha_list),wires=k_wires)
    mat = SELECT_matrix(U_list)
    mat = 1/np.sqrt(2)*( (c[0]+ 1j*c[1])*np.identity(2**targ_bits)
    +(c[0] - 1j * c[1])*mat )
    qml.QubitUnitary(mat,wires=targ_wires)


#b)
p_bits = 8 # number of bits in the T register
# range of wires in the T register (where phase estimation occurs)
p_wires = range(targ_bits, targ_bits + p_bits) 

dev2 = qml.device("default.qubit", wires=targ_bits + p_bits)

@qml.qnode(dev2)
def qpe_circuit(alpha_list, U_list, state, E):
    """Create a circuit for estimating the phase of a basis state of the walk operator.
    
    Args:
        alpha_list (array[float]): A list of coefficients.
        U_list (list[array[complex]]): A list of unitary matrices.
        state (list[int]): A basis state, specified as a list of bits.
        E (float): Our guess at the energy of the state.

    Returns:
        array[float]: The probabilities on the estimate register.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # INITIALIZE BASIS STATE
    # PREPARE EIGENSTATE OF WALK OPERATOR
    eigenstate_prep(alpha_list, U_list, E)
    # APPLY QUANTUM PHASE ESTIMATION
    qml.QuantumPhaseEstimation(walk_matrix(alpha_list,U_list), targ_wires ,p_wires)
    return qml.probs(wires=p_wires)

#c).
U_list = [np.kron(qml.Hadamard.compute_matrix(), qml.Hadamard.compute_matrix()), 
          np.kron(-qml.Hadamard.compute_matrix(), qml.PauliX.compute_matrix()),
          np.kron(-qml.PauliX.compute_matrix(), qml.Hadamard.compute_matrix()),
          np.kron(qml.PauliX.compute_matrix(), qml.PauliX.compute_matrix())] # MODIFY THIS
alpha_list = [2.0,np.sqrt(2), np.sqrt(2),1.0] # MODIFY THIS

phase_estimated_00 = qpe_circuit(alpha_list, U_list, [0, 0], 1.0) # MODIFY THIS
phase_estimated_01 = qpe_circuit(alpha_list, U_list, [0, 1], -1.0) # MODIFY THIS
# tips: read the documentation for qml.QuantumPhaseEstimation
# phase_estimated = np.argmax(circuit()) / 2 ** n_estimation_wires
phase_estimated_00 = phase_estimated = np.argmax(phase_estimated_00) / 2 ** p_bits
phase_estimated_01 = phase_estimated = np.argmax(phase_estimated_01) / 2 ** p_bits

alpha = sum(alpha_list)

energy_estimated_00 = alpha*np.cos(2*np.pi*phase_estimated_00)
energy_estimated_01 = alpha*np.cos(2*np.pi*phase_estimated_01)

print("The estimated energy for state |00> is", energy_estimated_00, ".")
print("The estimated energy for state |01> is", energy_estimated_01, ".")





#Codercise H.9.3. (a) 
def S(time, alpha):
    """Implement the unitary S as a matrix.
    
    Args:
        time (float): The time to evolve the Hamiltonian for.
        alpha (float): The sum of alpha coefficients in the Hamiltonian.

    Returns:
        array[complex]: The matrix representation of S.
    """
    hbar = 1e-34
    output = np.eye(2**(targ_bits + p_bits), dtype = 'complex_')
    for k in range(2**targ_bits):
        for i in range(2**p_bits):
            index = 2**p_bits*k + i

            ##################
            # YOUR CODE HERE #
            ##################
            val = - time * alpha / hbar * np.cos(2 * np.pi * 1/(2**p_bits) * index)
            output[index, index] = np.exp(1j * val) # MODIFY THIS

    return output

#b)
@qml.qnode(dev2)
def qubitization(alpha_list, U_list, time):
    """Perform Hamiltonian simulation using a simplified qubitization circuit.
    
    Args:
        alpha_list (array[float]): A list of coefficients.
        U_list (list[array[complex]]): A list of unitary matrices, stored as complex arrays.
        time (float): The time to evolve the Hamiltonian for.
    """
    prep = PREPARE_matrix(alpha_list)
    prep_dagger = np.conjugate(np.transpose(prep))
    alpha = sum(alpha_list)
    
    ##################
    # YOUR CODE HERE #
    ##################
    qml.QubitUnitary(prep,wires = [i for i in range(k_bits)])
    qml.QuantumPhaseEstimation(walk_matrix(alpha_list,U_list),targ_wires, p_wires)
    qml.QubitUnitary(S(time, alpha), wires = [i for i in range(10)])
    qml.adjoint(qml.QuantumPhaseEstimation)(walk_matrix(alpha_list,U_list),targ_wires,p_wires)
    qml.QubitUnitary(prep_dagger, wires = [i for i in range(k_bits)])
    
    return qml.probs(wires=range(k_bits, k_bits + main_bits))


















