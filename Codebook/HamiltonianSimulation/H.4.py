# H.4 Energy in quantum systems

n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def zz_circuit(alpha, time, init):
    """Circuit for evolving two electrons with a ZZ interaction.
    
    Args:
        alpha (float): The strength of the interaction.
        time (float): The time we evolve the electron wavefunction for.
        init (numpy.array(int)): An initial state specified by two bits [x, y]. Prepare the
            system in this state prior to applying the time evolution circuit.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """
    hbar = 1e-34
    ##################
    # YOUR CODE HERE #
    ##################
    qml.BasisState(init,wires=[i for i in range(n_bits)])
    qml.CNOT(wires=[0,1])
    qml.RZ(2*alpha*time / hbar, wires=1)
    qml.CNOT(wires=[0,1])
    return qml.probs(wires=range(n_bits))




n_bits = 5
dev = qml.device("default.qubit", wires=n_bits)
    
##################
# YOUR CODE HERE #
##################
coeffs = [1] # MODIFY THIS
obs = [qml.PauliZ(0)] # MODIFY THIS
H = qml.Hamiltonian(coeffs, obs)

@qml.qnode(dev)
def energy(init):
    """Circuit for measuring expectation value of Hamiltonian in a given state.
    
    Args:
        init (numpy.array(int)): An initial computational basis state, specified by five bits.

    Returns: 
        float: Expectation value of the Hamiltonian H.
    """
    qml.BasisState(init, wires=range(n_bits))

    obs = [qml.PauliZ(0)@qml.PauliZ(1), qml.PauliZ(1)@qml.PauliZ(2), qml.PauliZ(1)@qml.PauliZ(3), qml.PauliZ(3)@qml.PauliZ(4)]
    coeffs =  [1,1,1,1]
    H = qml.Hamiltonian(coeffs, obs)
    return qml.expval(H)



my_guess1 = np.array([0,1,0,0,1]) # opposite in every term Z01 =[0,1] or [1,0]
my_guess2 = np.array([1,0,1,1,0]) # MODIFY THIS

print("The expected energy for", my_guess1, "is", energy(my_guess1), ".")
print("The expected energy for", my_guess2, "is", energy(my_guess2), ".")

