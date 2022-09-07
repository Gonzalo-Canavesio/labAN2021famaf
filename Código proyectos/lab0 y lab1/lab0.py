def multiplo(n,m):
  if n % m == 0:
    print('Es divisible')
    return True
  else:
    print('No es divisible')
    return False

def print_vander(m,n):
  for idx in range (1,m+1):
    for jdx in range(idx,n+1):
      print(f"A({idx},{jdx}) = {1/(idx+jdx)}")

import random

def suma_aleatorio(Tol):
  s=0
  contador=0
  while s <= Tol:
    s = s + random.random()
    contador += 1
  return s, contador
  