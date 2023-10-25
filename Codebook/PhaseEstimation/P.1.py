# P.1 Catch the phase



dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def guess_the_unitary(unitary):
    """Given a unitary that performs a Z or a -Z operation
    on a qubit, guess which one it is.
    
    Args: 
        U (array[complex]): A unitary matrix, guaranteed to be either Z or -Z.
    
    Returns:
        array [int]:  Probabilities on  on the first qubit
        using qml.probs()
    """
    ##################
    # YOUR CODE HERE #
    ##################  
    qml.Hadamard(wires=0)
    qml.ctrl(qml.QubitUnitary,control=0)(unitary, wires=1)
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)

# Z gate 
U = qml.PauliZ.compute_matrix() 

# -Z gate
# U = (-1)*qml.PauliZ.compute_matrix()

print(guess_the_unitary(U))




dev = qml.device("default.qubit", wires=2)
        
@qml.qnode(dev)
def phase_kickback_X(eigenvector):
    """ Given an eigenvector of X, 
    apply the phase kickback circuit to observe 
    the probabilities on the control wire
    
    Args: 
        eigenvector(String): A string "plus" or "minus" depicting 
        the eigenvector of X
    
    Returns:
        array[int]: Measurement outcome on the first qubit using qml.probs()
    """
    # Prepare |ψ>
    ##################
    # YOUR CODE HERE #
    ##################  
    if eigenvector != "plus":
        qml.PauliX(wires=1)
    qml.Hadamard(wires=1)
    # Phase kickback
    ##################
    # YOUR CODE HERE #
    ################## 
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=0)
    return qml.probs(wires=[0])   

print(phase_kickback_X("plus"))
print(phase_kickback_X("minus"))

# MODIFY EIGENVALUES BELOW 
eigenvalue_of_X_plus = 1
eigenvalue_of_X_minus = -1





