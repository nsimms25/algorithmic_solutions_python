def factorial(n):
    '''
    Returns the factorial of the input integer:
        n * (n - 1) * (n - 2) * ... * 2 * 1
    Parameters
    ----------
    n: {int} number to compute factorial of (must be greater than 0)

    Returns
    -------
    n!: {int} factorial of n

    '''
    num = 1
    for i in range(1,n+1):
        num = num * i
    
    return num
