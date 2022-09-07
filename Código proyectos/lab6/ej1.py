import numpy as np

def soltrinf(A, b):
    n = A.shape[0]
    x = b
    if np.prod(np.diag(A)) == 0:
        print("La matriz es no singular")
        return None    
    for idx in range(n):
        for jdx in range(idx):
           x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

def soltrsup(A, b):
    n = A.shape[0]
    x = b
    if np.prod(np.diag(A)) == 0:
        print("La matriz es no singular")
        return None
    for idx in range(n-1, -1, -1):
        for jdx in range(n-1, idx, -1):
            x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

""" def test_soltrsup():
    U = np.array([
        [1, 1, 1],
        [0, 1, 1],
        [0, 0, 1],
    ], dtype="float"
    )
    b = np.array([3, 2, 1], dtype="float")
    print(soltrsup(U, b)) # Nos deberia dar [1, 1, 1]

def test_soltrinf():
    U = np.array([
        [1, 0, 0],        
        [1, 1, 0],
        [1, 1, 1],
    ], dtype="float"
    )
    b = np.array([1, 2, 3], dtype="float")
    print(soltrinf(U, b)) # Nos deberia dar [1, 1, 1]

test_soltrsup()
test_soltrinf() """