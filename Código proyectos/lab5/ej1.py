def intenumcompsimpson(fun,a,b,N):
    h = (b - a) / N
    sx0 = fun(a) + fun(b)
    sx1 = 0
    sx2 = 0
    x = a
    for j in range (1,N):
        x += h
        if j % 2 == 0:
            sx2 = sx2 + fun(x)
        else:
            sx1 = sx1 + fun(x)
    sx = (sx0 + 2 * sx2 + 4 *sx1) * h/3
    return sx

def intenumcomptrapecio(fun,a,b,N):
    h = (b - a) / N
    sx0 = fun(a) + fun(b)
    sx1 = 0
    x = a
    for _ in range (1,N):
        x += h
        sx1 = sx1 + fun(x)
    sx = (sx0 + 2 * sx1) * h/2
    return sx

def intenumcomppm(fun,a,b,N):
    h = (b - a) / N 
    sx = 0
    x = a - h
    for j in range (0,N//2):
        x += 2*h
        sx += fun(x)
    sx = sx * 2*h
    return sx

def intenumcomp(fun,a,b,N,regla):
    res = 0
    if regla == "simpson":
        res = intenumcompsimpson(fun,a,b,N)
    elif regla == "trapecio":
        res = intenumcomptrapecio(fun,a,b,N)
    elif regla == "pm":
        res = intenumcomppm(fun,a,b,N)
    else:
        return "El nombre de la regla no es valida"
    return res

aux = lambda x : x**2

#print(intenumcomp(aux,0,4,80,"simpson"))
#print(intenumcomp(aux,0,4,80,"trapecio"))
#print(intenumcomp(aux,0,4,80,"pm"))


    