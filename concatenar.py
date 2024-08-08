import os
os.system("cls" if os.name=="nt" else "clear")
i = 0
e = 1
nombre=""
mens = ["ntes", "ogaba", "r", "fectivamente","ejos"]
def recorrido(nombre2):
    long=int(len(nombre2)-1)
    nombre = reversed(nombre2)
    global e
    global i
    global mens

    for nom in nombre:

        #print(f"{i} {"letra:".capitalize()} {nombre[i]}","\t","|","\t",end="")
        if i == long:
            print(f"{"\t"*i}{i} {"letra:".capitalize()} {nom.capitalize()}{mens[-e]}")
        else:
            print(f"{"\t"*i}{i} {"letra:".capitalize()} {nom}{mens[-e]}")
        i += 1
        e += 1


#recorrido(input("Ingrese un nombre: ".capitalize()))
recorrido("Ariel")