# E.1 Got errors?


# Codercise E.1.1. 
def encode(b):
    """Returns three copes of Alice's bit b.
    
    Args:
        b (int): Alice's bit she wants to send to Bob. Can be 0 or 1. 
         
    Returns: 
        list(int): [b, b, b]
    """
    return [b, b, b]

def noisy_channel(b, p):
    """Returns a three-bit codeword message that Bob receives through a noisy channel.
    
    Args:
        b (int): Alice's bit she wants to send to Bob. Can be 0 or 1. 
        p (float): The probability that a bit is flipped. 
         
    Returns: 
        list(int): The three-bit codeword that Bob receives. It might be different
        than what Alice intended to send!
    """
    alice_sends = encode(b) # Alice sends this to Bob
    ##################
    # YOUR CODE HERE #
    ##################
    codeword = []
    for i in alice_sends:
        # Generate a random number between 0 and 1
        random_prob = np.random.uniform(0,1)

        # Check if the random number is less than the probability p
        # If yes, flip the bit by subtracting it from 1
        if random_prob < p:
            noisy_bit = 1 - i
        else:
            noisy_bit = i

        # Append the noisy bit to the noisy_codeword list
        codeword.append(noisy_bit)

    return codeword








#Codercise E.1.2. 
def decode(codeword):
    """Executes Bob's decoding procedure.

    Args:
        codeword (list(int)): The message Bob receives (a 3-bit string). 

    Returns:
        (int): A 0 or 1 — Bob's guess at what Alice's bit was.
    """
    """Executes Bob's decoding procedure."""
    # Count the number of zeros and ones in the codeword
    count_zeros = codeword.count(0)
    count_ones = codeword.count(1)

    # Return the majority vote (the bit that appears more times)
    return 0 if count_zeros >= count_ones else 1

def success(b, codeword):
    """Determines if Bob's decoding procedure is successful.

    Args:
        b (int): Alice's bit she sent to Bob. Can be 0 or 1. 
        codeword (list(int)): The message Bob receives (a 3-bit string). 
         
    Returns: 
        (bool): True/False if Bob decodes correctly/incorrectly.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    # Get Bob's guess from the decoding procedure
    bob_guess = decode(codeword)

    # Compare Bob's guess with Alice's original bit
    return bob_guess == b










#