# F.3: Connecting the dots


dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def three_qubit_QFT(basis_id):
    """A circuit that computes the QFT on three qubits.
    
    Args:
        basis_id (int): An integer value identifying the basis state to construct.
        
    Returns:
        array[complex]: The state of the qubits after the QFT operation.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=dev.num_wires)]
    qml.BasisStatePreparation(bits, wires=[0, 1, 2])
    
    ##################
    # YOUR CODE HERE #
    ################## 
    qml.Hadamard(wires=0)
    qml.ctrl(qml.PhaseShift(2*np.pi/2**2, wires=0), control=1)
    qml.ctrl(qml.PhaseShift(2*np.pi/2**3, wires=0), control=2)
    qml.Hadamard(wires=1)
    qml.ctrl(qml.PhaseShift(2*np.pi/2**2, wires=1), control=2)
    qml.Hadamard(wires=2)
    qml.SWAP(wires=[0,2])
    return qml.state()











dev = qml.device('default.qubit', wires=4)

            
def swap_bits(n_qubits):
    """A circuit that reverses the order of qubits, i.e.,
    performs a SWAP such that [q1, q2, ..., qn] -> [qn, ... q2, q1].
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    i = 0
    j = n_qubits -1
    
    while i !=j and i < j:
        qml.SWAP(wires= [i,j])
        i += 1
        j -= 1
    
     

@qml.qnode(dev) 
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    # qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qml.state()





# hard one: F.3.3
dev = qml.device('default.qubit', wires=4)

def qft_rotations(n_qubits):
    """A circuit performs the QFT rotations on the specified qubits.
    
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
    """

    ##################
    # YOUR CODE HERE #
    ################## 
    for i in range(n_qubits):
        qml.Hadamard(wires=i)
        for j in range(i+1, n_qubits):
            qml.ControlledPhaseShift(2*np.pi/2**(j-i+1),wires=[j,i]) # how to get R_k correctly? k = j-i+1 =n-(n-1)+1 = 2

@qml.qnode(dev) 
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qml.state()






# 递归解决问题
dev = qml.device('default.qubit', wires=4)

def qft_recursive_rotations(n_qubits, wire=0):
    """A circuit that performs the QFT rotations on the specified qubits
        recursively.
        
    Args:
        n_qubits (int): An integer value identifying the number of qubits.
        wire (int): An integer identifying the wire 
                    (or the qubit) to apply rotations on.
    """

    ##################
    # YOUR CODE HERE #
    ################## 
    if wire == n_qubits-1:
        qml.Hadamard(wires=wire)
    else:
        qml.Hadamard(wires=wire)     
        for j in range(wire+1, n_qubits):
            qml.ControlledPhaseShift(2*np.pi/2**(j-wire+1),wires=[j,wire])
        qft_recursive_rotations(n_qubits, wire+1)   
        
@qml.qnode(dev) 
def qft_node(basis_id, n_qubits):
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))
    qft_recursive_rotations(n_qubits)
    swap_bits(n_qubits)
    return qml.state()




dev = qml.device('default.qubit', wires=4)

@qml.qnode(dev)
def pennylane_qft(basis_id, n_qubits):
    """A that circuit performs the QFT using PennyLane's QFT template.
    
    Args:
        basis_id (int): An integer value identifying 
            the basis state to construct.
        n_qubits (int): An integer identifying the 
            number of qubits.
            
    Returns:
        array[complex]: The state after applying the QFT to the qubits.
    """
    # Prepare the basis state |basis_id>
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qml.BasisStatePreparation(bits, wires=range(n_qubits))

    ##################
    # YOUR CODE HERE #
    ################## 
    qml.QFT(wires= range(n_qubits))
    return qml.state()



