def rnewton(fun,x0,err,mit):
    f,df = fun(x0) # Guardo en f la evaluacion del punto x0 y en df su derivada evaluada en x0
    # Inicio los historiales como listas vacías
    hx = []
    hf = []
    # Agregamos los elementos a sus respectivos historiales
    hx.append(x0)
    hf.append(f)
    # Si f(x0) es menor al error terminamos la ejecución porque encontramos el cero que buscabamos
    if abs(f) < err:
        return hx,hf

    # Comenzamos a iterar, hasta hacer mit cantidad de iteraciones    
    for _ in range(mit):
        # Si la derivada es 0 es imposible dividir por ella
        if df == 0:
            return "No se puede realizar el metodo, la derivada es 0"
        x1 = x0 - f / df # Guardo en x1 el valor de la siguiente iteración del método de newton
        f,df = fun(x1) # Evaluo f y la derivada de f en la siguiente iteracion
        # Agregamos los elementos a sus respectivos historiales        
        hx.append(x1)
        hf.append(f)
        # Si estamos lo suficientemente cerca del 0 o la actual iteración es muy cercana a la iteración anterior, terminamos el ciclo
        if abs(f) < err or abs(x1 - x0) / x1 < err :
            return hx,hf
        x0 = x1 # Actualizamos el valor de la actual iteracion
    return hx,hf