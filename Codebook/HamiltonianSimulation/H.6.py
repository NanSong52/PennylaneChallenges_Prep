# H.6 Linear combination of unitaries



aux = 0
main = 1
n_bits = 2
dev = qml.device("default.qubit", wires=n_bits)

def add_two_unitaries(U, V):
    """A circuit to apply the sum of two unitaries non-deterministically.
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        V (array): A unitary matrix, stored as a complex array.
    """
    qml.Hadamard(wires=aux)
    ##################
    # YOUR CODE HERE #
    ##################
    qml.ControlledQubitUnitary(U,control_wires=[0],wires=[1],control_values=[0])
    qml.ControlledQubitUnitary(V,control_wires=[0],wires=[1],control_values=[1])
    qml.Hadamard(wires=aux)



@qml.qnode(dev)
def X_plus_Z():
    """Apply X + Z to |0> and return the state."""
    ##################
    # YOUR CODE HERE #
    ##################
    add_two_unitaries(qml.PauliX.compute_matrix(),qml.PauliZ.compute_matrix())
    return qml.state()

print("The amplitudes on the main register are proportional to", X_plus_Z()[:2], ".")





k_bits = 2
n_bits = 2
all_bits = k_bits + n_bits
aux = range(k_bits)
main = range(k_bits, all_bits)
dev = qml.device("default.qubit", wires=all_bits)

def SELECT_uniform(U_list):
    """Implement the SELECT subroutine for 2^k unitaries.
    
    Args:
        U_list (list[array[complex]]): A list of unitary matrices, stored as 
        complex arrays.
    """
    for index in range(2**k_bits):
        ctrl_str =  np.binary_repr(index, k_bits) # Create binary representation
        ##################
        # YOUR CODE HERE #
        ##################
        qml.ControlledQubitUnitary(U_list[index],
        control_wires=[i for i in range(k_bits)],
        wires=[i for i in range(k_bits,all_bits)],
        control_values=ctrl_str)



@qml.qnode(dev)
def XH_plus_HZ():
    """Apply XH + HZ to |01> and return the state."""
    U_list = [np.kron(qml.PauliX.compute_matrix(), qml.PauliX.compute_matrix()),
              np.kron(qml.PauliZ.compute_matrix(), qml.PauliZ.compute_matrix()),
              np.kron(qml.PauliX.compute_matrix(), qml.PauliZ.compute_matrix()),
              np.kron(qml.PauliZ.compute_matrix(), qml.PauliX.compute_matrix())]
    ##################
    # YOUR CODE HERE #
    ##################

    qml.PauliX(wires=main[1]) # |01> on main register (second one is 1)
    for i in aux: 
        qml.Hadamard(wires=[i])
        
    SELECT_uniform(U_list)
    
    for i in aux:
        qml.Hadamard(wires=[i])
    return qml.state()

print("The amplitudes on the main register are proportional to", XH_plus_HZ()[:4], ".")








def V(t):
    """Matrix for the PREPARE subroutine for the first-order approximation."""
    return np.array(
        [
            [np.sqrt(t) / np.sqrt(t + 1), -1 / np.sqrt(t + 1)],
            [1 / np.sqrt(t + 1), np.sqrt(t) / np.sqrt(t + 1)],
        ]
    )

def exp_U_first(U, t):
    """Implements the first two terms in the Taylor series for exp(tU).
    
    Args:
        U (array): A unitary matrix, stored as a complex array.
        t (float): A time to evolve by.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    qml.QubitUnitary(V(t),wires=0)
    qml.ControlledQubitUnitary(U, control_wires= 0, wires= 1, control_values=0)
    qml.ControlledQubitUnitary(np.identity(2), control_wires= 0, wires= 1, control_values=1)
    qml.adjoint(qml.QubitUnitary)(V(t),wires=0)
    

# np.identity(2): 2 by 2 identity matrix
# array([[1., 0.], [0., 1.]])



def prepare(coeffs):
    """Implements the PREPARE subroutine.,

    Args:
        coeffs (array): A vector of coefficients.
    """
    ##################
    # YOUR CODE HERE #
    ##################  
    # Create a quantum circuit with the auxiliary wires
    

    qml.MottonenStatePreparation( normalize(coeffs), wires=aux)


    
    def select(unitaries):
    """Implements a sequence of 4 controlled-unitary operations.

    Args:
        unitaries (list): A list containing 4 unitary operations in this order:
        (U0, U1, U2, U3).
    """
    ##################
    # YOUR CODE HERE #
    ##################

    qml.ControlledQubitUnitary(unitaries[0],
        control_wires=[i for i in aux],
        wires=[i for i in main],
        control_values= [0,0])

    qml.ControlledQubitUnitary(unitaries[1],
        control_wires=[i for i in aux],
        wires=[i for i in main],
        control_values= [0,1])
        
    qml.ControlledQubitUnitary(unitaries[2],
        control_wires=[i for i in aux],
        wires=[i for i in main],
        control_values= [1,0])
        
    qml.ControlledQubitUnitary(unitaries[3],
        control_wires=[i for i in aux],
        wires=[i for i in main],
        control_values= [1,1])
    


def v0(t):
    """Calculates the first column of the PREPARE matrix, v0.

    Args:
        t (float): the time we evolve for.

    Returns:
        (array): v0 = [v00, v01, v02, v03] normalized
    """
    ##################
    # YOUR CODE HERE #
    ##################
    v00 = 1/(np.sqrt(1+t+t**2/2))* 1
    v01 = 1/(np.sqrt(1+t+t**2/2))* np.sqrt(t)
    v02 = 1/(np.sqrt(1+t+t**2/2))* t /np.sqrt(2)
    v03 = 0
    
    return normalize([v00, v01, v02, v03])

    

def exp_U_second(unitaries, t):
    """Implements the second-order approximation to Hamiltonian time evolution. 

    Args:
        unitaries (list): A list containing 4 unitary operations in this order:
        (U0, U1, U2, U3).
        t (float): The Hamiltonian evolution time. 
    """
    ##################
    # YOUR CODE HERE #
    ##################
    x = v0(t)
    prepare(x)
    select(unitaries)
    qml.adjoint(qml.MottonenStatePreparation(normalize(x),wires=[0,1])) # wired this way because of the representation of the adjoint v^dagger
    # prepare state => adjoint state  


# Codercise H.6.5.  


aux = [0, 1]
main = [2]
all_bits = aux + main

U = qml.PauliX.compute_matrix()*(1.j)
unitaries = [np.eye(2), U, U @ U, np.eye(2)] # U0, U1, U2, U3
# Remember — U3 can be arbitrary!

dev1 = qml.device("default.qubit", wires=[aux[0]] + main)
dev2 = qml.device("default.qubit", wires=all_bits)

# H.6.3
@qml.qnode(dev1)
def first_approx(t):
    ##################
    # YOUR CODE HERE #
    ##################
    exp_U_first(U, t)
    return qml.state()

# H.6.4
@qml.qnode(dev2)
def second_approx(t):
    ##################
    # YOUR CODE HERE #
    ##################
    exp_U_second(unitaries, t)
    return qml.state()

# Exact Hamiltonian evolution
@qml.qnode(dev2)
def exact(t):
    ##################
    # YOUR CODE HERE #
    ##################
    qml.RX(-2*t, wires=main)
    return qml.state()

##################
# HIT SUBMIT FOR #
# PLOTTING MAGIC #
##################






