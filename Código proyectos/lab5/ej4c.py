from ej1 import *

cant_subintervalos = [10,205]

aux = lambda x : (1+x**2)**(3/2)

print("La integral calculada con la regla compuesta de simpson es", intenumcomp(aux,0,1,cant_subintervalos[0],"simpson"))
print("La integral calculada con la regla compuesta del trapecio es", intenumcomp(aux,0,1,cant_subintervalos[1],"trapecio"))