def get_divisors(n):
    '''
    This function calculates and returns all of the divisors of n, between 1 and
    n, inclusive.

    Parameters
    ----------
    n: {int}

    Returns
    -------
    divisors: {list} all divisors of n in order from smallest to largest
    '''
    divisors = []
    for i in range(1,n):
        if(n % i == 0):
            divisors.append(i)
    
    divisors.append(n)

    return divisors
