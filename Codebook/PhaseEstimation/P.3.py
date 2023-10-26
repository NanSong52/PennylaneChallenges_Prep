# P.3 Let's be rational
dev = qml.device("default.qubit", wires=10)

def fractional_binary_to_decimal(binary_fraction, wires):
    return float(binary_fraction/ 2 ** len(wires))

def phase_window(probs, estimation_wires):
    """ Given an array of probabilities, return the phase window of the 
    unitary's eigenvalue
    
    Args: 
        probs (array[float]): Probabilities on the estimation wires.
        estimation_wires (list[int]): List of estimation wires
    
    Returns:
        (float, float): the lower and upper bound of the phase
    """

    ##################
    # YOUR CODE HERE #
    ################## 
    increment = 2** -len(estimation_wires)
    arr= [ ]
    for i in range(2 **len(estimation_wires)):
        arr.append(i * increment)

    probs = [i for i in probs]
    values = sorted(probs)

    bound_1 = arr[probs.index(values[-1])] # MOST LIKELY OUTCOME
    bound_2 = arr[probs.index(values[-2])]  # SECOND MOST LIKELY OUTCOME
    return bound_1, bound_2


# Test your solution

# You can increase the number of estimation wires to a maximum of range(0, 9)
estimation_wires = range(0, 9)

# The target is set to the last qubit
target_wires = [9]

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

probs = qpe(U, estimation_wires, target_wires)

print(phase_window(probs, estimation_wires))

# MODIFY TO TRUE AFTER TESTING YOUR SOLUTION
done = True









dev = qml.device("default.qubit", wires=10)

def estimates_array(unitary):
    """ Given a unitary, return a list of its phase windows
    
    Args: 
        unitary (array[complex]): A unitary matrix.
    
    Returns:
        [(float, float)]: a list of phase windows for 2 to 9 
        estimation wires
    """

    estimates = []
    target_wires = [9]

    ##################
    # YOUR CODE HERE #
    ################## 
    for i in range(1,9):
        estimation_wires= [j for j in range(i+1)]
        probs = qpe(unitary, estimation_wires, target_wires)
        b1= phase_window(probs, estimation_wires)
        estimates.append(b1)
        
    return estimates

# Define the unitary
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])

estimates_array(U)

###################
# SUBMIT FOR PLOT #
###################












