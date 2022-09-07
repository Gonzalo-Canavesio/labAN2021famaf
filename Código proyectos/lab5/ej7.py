from ej1 import *
import numpy as np

def s(fun,a,b):
    return (fun(a)+fun(b)+4*fun((a+b)/2))*(b-a)/6


def cuadratura_adaptativa(fun,int,error):
    a = int[0]
    b = int[1]
    c = (a + b) / 2
    q = s(fun,a,b)
    q1 = s(fun,a,c)
    q2 = s(fun,c,b)
    e = abs(q-q1-q2)/15
    if(e>=error):
        q1 = cuadratura_adaptativa(fun,[a,c],error/2)
        q2 = cuadratura_adaptativa(fun,[c,b],error/2)
    return q1 + q2

f = lambda x : x*np.exp(-(x**2))

print(cuadratura_adaptativa(f,[0,1],10e-5))
print(intenumcompsimpson(f,0,1,10))