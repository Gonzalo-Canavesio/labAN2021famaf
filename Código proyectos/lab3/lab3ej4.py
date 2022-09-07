from lab3ej2 import *
import numpy as np
import matplotlib.pyplot as plt

f = lambda x : 1/(1+25*x**2)

puntos = np.linspace(-1,1,200)
for n in range(1,16):
    plt.subplot(3,5,n)
    xp = [2*(i-1)/n -1 for i in range(1,n+2)]
    yp = [f(xi) for xi in xp]
    plt.plot(xp,yp, label="p")
    xq = [np.cos(((2*i+1)/(2*n+2))*np.pi) for i in range(0,n+1)]
    yq = [f(xi) for xi in xq]
    plt.plot(xq,yq, label="q")
    y = [f(xi) for xi in puntos]
    plt.plot(puntos,y, label="f")
    plt.title(f"Grafico con $n={n}$")
    plt.legend()

plt.show()