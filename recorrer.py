import os
os.system("cls" if os.name=="nt" else "clear")
i = 0
e = -1
nombre=""
def recorrido(nombre):
    global e
    global i
    while (i<=(len(nombre)-1)):
        #print(f"{i} {"letra:".capitalize()} {nombre[i]}","\t","|","\t",end="")
        print(f"{"\t"*i}{i} {"letra:".capitalize()} {nombre[e]}")
        i += 1
        e -= 1

recorrido(input("Ingrese un nombre: ".capitalize()))