"""import os
os.system("cls" if os.name=="nt" else "clear")
nombre = input("Ingrese un nombre: ")
c = input("Ingrese un caracter: ")
i = 0
#c = ""
while (i< len(nombre)):
    if (c == nombre[i]):
        print(f"el caracter buscado '{c}' se encuentra en la posición: {i}") 
        break
    elif (i == len(nombre)-1):
        print(f"el caracter buscado '{c}' no existe en la cadena")
    i = i + 1"""

import os
os.system("cls" if os.name=="nt" else "clear")
nombre = input("Ingrese un nombre: ")
c = input("Ingrese un caracter: ")
i = 0
#c = ""
def buscar(nombre, c):
    global i
    while (i< len(nombre)):
        if (c == nombre[i]):
            print(f"el caracter buscado '{c}' se encuentra en la posición: {i}") 
            return i
        elif (i == len(nombre)-1):
            print(f"el caracter buscado '{c}' no existe en la cadena")
        i = i + 1
    return -1

val = buscar(nombre, c)

print(val!=-1)