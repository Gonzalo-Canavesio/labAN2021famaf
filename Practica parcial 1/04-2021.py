import numpy as np
import matplotlib.pyplot as plt

def rsec(fun,x0,x1,err,mit):
    f,df = fun(x0)
    f0 = f
    f,df = fun(x1)
    f1 = f
    hx = []
    hf = []
    hx.append(x1)
    hf.append(f1)
    if abs(f1) < err:
        return hx,hf
    for _ in range(mit):
        if abs(f0) > abs(f1):
            x0,x1 = x1,x0
            f0,f1 = f1,f0
        s = (x1 - x0)/(f1 - f0)
        x1 = x0
        f1 = f0
        x0 = x0 - f0 * s
        f,df = fun(x0)
        f0 = f
        hx.append(x1)
        hf.append(f1)
        if abs(f0) < err:
            break
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

def busqueda_ceros(fun, x0, x1, err, mit):
    hx1, hy1 = rnewton(fun,x0,err,mit)
    hx2, hy2 = rsec(fun,x0,x1,err,mit)
    print(f"El cero encontrado por el método de newton es {hy1[-1]}, le tomo {len(hy1)-1} iteraciones y lo encontró en el punto {hx1[-1]}")
    print(f"El cero encontrado por el método de la secante es {hy2[-1]}, le tomo {len(hy2)-1} iteraciones y lo encontró en el punto {hx2[-1]}")
    if abs(hx1[-1]) < abs(hx2[-1]):
        return hx1[-1]
    else:
        return hx2[-1]

def horn(coefs,x):
  res = 0
  for i in coefs:
    res = i + x * res
  return(res)

aux_fun = lambda x : ( horn([1,0,1,-5],x), horn([3,0,1],x)) 

busqueda_ceros(aux_fun,10,-10,1e-6,15)

x = np.linspace(-2, 4, 100)
plt.plot(x, horn([1,0,1,-5],x), label="$x^3+x-5$")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()
