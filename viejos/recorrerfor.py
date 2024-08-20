import os
os.system("cls" if os.name=="nt" else "clear")
i = 0
#e = -1
nombre=""
def recorrido(nombre2):
    nombre = reversed(nombre2)
    #global e
    global i
    for nom in nombre:
        #print(f"{i} {"letra:".capitalize()} {nombre[i]}","\t","|","\t",end="")
        print(f"{"\t"*i}{i} {"letra:".capitalize()} {nom}")
        i += 1


recorrido(input("Ingrese un nombre: ".capitalize()))