# H.2 Unitaries
from pennylane import numpy as np

def unitary_check(operator):
    """Checks if a complex-valued matrix is unitary.
    
    Args:
        operator (array[complex]): A square complex-valued array.
        
    Returns: 
        bool: Whether the matrix is unitary or not.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    check =np.allclose(operator.T.dot(operator), np.identity(operator.shape[0]) )
    return check # MODIFY THIS


n_bits = 1
dev = qml.device("default.qubit", wires=n_bits)

@qml.qnode(dev)
def unitary_circuit(operator):
    """Applies a matrix to the state if it is unitary and correctly sized.
    
    Args:
        operator (array[complex]): A square complex-valued array.

    Returns:
        array[complex]: The state of the quantum system, after applying the
        operator, if valid.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    if unitary_check(operator):
        qml.QubitUnitary(operator, wires=0)
    return qml.state()
