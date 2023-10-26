# P.4 A mixed bag

dev = qml.device("default.qubit", wires=5)
estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector_superposition(alpha, beta):
    # Normalize alpha and beta
    norm_squared = np.abs(alpha) ** 2 + np.abs(beta) ** 2
    norm = np.sqrt(norm_squared)
    state = np.array([alpha/norm, beta/norm])
    
    # Prepare the state
    qml.MottonenStatePreparation(state, wires=target_wires)


@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        array[float]: Probabilities on the estimation wires.
    """
    
    # MODIFY ALPHA, BETA TO PREPARE EIGENVECTOR    
    prepare_eigenvector_superposition(0, 1)
    prepare_eigenvector_superposition(1, 0)
    prepare_eigenvector_superposition(1/np.sqrt(2), 1/np.sqrt(2))
    # OR UNCOMMENT LINES ABOVE TO PREPARE THE STATE OF YOUR CHOICE

    qml.QuantumPhaseEstimation(
        unitary,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )
    return qml.probs(wires=estimation_wires)

U = qml.T.compute_matrix()

probs = qpe(U)

# MODIFY TO TRUE WHEN YOU ARE DONE TESTING
done = True







dev = qml.device("default.qubit", wires=5)
estimation_wires = [0, 1, 2]
target_wires = [3, 4]

def prepare_eigenvector_superposition(alpha, beta, gamma, delta):
    # Normalize alpha, beta, gamma, and delta
    norm_squared = np.abs(alpha) ** 2 + np.abs(beta) ** 2 + np.abs(gamma) ** 2 + np.abs(delta) ** 2 
    norm = np.sqrt(norm_squared)
    state = np.array([alpha/norm, beta/norm, gamma/norm, delta/norm])
    
    #Prepare the state
    qml.MottonenStatePreparation(state, wires=target_wires)


@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        array[float]: Probabilities on the estimation wires.
    """
    
    # PREPARE EIGENVECTOR
    # prepare_eigenvector_superposition(0, 0, 0, 1)
    # prepare_eigenvector_superposition(1, 0, 0, 0)
    prepare_eigenvector_superposition(1/4, 1/4, 1/4, 1/4)    
    # four states have same coefficients
    
    qml.QuantumPhaseEstimation(
        unitary,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )
    return qml.probs(wires=estimation_wires)


U = qml.CZ.compute_matrix()

probs = qpe(U)

# MODIFY TO PROBABILITY OF OBSERVING 100 WHEN ESTIMATION 
# WIRES ARE IN EQUAL SUPERPOSITION
probability_100 = 0.25













dev = qml.device("default.qubit", wires=6)
estimation_wires = [0, 1, 2, 3]
target_wires = [4, 5]

def prepare_eigenvector_superposition(alpha, beta, gamma, delta):
    # Normalize alpha, beta, gamma, and delta
    norm_squared = np.abs(alpha) ** 2 + np.abs(beta) ** 2 + np.abs(gamma) ** 2 + np.abs(delta) ** 2 
    norm = np.sqrt(norm_squared)
    state = np.array([alpha/norm, beta/norm, gamma/norm, delta/norm])
    
    # Prepare the state
    qml.MottonenStatePreparation(state, wires=target_wires)


@qml.qnode(dev)
def qpe(unitary):
    """Estimate the phase for a given unitary.
    
    Args:
        unitary (array[complex]): A unitary matrix.

    Returns:
        probs (array[float]): Probabilities on the estimation wires.
    """
    
    # MODIFY ALPHA, BETA, GAMMA, DELTA TO PREPARE EIGENVECTOR 
    prepare_eigenvector_superposition(1/4, 1/4, 1/4, 1/4)
    # prepare_eigenvector_superposition(1, 0, 0, 0)
    # prepare_eigenvector_superposition(0, 1, 0, 0)
    # OR UNCOMMENT LINES ABOVE TO PREPARE THE STATE OF YOUR CHOICE
    
    qml.QuantumPhaseEstimation(
        unitary,
        target_wires=target_wires,
        estimation_wires=estimation_wires,
    )
    return qml.probs(wires=estimation_wires)


# UNCOMMENT THE LINE CORRESPONDING TO THE MATRIX YOU'D LIKE 
# TO ESTIMATE PHASES OF
# U = qml.CZ.compute_matrix()
# U = qml.CRZ.compute_matrix(0.4)
U = qml.CRX.compute_matrix(1/3)
# U = qml.CRot.compute_matrix(0.9, 0.7, 0.4)

probs = qpe(U)
# Sort the probabilities in descending order
sorted_probs = np.sort(probs)[::-1]

# Find the second-largest probability
second_largest_prob = sorted_probs[1]

# Find the corresponding phase value
second_largest_phase_index = np.where(probs == second_largest_prob)[0][0]
m = 2**-len(estimation_wires)
phase = second_largest_phase_index * m
# phase value
mystery_phase = phase  # MODIFY THIS







