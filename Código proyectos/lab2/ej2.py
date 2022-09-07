import numpy as np
import matplotlib.pyplot as plt
from ej1 import *


def fun_lab2ej2a(x):
    return (np.tan(x) - 2*x)
hx, hy = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)
# 1.1655609130859372 es la primera solución que cumple que es menor a 10^(−5) y se obtiene en 16 iteraciones utilizando el intervalo [0.8,1.4]


def fun_lab2ej2b(x):
    return x**2 - 3
print(hx[-1])
# Una solución encontrada es 1.7320489883422852


x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
k = np.linspace(0, 10, 1000)
# Hago un grafico de la función a
plt.plot(x, fun_lab2ej2a(x), label="$2x = tan(x)$")
# Hago un gráfico de la función b
plt.plot(x, fun_lab2ej2b(x), label="$x^2-3$")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.ylim(-25, 25)
plt.title("Funciones")
plt.legend()
plt.show()

plt.plot(k, fun_lab2ej2a(k), label="$2x = tan (x)$")
plt.plot(k, fun_lab2ej2b(k), label="$x^2-3$")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.ylim(-25, 25)
plt.title("Funciones")
plt.legend()
plt.show()