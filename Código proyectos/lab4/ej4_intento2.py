import numpy as np
import matplotlib.pyplot as plt
from math import e

datos = np.loadtxt('covid_italia.csv', delimiter=",",dtype=str)

y = datos[:, 1].astype(int)
x = np.array(range(1, len(y)+1))

xx = x
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




plt.plot(x, y, "o")
plt.plot(x, a00*e**(a1*x), label="Ajuste")




plt.legend()


plt.show()