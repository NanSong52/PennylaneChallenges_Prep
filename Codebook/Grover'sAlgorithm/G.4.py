# G.4 Steps and speedups


def grover_iter(combo, num_steps):
    """Run Grover search for a given secret combination and a number of iterations.
    
    Args:
        combo (list[int]): The secret combination, represented as a list of bits.
        num_steps (int): The number of Grover iterations to perform.

    Returns: 
        array[float]: Probability for observing different outcomes.
    """
    n_bits = len(combo)
    query_register = list(range(n_bits))
    aux = [n_bits]
    all_wires = query_register+aux
    dev = qml.device('default.qubit', wires=all_wires)

    @qml.qnode(dev)
    def inner_circuit():
        ##################
        # YOUR CODE HERE #
        ##################
        # IMPLEMENT THE GROVER CIRCUIT
        qml.PauliX(wires= aux)
        hadamard_transform(all_wires)
        for i in range(num_steps):
            oracle(combo)
            diffusion(n_bits)
        return qml.probs(wires=query_register)
    
    return inner_circuit()

n_list = range(3,7)
opt_steps = []

for n_bits in n_list:
    combo = "0"*n_bits # A simple combination
    step_list = range(1,10) # Try out some large number of steps
    ##################
    # YOUR CODE HERE #
    ##################
    m = []
    for i in step_list:
        m.append(grover_iter(combo,i)[0])
    
    opt_steps.append(local_max_arg(m))
    
    
    
    
print("The optimal number of Grover steps for qubits in", [3,4,5,6], "is", opt_steps, ".")


grad = 0.5
intercept = -0.47
# SUBMIT TO PLOT GRAPH



