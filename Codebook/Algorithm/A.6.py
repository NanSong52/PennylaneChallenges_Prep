# A.6 Deutsch-Jozsa


import pennylane as qml
from pennylane import numpy as np


n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def multisol_hoh_circuit(combos):
    """A circuit which applies Hadamard, multi-solution oracle, then Hadamard.
    
    Args:
        combos (list[list[int]]): A list of secret bit strings.

    Returns: 
        array[float]: Probabilities for observing different outcomes.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    U = multisol_oracle_matrix(combos)
    qml.broadcast(qml.Hadamard,"single", [0,1,2,3])
    qml.QubitUnitary(U,wires=[0,1,2,3])
    qml.broadcast(qml.Hadamard,"single", [0,1,2,3])
    return qml.probs(wires=range(n_bits))

def deutsch_jozsa(promise_var):
    """Implement the Deutsch-Jozsa algorithm and guess the promise variable.
    
    Args:
        promise_var (int): Indicates whether the function is balanced (0) or constant (1).
        
    Returns: 
        int: A guess at the promise variable.
    """
    if promise_var == 0:
        how_many = 2**(n_bits - 1)
    else:
        how_many = np.random.choice([0, 2**n_bits]) # Choose all or nothing randomly
    combos = multisol_combo(n_bits, how_many) # Generate random combinations

    ##################
    # YOUR CODE HERE #
    ##################

    probs = multisol_hoh_circuit(combos)
    if np.isclose(probs[0],1):
        return 1
    else:
        return 0






