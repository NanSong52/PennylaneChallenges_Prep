from pennylane import numpy as np


# Fourier Transformation

# try to use fft from numpy package!
# fft: convert coefficient repr to value repr
def coefficients_to_values(coefficients):
    """Returns the value representation of a polynomial
    
    Args:
        coefficients (array[complex]): a 1-D array of complex 
            coefficients of a polynomial with 
            index i representing the i-th degree coefficient

    Returns: 
        array[complex]: the value representation of the 
            polynomial 
    """
    ##################
    # YOUR CODE HERE #
    ################## 
    value = np.fft.fft(coefficients)
    return value

A = [4, 3, 2, 1]

print(coefficients_to_values(A))


# ifft (convert value repr to coefficient repr) inverse of fft
def values_to_coefficients(values):
    """Returns the coefficient representation of a polynomial
    
    Args:
        values (array[complex]): a 1-D complex array with 
            the value representation of a polynomial 

    Returns: 
        array[complex]: a 1-D complex array of coefficients
    """
    
    ##################
    # YOUR CODE HERE #
    ################## 
    coff = np.fft.ifft(values)
    return coff


A = [10.+0.j,  2.-2.j,  2.+0.j,  2.+2.j]
print(values_to_coefficients(A))


# 2**(power_int)
def nearest_power_of_2(x):
    """Given an integer, return the nearest power of 2. 
    
    Args:
        x (int): a positive integer

    Returns: 
        int: the nearest power of 2 of x
    """
    ##################
    # YOUR CODE HERE #
    ################## 
    power = np.log2(x)
    power_int = np.ceil(power)
    return int(2**power_int)


# hard question here: 

def fft_multiplication(poly_a, poly_b):
    """Returns the result of multiplying two polynomials
    
    Args:
        poly_a (array[complex]): 1-D array of coefficients 
        poly_b (array[complex]): 1-D array of coefficients 

    Returns: 
        array[complex]: complex coefficients of the product
            of the polynomials
    """
    ##################
    # YOUR CODE HERE #
    ################## 

    # Calculate the number of values required
    n_a = len(poly_a)
    n_b = len(poly_b)
    n_c = n_a + n_b -1
    # Figure out the nearest power of 2
    points = nearest_power_of_2(n_c)
    # Pad zeros to the polynomial
    # add 0s after poly a array
    #  0 : the number of 0s to be added before the existing coefficients in the array
    poly_a_pad = np.pad(poly_a, (0,points - n_a))
    poly_b_pad = np.pad(poly_b, (0,points - n_b)) 
    # Convert the polynomials to value representation 
    poly_a = coefficients_to_values(poly_a_pad)
    poly_b = coefficients_to_values(poly_b_pad)
    # Multiply
    poly_c = np.multiply(poly_a,poly_b)
    # Convert back to coefficient representation
    coeff_repr = values_to_coefficients(poly_c)
    return coeff_repr
