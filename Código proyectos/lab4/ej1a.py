from stringprep import c22_specials
from xml.etree.ElementTree import C14NWriterTarget
import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos1a.dat')

x = datos[:,0]
y = datos[:,1]

c1 = sum(i**2 for i in x)
c2 = sum(i for i in x)
c3 = 0
for d in datos:
    c3 += d[0]*d[1]
c4 = sum(i for i in y)
c5 = len(x)

a0 = (c1 * c4 - c3 * c2)/ ( c5 * c1 - c2**2)

a1 = (c5 * c3 - c2 * c4) / (c5 * c1 - c2**2)

x1 = np.linspace(0, 5, 200)
y1 = [a0+a1*xi for xi in x1]
plt.scatter(x, y, c="r")
plt.plot(x1, y1,label="Aproximación lineal")
plt.legend()
plt.show()