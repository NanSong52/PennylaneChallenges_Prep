# S.3 Period finding

def U():
    qml.SWAP(wires=[2,3])
    qml.SWAP(wires=[1,2])
    qml.SWAP(wires=[0,1])
    for i in range(4):
        qml.PauliX(wires=i)

matrix = get_unitary_matrix(U, wire_order=range(4))()

n_target_wires = 4
target_wires = range(n_target_wires)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)


dev = qml.device("default.qubit", shots=1, wires=n_target_wires+n_estimation_wires)

@qml.qnode(dev)
def circuit(matrix):
    """Return a sample after taking a shot at the estimation wires.
    
    Args:
        matrix (array[complex]): matrix representation of U.

    Returns:
        array[float]: a sample after taking a shot at the estimation wires.
    """
    
    ##################
    # YOUR CODE HERE #
    ##################
    
    # CREATE THE INITIAL STATE |0001> ON TARGET WIRES
    qml.PauliX(wires=3)
    # USE THE SUBROUTINE QUANTUM PHASE ESTIMATION
    qml.QuantumPhaseEstimation(matrix,[0,1,2,3], [4,5,6])
    return qml.sample(wires=estimation_wires)

def get_phase(matrix):
    binary = "".join([str(b) for b in circuit(matrix)])
    return int(binary, 2) / 2 ** n_estimation_wires

for i in range(5):
    print(circuit(matrix))
    print(f"shot {i+1}, phase:",get_phase(matrix))








def U():
    qml.SWAP(wires=[2,3])
    qml.SWAP(wires=[1,2])
    qml.SWAP(wires=[0,1])
    for i in range(4):
        qml.PauliX(wires=i)

matrix = get_unitary_matrix(U, wire_order=range(4))()

target_wires = range(4)
n_estimation_wires = 3
estimation_wires = range(4, 4 + n_estimation_wires)

def get_period(matrix):
    """Return the period of the state using the already-defined 
    get_phase function.
    
    Args:
        matrix (array[complex]): matrix associated with the operator U
        
    Returns:
        int: Obtained period of the state.
    """
    
    shots = 10
    
    ##################
    # YOUR CODE HERE #
    ##################

    denominator = []
    for i in range(shots):
        phase = get_phase(matrix)
        f = Fraction(phase).limit_denominator(2**3)
        denominator.append(f.denominator)
        
    return np.max(denominator)

    

print(get_period(matrix))

def U():
    qml.SWAP(wires=[2,3])
    qml.SWAP(wires=[1,2])
    qml.SWAP(wires=[0,1])
    for i in range(4):
        qml.PauliX(wires=i)

dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev)
def circuit():
    """Apply U four times to |0001> to verify this is the period.
    
    Returns:
        array[float]: probabilities of each basis state. 
    """
    
    ##################
    # YOUR CODE HERE #
    ##################
    qml.PauliX(wires=3)
    U()
    U()
    U()
    U()
    
    return qml.probs(wires=range(4))


print(circuit())




