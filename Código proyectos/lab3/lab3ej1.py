def ilagrange(x, y, z):
    res = [] # En res guardaré los valores de cada elemento de z evaluado en el polinomio interpolante
    # Inicio ciclo para evaluar cada z en el polinomio interpolante
    for k in z:
        eval = 0 # 0 es el neutro de la suma
        # Simulo una sumatoria
        for i in range(0,len(x)):
            prod = 1 # 1 es el neutro del producto
            # Simulo una sumatoria
            for j in range(0,len(x)):
                if(j != i): 
                    prod *= (k-x[j])/(x[i]-x[j]) # Guardo el valor de esta "iteración" de la productoria
            eval += y[i] * prod  # Guardo el valor final de la productoria de esta "iteración" de la sumatoria
        res.append(eval) # Guardo el valor final de la sumatoria para el z correspondiente a esta iteración
    return res

# w = ilagrange([1,2,3,4], [0,-1,0,1], [0,5,6,8])
# print(w)