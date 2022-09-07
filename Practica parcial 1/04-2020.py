import numpy as np

def fibonacci(n):
    f = []
    f.append(0)
    f.append(1)
    for i in range (2,n):
        f.append(f[i-2] + f[i-1])
    return f[-1]

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

aux_fun = lambda x : (np.log(x)-1/x , (x+1)/x**2) # (funcion dependiente de x, derivada de la funcion)
hx, hy = rnewton(aux_fun,1.4,1e-6,100)
print(f"La raiz de f(x) es {hx[-1]}")

def rsteff(fun,x0,err,mit):
    hx = []
    hf = []
    hx.append(x0)
    hf.append(fun(x0))
    if abs(fun(x0)) < err:
        return hx,hf
    for _ in range(mit):
        x1 = x0 - fun(x0)**2 / (fun(x0+fun(x0)) - fun(x0))    
        hx.append(x1)
        hf.append(fun(x1))
        if abs(fun(x1)) < err or abs(x1 - x0) / x1 < err :
            return hx,hf
        x0 = x1
    return hx,hf

for i in [1.39, 1.40, 1.41, 3]:
    hx1, hy1 = rnewton(aux_fun,i,1e-6,100)
    aux_fun2 = lambda x : (np.log(x)-1/x)
    hx2, hy2 = rsteff(aux_fun2,i,1e-6,100)
    print(f"La raiz de f(x) con el método de newton es {hx1[-1]}, llevó {len(hx1)-1} iteraciones")
    print(f"La raiz de f(x) con el método de rsteff es {hx2[-1]}, llevó {len(hx2)-1} iteraciones")

# Conclusión: El método de rsteff esta bueno porque no usa la derivada y realiza una cantidad de iteraciones similares al método de Newton cuando estamos cerca de la raiz, pero lleva mas cantidad de iteraciones si estamos más alejados de la raiz


