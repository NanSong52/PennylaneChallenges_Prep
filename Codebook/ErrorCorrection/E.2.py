# E.2 No flip-flopping allowed!

# Codercise E.2.1
dev = qml.device("default.mixed", wires=3)

@qml.qnode(dev)
def bitflip_code_expval(p):
    """A circuit that uses two auxiliary qubits to encode the message of the first qubit, puts them through a simple noisy channel with a chance of a bit-flip error occuring, then decodes it and measures the expectation value of the original message.
    
    Args:
        p (float): Probability of one bit-flip error occuring in the noisy channel for each wire.

    Returns: 
        (float): Expectation value of the message qubit.
    """
    # Using two auxiliary qubits on wires 1 and 2, encode the message on wire 0 into a logical qubit
    ##################
    # YOUR CODE HERE #
    ##################
    qml.CNOT(wires=[0, 1])  # Apply CNOT gate on wires 0 and 1
    qml.CNOT(wires=[0, 2])

    # Put all wires through a noisy channel, where each wire has a probability p that a bit-flip error will occur
    qml.BitFlip(p, wires=0)
    qml.BitFlip(p, wires=1)
    qml.BitFlip(p, wires=2)
    
    # Decode the message after the noisy channel
    ##################
    # YOUR CODE HERE #
    ##################
    qml.CNOT(wires=[0, 1])  # Apply CNOT gate on wires 0 and 1
    qml.CNOT(wires=[0,2])
    qml.Toffoli(wires=[1, 2, 0])
    
    # Measure the expectation value of the message
    return qml.expval(qml.PauliZ([0]))




# Codercise E.2.2
dev = qml.device("default.mixed", wires=3)

@qml.qnode(dev)
def phaseflip_code_expval(p):
    """A circuit that uses two auxiliary qubits to encode the message of the first qubit, puts them through a simple noisy channel with a chance of a bit-flip error occurring, then decodes it and measures the expectation value of the original message.
    
    Args:
        p (float): Probability of one bit-flip error occurring in the noisy channel for each wire.

    Returns: 
        (float): Expectation value of the message qubit.
    """
    # Encode the message on wire 0 into a logical qubit, and transform it into the Hadamard basis

    qml.CNOT(wires=[0, 1])  # Apply CNOT gate on wires 0 and 1
    qml.CNOT(wires=[0, 2])  # Apply CNOT gate on wires 0 and 2
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)# Apply Hadamard gate on wire 0

    # Transform the logical qubit into the Hadamard basis, put all wires through a noisy channel where each wire has a probability p that a phase-flip error will occur, then transform the result back into the computational basis.
    qml.PhaseFlip(p, wires=0)
    qml.PhaseFlip(p, wires=1)
    qml.PhaseFlip(p, wires=2)
    qml.Hadamard(wires=0)  # Apply Hadamard gate on wire 0

    # Decode the message after the noisy channel and transform it back into the computational basis
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)# Apply Hadamard gate on wire 0
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[0,2])# Apply CNOT gate on wires 0 and 1
    qml.Toffoli(wires=[1, 2, 0])  # Apply Toffoli gate on wires 1, 2, and 0

    
    # Measure the expectation value of the message
    return qml.expval(qml.PauliZ([0]))







# Codercise E.2.3
def largest_p():
    # Range of bit-flip error probability
    probability_range = np.arange(0.0, 0.5, 0.01)
    # Initialize the array of function values
    expvals = []
    # Calculate function values for the circuit and append them to the list
    for prob in probability_range:
        expvals.append(bitflip_code_expval(prob))

    # Find out what the largest p is for which the expectation value of the message stays above 0.9
    ##################
    # YOUR CODE HERE #
    ##################
    # Find the largest p for which the expectation value of the message stays above 0.9
    largest_p = 0.0
    for i, expval in enumerate(expvals):
        if expval > 0.9:
            largest_p = probability_range[i]
            
    return largest_p







# Codercise E.2.4

n = 3
dev = qml.device("default.mixed", wires=3)

@qml.qnode(dev)
def multi_bitflip_code_expval(p, n):
    """A circuit that uses two auxiliary qubits to encode the message of the first qubit, puts them through a noisy channel with three opportunities for a bit-flip error occuring on each of the wires, then decodes it and measures the expectation value of the original message.
    
    Args:
        p (float): Probability of one bit-flip error occuring in the noisy channel for each wire.

    Returns: 
        (float): Expectation value of the message qubit.
    """
    # Using two auxiliary qubits on wires 1 and 2, encode the message on wire 0 into a logical qubit
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[0,2])
    
    # Put all wires through a noisy channel, where each wire has a probability p that a bit-flip error will occur
    # This probability occurs three times in a row
    ##################
    # YOUR CODE HERE #
    ##################
    # Put all wires through a noisy channel n times in a row
    for _ in range(n):
        qml.BitFlip(p, wires=0)
        qml.BitFlip(p, wires=1)
        qml.BitFlip(p, wires=2)
    
    # Decode the message after the noisy channel
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[0,2])
    qml.Toffoli(wires=[1,2,0])
    
    # Measure the expectation value of the message
    return qml.expval(qml.PauliZ([0]))










