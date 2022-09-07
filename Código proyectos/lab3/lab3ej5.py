import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

data = np.loadtxt('datos_aeroCBA.dat')
auxx = data[:,0]
auxy = data[:,1]
x = []
y = []
for i in range (0,len(auxx)):
    if not np.isnan(auxy[i]):
        x.append(auxx[i])
        y.append(auxy[i])

# interp1d nos devuelve una función que podemos evaluar
f = interpolate.interp1d(x, y, kind='cubic', fill_value='extrapolate')
xnew = [i for i in range(1957,2018)]
ynew = f(xnew)

plt.plot(xnew, ynew)
plt.plot(x, y, 'o')
plt.show()