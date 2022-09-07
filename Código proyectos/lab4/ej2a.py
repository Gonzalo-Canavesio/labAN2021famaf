import numpy as np
import matplotlib.pyplot as plt


xi = np.linspace(0,1,50)
yi = np.arcsin(xi)

x = np.linspace(0,1,200)

for i in range(0,6):
    aprox = np.polyfit(xi, yi, i)
    plt.plot(xi, np.polyval(aprox, xi),label="Polinomio de grado" + str(i))
    suma_residuos = 0
    for k in range(0,50):
        suma_residuos += abs(yi[k]-np.polyval(aprox, xi[k]))
    print("La suma de los residuos en el polinomio de grado",i,"es",suma_residuos)

plt.plot(xi,yi,'o')
plt.legend()
plt.show()