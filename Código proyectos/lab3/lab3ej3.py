from lab3ej2 import *
import matplotlib.pyplot as plt

f = lambda x : 1/x

x = [xi for xi in range(1,6)]
y = [f(xi) for xi in x]
z = [24/25 + j/25 for j in range(1,102)]
fun = [f(xi) for xi in z]
p = inewton(x, y, z)

plt.plot(z, fun, label="f(x)")
plt.plot(z, p, label="p(x)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()