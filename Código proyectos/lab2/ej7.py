import math
import numpy as np
import matplotlib.pyplot as plt
from ej1 import *
from ej3 import *
from ej5 import *

def lab2ej7bisec(x):
	aux_fun = lambda y : y - math.exp(-(1-x*y)**2)
	hy, hu = rbisec(aux_fun, [0.0,2.0], 1e-5, 100)
	y = hy[-1]
	return y

def lab2ej7newton(x):
	aux_fun = lambda y : (y - math.exp(-(1-x*y)**2), 1 - math.exp(-(1-x*y)**2)*(-2*(1-x*y)*(-x)))
	hy, hu = rnewton(aux_fun, 1, 1e-9, 1000)
	y = hy[-1]
	return y

def lab2ej7ipf(x):
	aux_fun = lambda y : math.exp(-(1-x*y)**2)
	hy = ripf(aux_fun, 1, 1e-9, 1000)
	y = hy[-1]
	return y


x = np.linspace(0, 1.5, 100)
y_bisec = [lab2ej7bisec(xi) for xi in x]
y_newton = [lab2ej7newton(xi) for xi in x]
y_ipf = [lab2ej7ipf(xi) for xi in x]
plt.subplot(3,1,1)
plt.plot(x, y_bisec)
plt.ylabel("lab2ej7bisec")
plt.subplot(3,1,2)
plt.plot(x, y_newton)
plt.ylabel("lab2ej7newton")
plt.subplot(3,1,3)
plt.plot(x, y_ipf)
plt.ylabel("lab2ej7ipf")
plt.show()