import os
#os.system("cls" if os.name=="nt" else "clear")
alumnos = list()
alumnos1 = []
archivo = "notas.txt"
while (True):
    os.system("cls" if os.name=="nt" else "clear")
    try:
        alumnos.insert(0,int(input("codigo: ".upper())))
    except ValueError:
        input("codigo invalido, pulse enter...".upper())
        continue
    try:
        alumnos.insert(1,int(input("nota: ".upper())))
    except ValueError:
        input("codigo invalido, pulse enter...".upper())
        continue

    res = input("Desea guardar el registro S/N: ".upper())
    if (res.lower()=="s" or res.lower()=="si"):
        alumnos1.insert(0,(str(alumnos[0]) + ", "))
        alumnos1.insert(1,(str(alumnos[1]) +"\n"))
        #print(alumnos, type(alumnos[0]), type(alumnos[1]))
        input()
        if os.path.exists(archivo):
            archi = open(archivo,"a",encoding="utf-8")
            archi.writelines(alumnos1)
        else:
            with open(archivo,"w",encoding="utf-8") as archi:
                archi.writelines(alumnos1)
        print("registro cargado".upper())
        archi.close()
        #print(alumnos)
    else:
        print("registro no cargado".upper())
    seguir = input("desea seguir cargando: ".upper())
    if (seguir.lower()=="s" or seguir.lower()=="si"):
        alumnos1 = []

        continue
    else:
        break
print("que descanses, buenas tardes...".upper())
print()