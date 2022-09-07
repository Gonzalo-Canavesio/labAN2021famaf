import math
import random

### 3

def underflow():
  res = 1
  while(True):
    if(res/2 == 0.0):
      print(f"El número de underflow es {res}")
      break
    res = res/2

def overflow():
  res = 1.0
  while(True):
    if(math.isinf(res*2.0)):
      print(f"El número de overflow es {res}")
      break
    res = res*2

### 4

def hasta_10_1():
  x = 0
  while x != 10:
    x = x + 0.1
    print(x)

# Cómo 0.1 no puede ser representado exactamente en binario, x nunca llega a ser exactamente 10 y por lo tanto el programa no termina porque siempre es diferente de 10

def hasta_10_1_posible():
  x = 0
  while x < 10:
   x = x + 0.1
   print(x)

def hasta_10_5():
  x = 0
  while x != 10:
    x = x + 0.5
    print(x)

# Cómo 0.5 puede ser representado exactamente en binario, x llega a ser exactamente 10 y por lo tanto el programa termina porque x es igual a 10

### 5

def factorial_6():
  res = 1
  for i in range (2,7):
    res = res * i
  return res

def factorial_manual(n):
  x = 1
  for i in range (1,n+1):
    x = x * i
  return(x)

def factorial_auto(n):
  return math.factorial(n)

### 6

def diferentes(n,m):
  if(n == m):
    print(f"Ambos numeros son iguales")
  elif (n > m):
    print(f"El numero {n} es mayor a {m}")
  else:
    print(f"El numero {m} es mayor a {n}")

### 7

def potencia(x,n):
  k = 1
  for i in range (n):
    k = k*x
  return(k)

def primeras_potencias(x):
  for i in range (1,6):
    print(potencia(x,i))

### 8

def mala(a,b,c):
  d = b**2-4*a*c
  if(d < 0):
    print("La ecuación no tiene raices reales")
  elif(d == 0):
    x = (-b+math.sqrt(d))/(2*a)
    return x
  else:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    return [x1,x2]

def buena(a,b,c):
  d = b**2-4*a*c
  if(d < 0):
    print("La ecuación no tiene raices reales")
  elif(d == 0):
    x = (-b+math.sqrt(d))/(2*a)
    return x
  else:
    if(b > 0):
      x1 = (-b-math.sqrt(d))/(2*a)
      x2 = c/(a*x1)
      return [x1,x2]
    else:
      x1 = (-b+math.sqrt(d))/(2*a)
      x2 = c/(a*x1)
      return [x1,x2]      

### 9

def horn(coefs,x):
  res = 0
  for i in coefs:
    res = i + x * res
  return(res)

### 10

def sonReciprocos(x,y):
  return x*y == 1

def prueba_reciprocos():
  for _ in range(100):
    x = 1 + random.random()
    y = 1/x
    if not sonReciprocos(x,y):
      print(x)

# Lo que sucede es que 1/x no puede ser representado de manera exacta en binario en algunos casos porque no alcanzan la cantidad de digitos, por lo tanto luego al multiplicarse por x queda algo diferente de 1

### 11

def f(x):
  return math.sqrt(x**2+1) - 1

def g(x):
  return x**2/(math.sqrt(x**2+1)+1)

def prueba_g_f():
  for i in range(20):
    x = 8**-i
    print(f"f(x)={f(x)}, g(x)={g(x)}")

# Mientras más chico es el número, mayor es la diferencia relativa entre ambos resultados. g(x) es más confiable porque no utiliza restas, y las restas son las operaciones que mayor error pueden generar al hacer un calculo en la computadora
### 12

def sonOrtogonales(x,y):
  return x[0]*y[0]+x[1]*y[1] == 0

def prueba_ortogonales():
  x = [1, 1.1024074512658109]
  y = [-1, 1/x[1]]
  if not sonOrtogonales(x,y):
    print("Algo salio mal...")

# Lo que sucede es que 1/x no puede ser representado de manera exacta en binario porque no alcanzan la cantidad de digitos (es un número periodico en binario), por lo tanto luego al multiplicar 1/x * x queda algo diferente de 1 (en este caso, 0.9999...)