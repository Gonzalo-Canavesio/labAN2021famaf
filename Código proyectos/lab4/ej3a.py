import numpy as np
import matplotlib.pyplot as plt
from math import e

datos = np.loadtxt('datos3a.dat')

x = datos[0,:]
y = datos[1,:]
xx = [np.log(i) for i in x]
yy = [np.log(i) for i in y]
c5 = len(xx)


unos = np.ones(c5)
c1 = np.dot(xx, xx)
c2 = np.dot(xx, unos)
c3 = np.dot(xx, yy)
c4 = np.dot(yy, unos)

a0 = (c1 * c4 - c3 * c2)/ ( c5 * c1 - c2**2)

a1 = (c5 * c3 - c2 * c4) / (c5 * c1 - c2**2)

a00 = e**a0

x1 = np.linspace(1, 5, 200)
y1 = [a00*xi**a1 for xi in x1]
plt.plot(x, y, 'o')
plt.plot(x1, y1,label="Aproximación lineal")
plt.legend()
plt.show()