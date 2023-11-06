# E.3 Are you Shor this works?

# Codercise E.3.1.
# Create a Z error on qubit 4
z_error_4 = error(error_type="Z", wires=[4])

# Create a YX error on qubits 8 and 0
yx_error_80 = error(error_type="YX", wires=[8, 0])

# Create a XXZZYY error on qubits 1, 2, 3, 4, 5, and 0.
xxzzyy_error_123450 = error(error_type="XXZZYY", wires=[1, 2, 3, 4, 5, 0])



#Codercise E.3.2.
dev = qml.device("default.qubit", wires=9)

@qml.qnode(dev)
def shor(state, error_type, wires):
    """A quantum circuit that implements Shor's 9-qubit code
    
    Args:
        state (tensor): a numpy array representing a 1-qubit state: alpha |0> + beta |1>
                        This is used to initialize the 0th wire with qml.QubitStateVector
        error_type (str): for example, XX, YY, XZ, YZ.
        wires (list(int)): the wires the error acts on.
    
    Returns:
        (tuple(tensor, tensor)): the separate probability distributions over the 0th wire (|psi>)
        and all 8 ancillary qubits in that order.
    """


dev = qml.device("default.qubit", wires=9)

@qml.qnode(dev)
def shor(state, error_type, wires):
    """A quantum circuit that implements Shor's 9-qubit code

    Args:
        state (tensor): a numpy array representing a 1-qubit state: alpha |0> + beta |1>
                        This is used to initialize the 0th wire with qml.QubitStateVector
        error_type (str): for example, XX, YY, XZ, YZ.
        wires (list(int)): the wires the error acts on.

    Returns:
        (tuple(tensor, tensor)): the separate probability distributions over the 0th wire (|psi>)
        and all 8 ancillary qubits in that order.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    qml.CNOT(wires=[0,3])
    qml.CNOT(wires=[0,6])

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=3)
    qml.Hadamard(wires=6)

    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[3,4])
    qml.CNOT(wires=[6,7])
    qml.CNOT(wires=[0,2])
    qml.CNOT(wires=[3,5])
    qml.CNOT(wires=[6,8])

    # apply the error
    for err in error(error_type=error_type, wires=wires):
        err

    ##################
    # YOUR CODE HERE #
    ##################
    qml.CNOT(wires=[0,1])
    qml.CNOT(wires=[3,4])
    qml.CNOT(wires=[6,7])
    qml.CNOT(wires=[0,2])
    qml.CNOT(wires=[3,5])
    qml.CNOT(wires=[6,8])

    qml.Toffoli(wires=[2, 1, 0])
    qml.Toffoli(wires=[5, 4, 3])
    qml.Toffoli(wires=[8, 7, 6])

    qml.Hadamard(wires=0)
    qml.Hadamard(wires=3)
    qml.Hadamard(wires=6)

    qml.CNOT(wires=[0,3])
    qml.CNOT(wires=[0,6])

    qml.Toffoli(wires=[6,3,0])

    return qml.probs(wires=0), qml.probs(wires=range(1, 9))



# Codercise E.3.3.
def decoded(state, error_type, wires):
    """Tells us whether the state was decoded by Shor's code
    
    Args:
        state (tensor): a numpy array representing a 1-qubit state: alpha |0> + beta |1>
        error_type (str): for example, XX, YY, XZ, YZ.
        wires (list(int)): the wires the error acts on.
    
    Returns:
        (bool): True if state is decoded successfully, False if not. 
    """
    ##################
    # YOUR CODE HERE #
    ##################
    prob0 = shor(state, error_type, wires)[0]

    # Check if the probability of |0> state is above a threshold (e.g., 0.9)
    # If it is, then consider the state as decoded successfully
    threshold = 0.5
    if prob0[0] >= threshold:
        return True
    else:
        return False
        
        
state = random_state()

single_qubit_errors = [["X", [i]] for i in range(9)]
single_qubit_errors += [["Y", [i]] for i in range(9)]
single_qubit_errors += [["Z", [i]] for i in range(9)]

decoded_list = []

for err in single_qubit_errors:
    decoded_list.append(decoded(state, *err))

print(decoded_list)



# Codercise E.3.4.a.

def find_the_one(syndrome):
    """Finds the entry in the error syndrome that is equal to 1.

    Args:
        syndrome (tensor): the output of the shor function

    Returns:
        (int): the index of the syndrome vector that is equal to 1. For example, 
        if syndrome = [0, 0, 1, 0], then this function would return 2.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    index = np.nonzero(syndrome)[0]  # Find the indices where the error syndrome is equal to 1
    # np.where cannot use here???

    return index
 






# Codercise E.3.5.

state = random_state()

xxzz_error_0458 = ["XXZZ", [0, 4, 5, 8]]
xxyyzz_error_371820 = ["XXYYZZ", [3, 7, 1, 8, 2, 0]] # Put your code here
xyzxyzxyz_error_012345678 = ["XYZXYZXYZ", [0, 1, 2, 3, 4, 5, 6, 7, 8]] # Put your code here

errors = [xxzz_error_0458, xxyyzz_error_371820, xyzxyzxyz_error_012345678]

decoded_list = []

for err in errors:
    decoded_list.append(decoded(state, *err))

print(decoded_list)

