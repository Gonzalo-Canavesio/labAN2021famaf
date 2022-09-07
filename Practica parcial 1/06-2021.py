import numpy as np
import math

def rbisec(fun,I,err,mit):
    a = I[0]
    b = I[1]
    u = fun(a)
    v = fun(b)
    hx = []
    hf = []
    if (u*v > 0):
        return("No se puede asegurar la hipotesis del metodo de biseccion en el intervalo dado")
    elif u==0:
        hx.append(a)
        hf.append(u)
        return(hx,hf)
    elif v==0:
        hx.append(b)
        hf.append(v)
        return(hx,hf)
    if u > v:
        u,v = v,u
    for _ in range(mit):
        c = a + (b-a)/2
        w = fun(c)
        hx.append(c)
        hf.append(w)
        if(abs(w)<err):
            break   
        if (u*w < 0):
            b = c
            v = w
        else:
            a = c
            u = w
    return (hx,hf)

def rnewton(fun,x0,err,mit):
    f,df = fun(x0)
    hx = []
    hf = []
    hx.append(x0)
    hf.append(f)
    if abs(f) < err:
        return hx,hf
    for _ in range(mit):
        if df == 0:
            return "No se puede realizar el metodo, la derivada es 0"
        x1 = x0 - f / df    
        f,df = fun(x1)
        hx.append(x1)
        hf.append(f)
        if abs(f) < err or abs(x1 - x0) / x1 < err :
            return hx,hf
        x0 = x1
    return hx,hf

aux_fun1 = lambda x : (x/np.cos(x)**2-2*np.sin(x)/np.cos(x))/ x**3
aux_fun2 = lambda x : (((x/np.cos(x)**2)-(2*np.sin(x)/np.cos(x)))/ x**3 , (6*np.tan(x)+2*x*(1/np.cos(x)**2)*(-2+x*np.tan(x)))/x**4) # (funcion dependiente de x, derivada de la funcion)
hx, hy = rbisec(aux_fun1,[0.1,np.pi/2],1e-6,100)
hx1, hy1 = rnewton(aux_fun2,np.pi/2-1,1e-6,100)
print(f"(Realizado con método de bisección) El mínimo de la función f está en el punto {hx[-1]}")
print(f"(Realizado con método de newton) El mínimo de la función f está en el punto {hx1[-1]}")

def ripf(fun,x0,err,mit):
    hx = []
    hx.append(x0)
    for _ in range(mit):
        x = fun(x0)
        hx.append(x)
        print(x)
        if abs(x - x0) < err:
            return hx
        x0 = x
    return hx

def molino(e,v):
    aux_fun = lambda d : (e - (0.01328 * math.pow(v,3) * math.pow(d,2)),- (0.01328 *2* math.pow(v,3) * d))
    hx, hy = rnewton(aux_fun, 5, 1e-9, 100) #Uso el método de Newton porque el método de punto fijo no se puede aplicar en este intervalo
    y = hx[-1]
    return y

print(f"El diametro del molino debe ser de {molino(1000,300/36)}")