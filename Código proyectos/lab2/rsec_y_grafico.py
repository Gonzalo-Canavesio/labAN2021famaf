import numpy as np
import matplotlib.pyplot as plt

def rsec(fun,x0,x1,err,mit):
    f0 = fun(x0)
    f1 = fun(x1)
    hx = []
    hf = []
    hx.append(x1)
    hf.append(f1)
    if abs(f1) < err:
        return hx,hf
    for _ in range(mit):
        if abs(f0 < f1):
            x0,x1,f0,f1 = x1,x0,f1,f0
        s = (x1 - x0)/(f1 - f0)
        x1 = x0
        f1 = f0
        x0 = x0 - f0 * s
        f0 = fun(x0)
        hx.append(x1)
        hf.append(f1)
        if abs(x1 -x0) < err:
            break
    return (hx,hf)


x = np.linspace(0, 10, 100)
y = [funcion(xi) for xi in x] # Funcion es la funcion que aproxima el valor de los y
plt.subplot(3,1,1)
plt.plot(x, y,label="Funcion")
plt.legend()
plt.show()

x = np.linspace(0, 10, 100)
plt.plot(x, funcion(x), label="funcion") # Funcion es la funcion que te da el valor de los y
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()
