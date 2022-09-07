from ej3 import *


def fun_lab2ej4(a):
    if a <= 0:
        return "El numero a debe ser mayor que 0"
    aux_fun = lambda x : (x**3-a, 3*x**2)
    return rnewton(aux_fun,a,10e-6,200)

print(fun_lab2ej4(13))