from ej2 import soleg
import numpy as np
from ej3 import sollu

A = np.array([
    [4, -1, 0, -1, 0, 0],
    [-1, 4, -1, 0, -1, 0],
    [0, -1, 0, 4, -1, 0],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4],
], dtype="float"
)
b = np.array([1,1,1,0,0,0], dtype="float")
b_ = np.array([1,1,1,1,1,1], dtype="float")    
print(sollu(A, b))
print(soleg(A, b))
print(sollu(A, b_))
print(soleg(A, b_))