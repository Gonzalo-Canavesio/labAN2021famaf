from ej5 import jacobi,gseidel

import numpy as np
A = np.array([
    [3,1,1],
    [2,6,1],
    [1,1,4],
], dtype="float"
)
b = np.array([5,0,6], dtype="float")

A_ = np.array([
    [5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10],
], dtype="float"
)
b_ = np.array([23,32,33,31], dtype="float")

j1 = jacobi(A,b,1e-11,500)
g1 = gseidel(A,b,1e-11,500)

j2 = jacobi(A_,b_,1e-4,500)
g2 = gseidel(A_,b_,1e-4,500)

print(f"La solución de (1) con el metodo de Jacobi es {j1[0]}, y se alcanza con {j1[1]} iteraciones")
print(f"La solución de (1) con el metodo de Gauss Seidel es {g1[0]}, y se alcanza con {g1[1]} iteraciones")
print(f"La solución de (2) con el metodo de Jacobi es {j2[0]}, y se alcanza con {j2[1]} iteraciones")
print(f"La solución de (2) con el metodo de Gauss Seidel es {g2[0]}, y se alcanza con {g1[1]} iteraciones")