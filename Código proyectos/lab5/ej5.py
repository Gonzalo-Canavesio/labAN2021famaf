from math import sqrt
import scipy.integrate
import numpy as np

aux1 = lambda x : np.exp(-(x**2))
aux2 = lambda x : x**2 * np.log(x+sqrt(x**2+1))

print("La integral del ejercicio a es", scipy.integrate.quad(aux1,-np.inf,np.inf)[0])
print("La integral del ejercicio b es", scipy.integrate.quad(aux2,0,2)[0])