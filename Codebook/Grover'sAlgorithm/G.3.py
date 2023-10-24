# G.3 Searching with circuits
import pennylane as qml
from pennylane import numpy as np

n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register+aux
dev = qml.device('default.qubit', wires=all_wires)

def oracle(combo):
    """Implement an oracle using a multi-controlled X gate.
    
    Args:
        combo (list): A list of bits representing the secret combination.
    """
    combo_str = ''.join(str(j) for j in combo)
    ##################
    # YOUR CODE HERE #
    ##################
    
    return qml.MultiControlledX(query_register, wires=aux, control_values = combo_str)
    # pass # APPLY MULTI-CONTROLLED X

def hadamard_transform(my_wires):
    """Apply the Hadamard transform on a given set of wires.
    
    Args:
        my_wires (list[int]): A list of wires on which the Hadamard transform will act.
    """
    for wire in my_wires:
        qml.Hadamard(wires=wire)

def diffusion():
    """Implement the diffusion operator using the Hadamard transform and 
    multi-controlled X."""

    ##################
    # YOUR CODE HERE #
    ##################
    hadamard_transform(query_register)
    qml.MultiControlledX(query_register, wires=aux, control_values = "0"*len(query_register))
    hadamard_transform(query_register)




@qml.qnode(dev)
def grover_circuit(combo):
    """Apply the MultiControlledX Grover operator and return probabilities on 
    query register.
    
    Args:
        combo (list[int]): A list of bits representing the secret combination.

    Returns:
        array[float]: Measurement outcome probabilities.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    # PREPARE QUERY AND AUXILIARY SYSTEM
    # APPLY GROVER ITERATION
    qml.PauliX(wires= aux)
    hadamard_transform(all_wires)
    oracle(combo)
    diffusion()
        
    return qml.probs(wires=query_register)
