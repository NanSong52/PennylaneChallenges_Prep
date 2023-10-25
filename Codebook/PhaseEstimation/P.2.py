# P.2 It's not just a phase


def U_power_2k(unitary, k):
    """ Computes U at a power of 2k (U^2^k)
    
    Args: 
        unitary (array[complex]): A unitary matrix
    
    Returns: 
        array[complex]: the unitary raised to the power of 2^k
    """
    ##################
    # YOUR CODE HERE #
    ##################  
    return np.linalg.matrix_power(unitary, 2**k)


# Try out a higher power of U
U = qml.T.compute_matrix()
print(U)

U_power_2k(U, 2)
    
   
estimation_wires = [0, 1, 2]
target_wires = [3]

def apply_controlled_powers_of_U(unitary):
    """A quantum function that applies the sequence of powers of U^2^k to
    the estimation wires.
    
    Args: 
        unitary (array [complex]): A unitary matrix
    """

    ##################
    # YOUR CODE HERE #
    ##################  
    u = [U_power_2k(unitary, i) for i in range(len(estimation_wires))]
    u =list(reversed(u)) # reverse: list => tuple
    for i in range(len(estimation_wires)):
        qml.ControlledQubitUnitary(u[i],\
        control_wires = estimation_wires[i],wires=target_wires)


dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)

@qml.qnode(dev)
def qpe(unitary):
    """ Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Measurement outcome probabilities on the estimation wires.
    """
    ##################
    # YOUR CODE HERE #
    ################## 
    prepare_eigenvector()
    for i in range(len(estimation_wires)):
        qml.Hadamard(wires= i)
    apply_controlled_powers_of_U(unitary)
    qml.adjoint(qml.QFT(wires= estimation_wires))
    return qml.probs(wires=estimation_wires)
    
U = qml.T.compute_matrix()
print(qpe(U))




estimation_wires = [0, 1, 2]
target_wires = [3]

def estimate_phase(probs):
    """Estimate the value of a phase given measurement outcome probabilities
    of the QPE routine.
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
    
    Returns:
        float: the estimated phase   
    """
    ##################
    # YOUR CODE HERE #
    ################## 
    increment = 2** -3
    arr= []
    for i in range(8):
        arr.append(i * increment)
    return float(sum(np.array(arr)*probs))


U = qml.T.compute_matrix()

probs = qpe(U)





dev = qml.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qml.PauliX(wires=target_wires)

@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.
        
    Returns:
        array[float]: Probabilities on the estimation wires.
    """
    
    prepare_eigenvector()
    
    ##################
    # YOUR CODE HERE #
    ################## 
    qml.QuantumPhaseEstimation(unitary, target_wires,estimation_wires)
    return qml.probs(wires=estimation_wires)


U = qml.T.compute_matrix()
probs = qpe(U)
print(estimate_phase(probs))

