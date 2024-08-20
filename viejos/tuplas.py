a = 1,2
b = 3,4
import os
os.system("cls" if os.name=="nt" else "clear")
def cambio (a,b):
    return b,a

a, b = cambio(a,b)
print(a, b)
import random
print(random.randint(1,10))
"""for i in range(10):
    x = random.random()*9
    print(x)
azar=(random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(azar)"""
def listaAleatorios(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
        print(s)
    return s

listaAleatorios(2)