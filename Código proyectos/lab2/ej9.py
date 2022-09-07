from ej1 import rbisec
from ej3 import *
import math

def lab2ej9(e,v):
    aux_fun = lambda d : (e - (0.01328 * math.pow(v,3) * d**2) , -2* 0.01328 * math.pow(v,3) * d)
    hy, hu = rnewton(aux_fun, 1, 1e-9, 100)
    y = hy[-1]
    return y

# E = 0.01328 * D^2 * V^3, donde E es la energı́a generada, D es el diámetro en metros y V es la velocidad del viento en m/s.
# Usar el método de Newton para determinar el diámetro del molino si se desea generar 500W de energı́a eléctrica cuando la velocidad del viento es de 24 km/h.

print(lab2ej9(500,240/36))