import numpy as np

def xtx_product(X):
    """
    Given a matrix X, calculate the inner product X^T X, where the ^T
    operator denotes the transpose.

    Parameters
    ----------
    X: NumPy array size of (n, m)

    Returns
    -------
    NumPy Array of size (m, m)
    """
    Xt = X.transpose()

    return np.dot(Xt, X)
