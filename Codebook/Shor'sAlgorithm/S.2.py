# S.2 Classical factorization



def nontrivial_square_root(m):
    """Return the first nontrivial square root modulo m.
    
    Args:
        m (int): modulus for which want to find the nontrivial square root

    Returns:
        int: the first nontrivial square root of m
    """
    
    ##################
    # YOUR CODE HERE #
    ##################
    for i in range(2,m):
        if i**2 % m == 1:
            break
    return i
        
print(nontrivial_square_root(391))


 
def factorization(N):
    
    """Return the factors of N.
    
    Args:
        N (int): number we want to factor.

    Returns:
        array[int]: [p,q] factors of N.
    """
    ##################
    # YOUR CODE HERE #
    ##################
    x = nontrivial_square_root(N)
    p = np.gcd(x-1,N)
    q = np.gcd(x+1,N)
    return p,q


N = 391
p, q = factorization(N)
print(f"{N} = {p} x {q}")









