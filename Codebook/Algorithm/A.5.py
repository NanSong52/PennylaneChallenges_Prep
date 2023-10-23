# A.5 Hadamard transform

from pennylane import numpy as np
import pennylane as qml


n_bits = 4
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def hoh_circuit(combo):
    """A circuit which applies Hadamard-oracle-Hadamard and returns probabilities.
    
    Args:
        combo (list[int]): A list of bits representing a secret combination.

    Returns:
        list[float]: Measurement outcome probabilities.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    qml.broadcast(qml.Hadamard,"single", [0,1,2,3])
    qml.QubitUnitary(oracle_matrix(combo),wires=[0,1,2,3])
    qml.broadcast(qml.Hadamard,"single", [0,1,2,3])

    return qml.probs(wires=range(n_bits))
