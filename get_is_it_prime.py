def is_prime(n):
    '''
    Return True if the input is prime, False otherwise
    Parameters
    ----------
    n: {int} input integer

    Returns
    -------
    is_prime: {bool} whether n is prime
    '''
    prime = True

    for i in range(2,n):
        if(n % i == 0):
            prime = False
    
    return prime
