import os
#os.system("cls" if os.name=="nt" else "clear")
alumnos = list()
archivo = "alumno.txt"
while (True):
    os.system("cls" if os.name=="nt" else "clear")
    try:
        alumnos.insert(0,int(input("codigo: ".upper())))
    except ValueError:
        input("codigo invalido, pulse enter...".upper())
        continue
    #alumnos.insert(1,",")
    alumnos.insert(1,input("Nombre: ".upper()).upper())
    alumnos.insert(2,input("Curso:  ".upper()).upper())
    res = input("Desea guardar el registro S/N: ".upper())
    if (res.lower()=="s" or res.lower()=="si"):
        alumnos[0] = str(alumnos[0]) + ", "
        alumnos[1] = alumnos[1] + ", "
        alumnos[2] = alumnos[2] +"\n"
        print(alumnos)
        input()
        if os.path.exists(archivo):
            archi = open(archivo,"a",encoding="utf-8")
            archi.writelines(alumnos)
        else:
            with open(archivo,"w",encoding="utf-8") as archi:
                archi.writelines(alumnos)
        print("registro cargado".upper())
        archi.close()
        #print(alumnos)
    else:
        print("registro no cargado".upper())
    seguir = input("desea seguir cargando: ".upper())
    if (seguir.lower()=="s" or seguir.lower()=="si"):
        alumnos = list()

        continue
    else:
        break
print("que descanses, buenas tardes...".upper())
print()