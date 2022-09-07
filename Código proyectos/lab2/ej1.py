def rbisec(fun,I,err,mit):
    a = I[0] # extremo izquierdo del intervalo
    b = I[1] # extremo derecho del intervalo
    # Evaluo la función en los extremos del itnervalo
    u = fun(a)
    v = fun(b)
    # Inicio los historiales como listas vacías
    hx = []
    hf = []
    # Si u y v tienen mismo signo, no podemos seguir
    if (u*v > 0):
        return("No se puede asegurar la hipotesis del metodo de biseccion en el intervalo dado")
    # Si f(a) es menor al error terminamos la ejecución porque encontramos el cero que buscabamos
    elif abs(u)<err:
        hx.append(a)
        hf.append(u)
        return(hx,hf)
    # Si f(b) es menor al error terminamos la ejecución porque encontramos el cero que buscabamos
    elif abs(v)<err:
        hx.append(b)
        hf.append(v)
        return(hx,hf)
    # Nos aseguramos de que u < v
    if u > v:
        u,v = v,u
    # Comenzamos a iterar, hasta hacer mit cantidad de iteraciones    
    for _ in range(mit):
        c = a + (b-a)/2 # c es tiene el punto medio entre a y b
        w = fun(c) # evaluo la función en el punto medio
        # Agregamos los elementos a sus respectivos historiales
        hx.append(c)
        hf.append(w)
        # Si la función evaluada en c es suficientemente pequeña en modulo, salimos del ciclo
        if(abs(w)<err):
            break
        # Reemplazo a <- c o b <- c, según corresponda
        if (u*w < 0):
            b = c
            v = w
        else:
            a = c
            u = w

    return (hx,hf)