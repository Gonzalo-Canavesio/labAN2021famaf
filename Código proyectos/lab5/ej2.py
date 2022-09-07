import numpy as np
from ej1 import *

cant_subintervalos = [4,10,20]
reglas = ["simpson", "trapecio", "pm"]

aux = lambda x : np.exp(-x)

valor_exacto = - aux(1) + aux(0)
print(intenumcomp(aux,0,1,4,"simpson"))
print(valor_exacto)
for r in reglas:
    for n in cant_subintervalos:
        print(f"El error absoluto al calcular la integral con la regla compuesta de {r} con {n} subintervalos es {abs(valor_exacto - intenumcomp(aux,0,1,n,r))}")