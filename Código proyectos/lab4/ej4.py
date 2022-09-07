import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('covid_italia.csv', delimiter=",",dtype=str)

y = datos[:, 1].astype(int)
x = np.array(range(1, len(y)+1))

yy = np.log(y)

b, aa = np.polyfit(x, yy, 1)

a = np.exp(aa)

plt.plot(x, y, "o", label="Casos covid Italia")
plt.plot(x, a*np.exp(b*x), label="Ajuste")
plt.legend()


plt.show()