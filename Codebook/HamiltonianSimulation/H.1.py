#  H.1 Simulating Nature

input = [1, 1, 0] # MODIFY EXAMPLE
print("The result of applying the secret box to ", input, "is ")
# We will secretly apply the function and return the result!

def deterministic_box(bits):
    """Guess the secret deterministic rule.
    
    Args:
        bits (list[int]): A list of bits representing an initial condition.
         
    Returns: 
        list[int]: The output bits measured after deterministic evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
 
    return bits[1:]+ [bits[0]] # MODIFY THIS



input = 0 # MODIFY EXAMPLE

trials = 100 # INCREASE TRIALS TO IMPROVE APPROXIMATION
print("On input", input, "the approximate probability distribution is")
# We will secretly apply the function and return the result!

def random_box(bit):
    """Guess the secret random rule.
    
    Args:
        bit (int): A bit representing the initial condition.
         
    Returns: 
        int: The output bit measured after random evolution.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    return np.random.choice(2) # output: 0 / 1



dev = qml.device("default.qubit", wires=1)

input = 0 # MODIFY EXAMPLE
reps = 1
print("The probability distribution after applying the secret box to ", input)
print("a total of ", reps, "time(s) is ")
# We will secretly apply the function and return the result!

@qml.qnode(dev)
def quantum_box(bit, reps):
    """Implements the secret quantum rule on a single (qu)bit.
    
    Args:
        bit (int): A bit representing an initial condition.
        reps (int): Number of times gate is repeated.

    Returns:
        list[float]: The output probability distribution.
    """
    if bit == 1:
        qml.PauliX(wires=0)
    for _ in range(reps):
        ##################
        # YOUR CODE HERE #
        ##################
        qml.Hadamard(wires=0)
    return qml.probs(wires=0)













