# F.2 Quantum Fourier transform
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def one_qubit_QFT(basis_id):
    """A circuit that computes the QFT on a single qubit. 
    
    Args:
        basis_id (int): An integer value identifying 
            the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubit after applying QFT.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=dev.num_wires)]
    qml.BasisStatePreparation(bits, wires=[0])
    
    ##################
    # YOUR CODE HERE #
    ##################
    qml.Hadamard(wires=0) # N=1, same with Hadamard Gate!
    return qml.state()


n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using qml.QubitUnitary. 
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=2)]
    qml.BasisStatePreparation(bits, wires=[0, 1])
    
    ##################
    # YOUR CODE HERE #
    ##################
    w = np.exp(np.pi * 1j / 2)

    U = [[1, 1, 1, 1], [1, w, w**2, w**3], [1, w**2, w**0, w**2], [1, w**3, w**2, w**1]]
    U = 1/2 * np.array(U)
    qml.QubitUnitary(U, wires=[0,1])
    return qml.state()



dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def decompose_two_qubit_QFT(basis_id):
    """A circuit that computes the QFT on two qubits using elementary gates.
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
    
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=dev.num_wires)]
    qml.BasisStatePreparation(bits, wires=[0, 1])
    
    ##################
    # YOUR CODE HERE #
    ##################
    qml.Hadamard(wires=0)
    qml.ctrl(qml.S, control=1)(wires=0)
    qml.Hadamard(wires=1)
    qml.SWAP(wires=[0,1])
    
    return qml.state()







