
def householder(state):
    """Create the matrix form of a Householder transformation.
    
    Args:
        state (array[complex]): A list of amplitudes representing a state.

    Returns: 
        array[complex]: The matrix representation of the Householder transformation.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    U = np.identity(len(state)) -2*np.outer(state,state)
    return U




k_bits = 2
n_bits = 2
all_bits = k_bits + n_bits
aux = range(k_bits)
main = range(k_bits, all_bits)
dev = qml.device("default.qubit", wires=all_bits)

def PREPARE(alpha_list):
    """Create the PREPARE oracle as a matrix.
    
    Args:
        alpha_list (array[float]): A list of coefficients.

    Returns: 
        array[complex]: The matrix representation of the PREPARE routine.
    """
    zero_vec = np.array([1] + [0]*(2**k_bits - 1))
    ##################
    # YOUR CODE HERE #
    ##################
    alpha = alpha_list/np.linalg.norm(alpha_list)
    diff = (zero_vec - alpha)/np.linalg.norm(zero_vec - alpha)
    P = householder(diff)
    return P








# H.7.2. b)
def SELECT(U_list):
    """Implement the SELECT oracle for 2^k unitaries."""
    for index in range(2**k_bits):
        ctrl_str = np.binary_repr(index, k_bits) # Create binary representation
        qml.ControlledQubitUnitary(U_list[index], control_wires=aux, 
                                   wires=main, control_values=ctrl_str)

def LCU(alpha_list, U_list):
    """Implement LCU using PREPARE and SELECT oracles for 2^k unitaries.
    
    Args:
        alpha_list (list[float]): A list of coefficients.
        U_list (list[array[complex]]): A list of unitary matrices, stored as 
        complex arrays.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    qml.QubitUnitary(PREPARE(alpha_list), wires=aux)
    SELECT(U_list)
    qml.adjoint(qml.QubitUnitary)(PREPARE(alpha_list), wires=aux)



# H.7.2. c)
# all target gate are |1>:

U_list = [np.kron(qml.PauliX.compute_matrix(), qml.PauliX.compute_matrix()),
          np.kron(qml.PauliZ.compute_matrix(), qml.PauliZ.compute_matrix()),
          np.kron(qml.PauliX.compute_matrix(), qml.PauliZ.compute_matrix()),
          np.kron(qml.PauliZ.compute_matrix(), qml.PauliX.compute_matrix())]
alpha_list = [1, 0.5, 0.5, 1]

@qml.qnode(dev)
def my_circuit():
    """Apply H(X + Z/2) to the state |11> using LCU."""
    ##################
    # YOUR CODE HERE #
    ##################
    for i in main:
        qml.PauliX(wires=i)
    LCU(alpha_list, U_list)
    return qml.state()

print("The amplitudes on the main register are proportional to", my_circuit()[:4], ".")



#H.7.3

@qml.qnode(dev)
def quantum_memory(beta_list):
    """Produce a data state with positive coefficients beta_list.

    Args:
        beta_list (array[float]): The amplitudes for our superposition.

    Returns: 
        array[float]: The state on both address and data registers.
    """
    U_list =[np.kron(qml.PauliZ.compute_matrix(), qml.PauliZ.compute_matrix()),
          np.kron(qml.PauliZ.compute_matrix(), qml.PauliX.compute_matrix()),
          np.kron(qml.PauliX.compute_matrix(), qml.PauliZ.compute_matrix()),
          np.kron(qml.PauliX.compute_matrix(), qml.PauliX.compute_matrix())]
    ##################
    # YOUR CODE HERE #
    ##################
    # why cannot use beta_list**2 here????????????????
    qml.QubitUnitary(PREPARE(np.square(beta_list)), wires= aux)
    SELECT(U_list)
    
    return qml.state()

beta_list = [1, 0, 0, 1]
normalized_coefficients = [quantum_memory(beta_list)[i].item() for i in range(0, 20, 5)]
print("The amplitudes on the main register are proportional to", normalized_coefficients, ".")


