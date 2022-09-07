import math
import numpy as np
import matplotlib.pyplot as plt
from ej1 import *

def elegir_intervalo(x):
    N = math.ceil(x*10)
    N = 1 if N<1 else N
    return N

def senint(x):
    aux = lambda x : np.cos(x)

    y = [intenumcomp(aux,0,i,elegir_intervalo(i), "trapecio") for i in x]
    return y

x = [i*0.5 for i in range(0,math.ceil(4*np.pi))]
y = senint(x)

plt.plot(x, y, label="seint")
plt.plot(x, np.sin(x), label="seno")
plt.legend()

plt.show()