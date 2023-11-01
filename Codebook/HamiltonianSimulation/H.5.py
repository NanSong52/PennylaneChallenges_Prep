# 

n_bits=2
dev = qml.device("default.qubit", wires=range(n_bits))

@qml.qnode(dev)
def two_distant_spins(B, time):
    """Circuit for evolving the state of two distant electrons in a magnetic field.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron wavefunction for.

    Returns: 
        array[complex]: The quantum state after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################
    qml.RZ(-2 * alpha * time,wires=0)
    qml.RZ(-2 * alpha * time,wires=1)
    return qml.state()



@qml.qnode(dev)
def two_close_spins_X(B, J, time, n):
    """Circuit for evolving the state of two electrons with an X coupling.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (float): The strength of the coupling between electrons.
        time (float): The time we evolve the electron wavefunction for.
        n (int): The number of steps in our Trotterization.

    Returns: 
        array[complex]: The quantum state after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    hbar = 1e-34
    beta = -J*hbar/4
    ##################
    # YOUR CODE HERE #
    ##################
    for i in range(n):
        qml.PauliRot(-2*beta*time/n, "XX", wires=[0,1])
        qml.PauliRot(-2*alpha*time/n, "Z",wires=0)
        qml.PauliRot(-2*alpha*time/n, "Z",wires=1)    
    return qml.state()





def ham_close_spins(B, J):
    """Creates the Hamiltonian for two close spins.

    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (list[float]): A vector of couplings [J_X, J_Y, J_Z].

    Returns:
        qml.Hamiltonian: The Hamiltonian of the system.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    hbar = 1e-34
    ##################
    # YOUR CODE HERE #
    ##################
    coeffs = [-alpha,-alpha, hbar/4*J[0],
    hbar/4*J[1],hbar/4*J[2]] # MODIFY THIS
    obs = [qml.PauliZ(0),qml.PauliZ(1),
    qml.PauliX(0)@qml.PauliX(1), qml.PauliY(0)@qml.PauliY(1),
    qml.PauliZ(0)@qml.PauliZ(1)] # MODIFY THIS
    return qml.Hamiltonian(coeffs, obs)




@qml.qnode(dev)
def two_close_spins(B, J, time, n):
    """Circuit for evolving the state of two nearby electrons with an arbitrary coupling.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (array[float]): The coupling strengths J = [J_X, J_Y, J_Z] between electrons.
        time (float): The time we evolve the electron wavefunction for.
        n (int): The number of steps in our Trotterization.

    Returns: 
        array[complex]: The quantum state after evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    ham = ham_close_spins(B, J)
    qml.ApproxTimeEvolution(ham,time,n)
    return qml.state()
