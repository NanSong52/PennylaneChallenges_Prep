# I.15 Quantum teleportation



import pennylane as qml
from pennylane import numpy as np


def state_preparation():
    ##################
    # YOUR CODE HERE #
    ##################

    # OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE

    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)




dev = qml.device("default.qubit", wires=1)

##################
# YOUR CODE HERE #
##################

# OPTIONALLY REPLACE THIS STATE PREPARATION ROUTINE WITH
# THE ONE FROM THE PREVIOUS EXERCISE

def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def state_prep_only():
    state_preparation()
    return qml.state()

print(state_prep_only())



def entangle_qubits():
    ##################
    # YOUR CODE HERE #
    ##################

    # ENTANGLE THE SECOND QUBIT (WIRES=1) AND THE THIRD QUBIT
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[1,2])



def rotate_and_controls():
    ##################
    # YOUR CODE HERE #
    ##################

    # PERFORM THE BASIS ROTATION

    # PERFORM THE CONTROLLED OPERATIONS
    qml.CNOT(wires=[0,1])
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[1,2])
    qml.CZ(wires=[0,2])


    dev = qml.device("default.qubit", wires=3)

##################
# YOUR CODE HERE #
##################

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def teleportation():
    ##################
    # YOUR CODE HERE #
    ##################

    # USE YOUR QUANTUM FUNCTIONS TO IMPLEMENT QUANTUM TELEPORTATION
    state_preparation()
    entangle_qubits()
    rotate_and_controls()
    # RETURN THE STATE
    return qml.state()


print(teleportation())



def extract_qubit_state(input_state):
    """Extract the state of the third qubit from the combined state after teleportation.
    
    Args:
        input_state (array[complex]): A 3-qubit state of the form 
            (1/2)(|00> + |01> + |10> + |11>) (a|0> + b|1>)
            obtained from the teleportation protocol.
            
    Returns:
        array[complex]: The state vector np.array([a, b]) of the third qubit.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # DETERMINE THE STATE OF THE THIRD QUBIT

    return np.array([2* input_state[0], 2*input_state[1]])
    

# Here is the teleportation routine for you
dev = qml.device("default.qubit", wires=3)

#################
# YOUR CODE HERE #
##################

# OPTIONALLY UPDATE THIS STATE PREPARATION ROUTINE
def state_preparation():
    qml.Hadamard(wires=0)
    qml.Rot(0.1, 0.2, 0.3, wires=0)


@qml.qnode(dev)
def teleportation():
    state_preparation()
    entangle_qubits()
    rotate_and_controls()    
    return qml.state()

# Print the extracted state after teleportation
full_state = teleportation()
print(extract_qubit_state(full_state))

# Congratulations!
# Press submit to finish this module and start exploring a new one.
