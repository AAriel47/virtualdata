import os
os.system("cls" if os.name=='nt' else 'clear')
valor = ('a',1,'b',2,3)
print(valor)
letra = {"one": "uno", "two": "dos"}
datos = {}
datos["nombre"] = "Alejandro Ariel"
datos ["apellido"] = "Uñate"
datos ["edad"] = 48
print (f"{"datos".capitalize()} {datos}")
datos.keys()
matriz = [ [0,0,0,1,0],
[0,0,0,0,0],
[0,2,0,0,0],
[0,0,0,0,0],
[0,0,0,3,0] ]

#letra.
numeros = 1
#letra.
letra = {}
letra.keys
for i in valor:
    print(type [i])
"""import random
lista = [0] * 1000
for i in range(1000):
    lista[i] = random.random()
#return s
#lista=[0.15156642489, 0.498048560109, 0.810894847068, 0.360371157682, 0.275119183077, 0.328578797631, 0.759199803101, 0.800367163582]
def enElBalde(lista, minimo, maximo):
    cuenta = 0
    for num in lista:
        if minimo < num < maximo:
            cuenta = cuenta + 1
    return cuenta

numBaldes = 8
baldes = [0] * numBaldes
anchuraBalde = 1 / numBaldes
for i in range(numBaldes):
    minimo = i * anchuraBalde
    maximo = minimo + anchuraBalde
    #print("minimo", minimo, maximo)
    baldes[i] = enElBalde(lista, minimo, maximo)
print (baldes)
"""