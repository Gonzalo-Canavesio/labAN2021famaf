def dif_divididas(x,y):
    res = []
    temp = []
    for i in range(0,len(x)):
        temp.append(y[i])
    res.append(temp)
    for j in range(1,len(x)):
        temp = []
        for i in range(0,len(x)-j):
            temp.append((res[j-1][i+1] - res[j-1][i])/(x[i+j]-x[i]))
        res.append(temp)
    return res


def inewton(x, y, z):
    res = []
    difs_div = dif_divididas(x,y)
    for k in z:
        eval = 0
        for i in range(0,len(x)):
            prod = 1
            for j in range(0,i):
                prod *= (k-x[j])
            eval += difs_div[i][0] * prod
        res.append(eval)
    return res