import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos1a.dat')

x = datos[:,0]
y = datos[:,1]

c5 = len(x)


unos = np.ones(c5)
c1 = np.dot(x, x)
c2 = np.dot(x, unos)
c3 = np.dot(x, y)
c4 = np.dot(y, unos)

a0 = (c1 * c4 - c3 * c2)/ ( c5 * c1 - c2**2)

a1 = (c5 * c3 - c2 * c4) / (c5 * c1 - c2**2)

x1 = np.linspace(0, 5, 200)
y1 = [a0+a1*xi for xi in x1]
plt.scatter(x, y, c="r")
plt.plot(x1, y1,label="Aproximación lineal")
plt.legend()
plt.show()