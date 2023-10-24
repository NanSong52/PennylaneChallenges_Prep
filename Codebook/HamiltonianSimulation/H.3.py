
# H.3 Hamiltonians



def mag_z_unitary(B, time):
    """Creates a unitary operator to evolve the state of an electron in 
    a magnetic field.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time (t) we evolve the electron state for.
        
    Returns:
        array[complex]: The unitary matrix implementing time evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################
    matrix = np.array([[0+0j, 0], [0, 0+0j]]) # CHANGE THIS
    matrix[0][0] = np.exp(alpha*time*1j)
    matrix[1][1] = np.exp(alpha*time*-1j)
    return matrix

B, t = 0.1, 0.6
if unitary_check(mag_z_unitary(B, t)):
    print("The output is unitary for B =", B, "and t =", t, ".")





dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def mag_z_0_v1(B, time):
    """Simulates an electron (initial state |0>) in a magnetic field, using a 
    unitary matrix.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        array[complex]: The state of the system after evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    qml.QubitUnitary(mag_z_unitary(B, time), wires=0)
    return qml.state()

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def mag_z_0_v2(B, time):
    """Simulates an electron (initial state |0>) in a magnetic field, using a 
    Z rotation.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        array[complex]: The state of the system after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################
    qml.RZ(-2*alpha*time,wires=0)
    return qml.state()

B, t = 0.1, 0.6
if np.allclose(mag_z_0_v1(B, t), mag_z_0_v2(B, t)):
    print("The two circuits give the same answer!")



dev = qml.device("default.qubit", wires=1)

def evolve_plus_state(B, time):
    """Simulates an electron (initial state |+>) in a magnetic field.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B*e/(2*m_e)
    ##################
    # YOUR CODE HERE #
    ##################
    qml.Hadamard(wires=0)
    qml.RZ(-2*alpha*time,wires=0)
    
    
    

@qml.qnode(dev)
def mag_z_plus_X(B, time):
    """Simulates an electron (initial state |+>) in a magnetic field and returns <X>.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        float: Expectation value for the Pauli X operator.
    """
    evolve_plus_state(B, time)
    return qml.expval(qml.PauliX(0))

@qml.qnode(dev)
def mag_z_plus_Y(B, time):
    """Simulates an electron (initial state |+>) in a magnetic field and returns <Y>.
    
    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        time (float): The time we evolve the electron state for.

    Returns:
        float: Expectation value for the Pauli X operator.
    """
    evolve_plus_state(B, time)
    return qml.expval(qml.PauliY(0))

##################
# HIT SUBMIT FOR #
# PLOTTING MAGIC #
##################

