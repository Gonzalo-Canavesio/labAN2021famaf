from tkinter import X
import numpy as np
from scipy.optimize import linprog

costos = np.loadtxt('costos.dat')
demanda = np.loadtxt('demanda.dat')
stock = np.loadtxt('stock.dat')

c = costos.flatten()

b_ub = np.hstack([stock, -demanda])

A_s = np.zeros((100,10000))

for i in range(100):
    A_s[i,(i*100):((i+1)*100)] = np.ones(100)

A_d = np.hstack([np.eye(100) for _ in range(100)])

A_ub = np.vstack([A_s,-A_d])

solucion = linprog(c, A_ub, b_ub)

x = np.reshape(solucion.x,(100,100))

idx, idy = np.where(np.round(x))

for i,j in zip(idx,idy):
    print(f"Hay que llevar del deposito {i} al cliente {j} {x[i,j]} cantidad de manies")