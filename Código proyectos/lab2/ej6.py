from ej5 import *


def fun_lab2ej6(x):
    return 2**(x-1)

hx = ripf(fun_lab2ej6, 0, 1e-5, 100)
print(hx)
# Converge a 1 y converge para x <= 2