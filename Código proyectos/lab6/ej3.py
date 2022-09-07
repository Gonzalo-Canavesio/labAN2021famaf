from scipy.linalg import lu
from ej1 import soltrinf, soltrsup

def sollu(A,b):
	P,L,U = lu(A)
	y = soltrinf(L,P.T @ b)
	x = soltrsup(U,y)
	return x

""" def test_sollu():
    A = np.array([
        [3, 1, 1],
        [2, 6, 1],
        [1, 1, 4],
    ], dtype="float"
    )
    b = np.array([5, 9, 6], dtype="float")
    print(sollu(A, b)) # Nos deberia dar [1, 1, 1]

test_sollu() """