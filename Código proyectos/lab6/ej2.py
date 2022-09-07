import numpy as np
from  ej1 import soltrsup #Aqui importe su soltrsup

#Opción 1 - Calcular los ceros de la matriz
def egauss(A_, b_):

    A = A_.copy()
    b = b_.copy()
    n = A.shape[0]

    for k in range(n-1):
        for i in range(k+1,n):
            if A[k,k] == 0:
                print('El elemento a_kk es igual a cero.')
                return None
            
            m = A[i,k] / A[k,k]

            for j in range(k,n):
                A[i,j] = A[i,j] - m * A[k,j]    
            b[i] = b[i] - m * b[k]

    return A, b

def soleg(A,b):
    U, y = egauss(A,b)
    x = soltrsup(U,y)
    return x

""" def test():
    U = np.array([
        [3, 7, 2],        
        [4, 4, 4],
        [0, 2, 1],
    ], dtype="float"
    )
    b = np.array([1, 2, 3], dtype="float")
    print(soleg(U, b))

test() """