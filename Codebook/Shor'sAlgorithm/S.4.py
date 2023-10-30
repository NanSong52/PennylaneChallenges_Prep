



def is_not_one(x, N):
    """Determine if x is not +- 1 modulo N.
    
    Args:
        N (int): Modulus of the equivalence.
        x (int): Integer to check if it is different from +-1 modulo N.
        
    Returns:
        bool: True if it is different, False otherwise.
    """
    
    ##################
    # YOUR CODE HERE #
    ##################
    if x != 1%N and x != -1%N:
        return True
    else:
        return False


print("3 and 12 are coprime numbers: ", is_coprime(3,12))
print("5 is odd: ", is_odd(5))
print("4 is not one mod 5: ",is_not_one(4,5))


def shor(N):
    """Return the factorization of a given integer.
   
    Args:
       N (int): integer we want to factorize.
    
    Returns:
        array[int]: [p,q], the prime factors of N.
    """
        
    ##################
    # YOUR CODE HERE #
    ##################
    a = np.random.randint(2,N-2)
    if is_coprime(a,N):
        U = get_matrix_a_mod_N(a,N)
        r = get_period(U,N)
        if is_odd(r) is False:
            x = a**(r/2)
            if is_not_one(x,N) is False:
                p = np.gcd(x-1,N)
                q = np.gcd(x+1,N)
                return p,q
            else:
                return shor(N)
        else:
            return shor(N)
    else: 
        p = np.gcd(a,N)
        q = N/p
    return p,q

print(shor(21))
