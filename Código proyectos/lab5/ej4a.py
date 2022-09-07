from ej1 import *
import numpy as np

cant_subintervalos = [8,130]

aux = lambda x : x*np.exp(-x)

print("La integral calculada con la regla compuesta de simpson es", intenumcomp(aux,0,1,cant_subintervalos[0],"simpson"))
print("La integral calculada con la regla compuesta del trapecio es", intenumcomp(aux,0,1,cant_subintervalos[1],"trapecio"))