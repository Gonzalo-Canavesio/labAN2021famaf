import numpy as np
from math import sqrt
import scipy.integrate

def pendulo(l,a):
    a *= np.pi / 180
    integral = lambda k :  1/(sqrt(1-np.sin(a/2)**2*np.sin(k)**2))
    return 4 * sqrt(l/(9.8)) * scipy.integrate.quad(integral,0,np.pi/2)[0]

print(pendulo(20,45))
print(pendulo(20,0))
print(pendulo(90,0))
print(pendulo(47,0))
print(pendulo(12,60))