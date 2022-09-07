from mpmath import sec
import math
from ej3 import *


def lab2ej8():
	aux_fun = lambda x : ((x * (sec(x))**2 - 2 * math.tan(x))/x**3, (6 *math.tan(x) + 2 *x *(sec(x))**2 * (-2 + x* math.tan(x)))/x**4)
	hy, hu = rnewton(aux_fun, 1, 1e-9, 100)
	y = hy[-1]
	return y

print(lab2ej8())