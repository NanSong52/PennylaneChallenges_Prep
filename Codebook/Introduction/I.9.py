# I.9: Measurements 

import pennylane as qml
from pennylane import numpy as np   

dev = qml.device("default.qubit", wires=1)



@qml.qnode(dev)
def apply_h_and_measure(state):
    """Complete the function such that we apply the Hadamard gate
    and measure in the computational basis.
    
    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise leave it in state 0.
    
    Returns:
        array[float]: The measurement outcome probabilities.
    """
    if state == 1:
        qml.PauliX(wires=0)

    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY HADAMARD AND MEASURE
    qml.Hadamard(wires=0)

    return qml.probs(wires=0)

print(apply_h_and_measure(0))
print(apply_h_and_measure(1))


##################
# YOUR CODE HERE # q2
##################

# WRITE A QUANTUM FUNCTION THAT PREPARES (1/2)|0> + i(sqrt(3)/2)|1>
def prepare_psi():
    state = np.array([1/2, 1j*(np.sqrt(3)/2)])
    return qml.MottonenStatePreparation(state_vector= state,wires=0 )
# Prepares an arbitrary state on the given wires 
# using a decomposition into gates developed by Möttönen et al. (2004).
# MottonenStatePreparation(state_vector, wires, id=None)



# WRITE A QUANTUM FUNCTION THAT SENDS BOTH |0> TO |y_+> and |1> TO |y_->
def y_basis_rotation():
    qml.Hadamard(wires=0) # target matrix has sqrt(2)
    qml.S(wires=0) # i for |1>; 1 for |0>
    return qml.state()




# q3: something wrong here?
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def measure_in_y_basis():
    ##################
    # YOUR CODE HERE #
    ##################
    
    # PREPARE THE STATE
    prepare_psi()
    y_basis_rotation()
    # PERFORM THE ROTATION BACK TO COMPUTATIONAL BASIS
    qml.Hadamard(wires=0) # h^dagger = H
    qml.adjoint(qml.S)(wires=0) 

    # I dont think this is a correct order
    # I think should be S^dagger H^dagger
   
    # RETURN THE MEASUREMENT OUTCOME PROBABILITIES

    return qml.probs(wires=0)

print(measure_in_y_basis())
