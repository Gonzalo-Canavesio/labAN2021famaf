from lab3ej1 import ilagrange
import math

def obtiene_coefs(f):
    c = f(0)[0]
    ab1 = f(1)[0]
    ab2 = f(-1)[0]
    ab1 = ab1 - c
    ab2 = ab2 - c
    a = (ab1+ab2)/2
    b = (ab2-ab1)/2
    return a, b, c

def buena(a,b,c):
  d = b**2-4*a*c
  if(d < 0):
    return b/(2*a)
  elif(d == 0):
    return (-b+math.sqrt(d))/(2*a)
  else:
    if(b > 0):
      x1 = (-b-math.sqrt(d))/(2*a)
      x2 = c/(a*x1)
      return [x1,x2]
    else:
      x1 = (-b+math.sqrt(d))/(2*a)
      x2 = c/(a*x1)
      return min(abs(x1),abs(x2))

def ripf(fun,x0,err,mit):
    hx = []
    hx.append(x0)
    for _ in range(mit):
        x = fun(x0)
        hx.append(x)
        if abs(x - x0) < err:
            return hx
        x0 = x
    return hx

def rinterp(fun ,x0, x1, x2, err, mit):
    f0 = fun(x0)
    f1 = fun(x1)
    f2 = fun(x2)
    hx = []
    hf = []
    hx.append(x2)
    hf.append(f2)
    for _ in range (mit):
        f = lambda x : ilagrange([x0,x1,x2], [f0,f1,f2], [x])
        a,b,c = obtiene_coefs(f)
        xn = buena(a,b,c)
        x0 = x1
        x1 = x2
        x2 = xn
        print([x0,x1,x2])
        f0 = f1
        f1 = f2
        f2 = fun(x2)
        hx.append(x2)
        hf.append(f2)
        if abs(f2) < err:
            break
    return hx, hf


def fun(x): return (x**3 + x**4 + x)
print(rinterp(fun, -5, 1, 8, 1e-7, 500))