from lab3ej1 import ilagrange
from lab3ej2 import inewton
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = [-3,-2,-1,0,1,2,3]
f = [1,2,5,10,5,2,1]
inter = interpolate.interp1d(x,f, kind='cubic') 

xgraf = np.linspace(-3,3,100)
ylagrange = ilagrange(x,f,xgraf)
ynewton = inewton(x,f,xgraf)
yscipy = [inter(i) for i in xgraf]

plt.subplot(3,1,1)
plt.plot(xgraf,ylagrange, label="Lagrange")
plt.subplot(3,1,2)
plt.plot(xgraf,ynewton, label="Newton")
plt.legend()
plt.subplot(3,1,3)
plt.plot(xgraf,yscipy, label="Scipy")
plt.legend()

plt.show()

# Scipy genera un polinomio mas suave para interpolar los valores de la funcion