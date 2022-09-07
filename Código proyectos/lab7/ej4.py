import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = np.array([-7,-4,-3])
A_ub = np.array([  [1,2,2], 
                [2,1,2] 
])
b_ub = np.array([30,45])

solucion = linprog(c, A_ub, b_ub)

print("Hay que fabricar", round(solucion.x[0]), "rubia,", round(solucion.x[1]), "negra y", round(solucion.x[2]), "de baja graduacion")

