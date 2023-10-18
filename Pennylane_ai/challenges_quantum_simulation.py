import json
import numpy as np

def initialize_state():
    """
    Prepare a qubit in state |0>.

    Returns:
        array[float]: the vector representation of state |0>.
    """
    return np.array([1, 0])
    # PREPARE THE STATE |0>


def apply_u(U, state):
    """
    Apply the quantum operation U on the state

    Args:
        U (np.array(array(complex))): A (2,2) numpy array with complex entries 
        representing a unitary matrix.
        state (np.array(complex)): A (2,) numpy array with complex entries 
        representing a quantum state.
    
    Returns:
        (np.array(complex)): The state vector after applying U to state.
    """


    # Put your code here #
    return state @ U


def measure_state(state, num_meas):
    """
    Measure a quantum state num_meas times.

    Args:
        state (np.array(complex)): A (2,) numpy array with complex entries
        representing a quantum state.
        num_meas(float): The number of computational basis measurements on state.
        
    Returns:
        (np.array(int)) A (num_meas,) numpy array of zeros and ones, representing
        measurement outcomes on the state
    """
    mesurements = np.zeros(num_meas)
    for i in range(num_meas):
        # Perform a single measurement by sampling from the probability distribution
        # Defined by the squared magnitudes of the state amplitudes.
        mesurements[i] = np.random.choice([0, 1], p=[abs(state[0])**2, abs(state[1])**2])

    # Your code here #
    return mesurements


def quantum_algorithm(U):
    """
    Use the functions above to implement the quantum algorithm described above.

    Try and do so using three lines of code or less!

    Args:
        U (np.array(array(complex))): A (2,2) numpy array with complex entries
        representing a unitary matrix.

    Returns:
        np.array(int): the measurement results after running the algorithm 20 times
    """
    state0 = initialize_state()
    state1 = apply_u(U, state0)
    return measure_state(state1, 20)

    # PREPARE THE STATE, APPLY U, THEN TAKE 20 MEASUREMENT SAMPLES


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    np.random.seed(0)
    ins = json.loads(test_case_input)
    output = quantum_algorithm(ins).tolist()
    return str(output)


def check(solution_output: str, expected_output: str) -> None:
    
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    
    initial_state = initialize_state()

    assert isinstance(
        initial_state, np.ndarray
    ), "The output of your initialize_state function should be a numpy array"

    assert np.allclose(
        initial_state, np.array([1, 0])
    ), "The output of your initialize_state function isn't quite right"

    U_test = [[0.70710678, 0.70710678], [0.70710678, -0.70710678]]

    assert np.allclose(
        apply_u(U_test, np.array([1, 0])), [0.70710678, 0.70710678]
    ), "Your output of apply_u isn't quite right"

    sample_list = measure_state([0.70710678, 0.70710678], 100).tolist()

    assert (
        sample_list.count(0) + sample_list.count(1) == 100
    ), "Your measure_state function isn't quite right"

    sample_list_2 = quantum_algorithm(U_test).tolist()

    assert (
        sample_list_2.count(0) + sample_list_2.count(1) == 20
    ), "Your quantum_algorithm function isn't quite right"
    
    assert np.allclose(solution_output, expected_output)


# These are the public test cases
test_cases = [
    ('[[0.70710678,  0.70710678], [0.70710678, -0.70710678]]', '[1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]'),
    ('[[0.8660254, -0.5],[0.5, 0.8660254]]', '[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]')
]

# This will run the public test cases locally
for i, (input_, expected_output) in enumerate(test_cases):
    print(f"Running test case {i} with input '{input_}'...")

    try:
        output = run(input_)

    except Exception as exc:
        print(f"Runtime Error. {exc}")

    else:
        if message := check(output, expected_output):
            print(f"Wrong Answer. Have: '{output}'. Want: '{expected_output}'.")

        else:
            print("Correct!")