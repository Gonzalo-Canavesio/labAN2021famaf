def ripf(fun,x0,err,mit):
    hx = [] # Inicio el historial de puntos como lista vacia  
    hx.append(x0) # Agrego el elemento al historial de puntos

    # Comenzamos a iterar, hasta hacer mit cantidad de iteraciones        
    for _ in range(mit):
        x = fun(x0) # Evaluo la funcion en x0
        hx.append(x) # Agrego el elemento al historial de puntos
        # Si actual iteración es muy cercana a la iteración anterior, terminamos el ciclo
        if abs(x - x0) < err:
            return hx
        x0 = x # Actualizamos el valor del punto actual para la próxima iteración  
    return hx