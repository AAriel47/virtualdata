import os
import math
alumno = list()
datos = "alumnos.txt"
while (True):
    alumno.clear()
    os.system("cls" if os.name=="nt" else "clear")
    print(f"{"-".ljust(40,"-")} {"ingreso de alumnos 2025".upper()} {"-".rjust(40,"-")}")
    print("")
    try:
        alum = int(input("Ingrese el codigo:   ".upper()).upper())
    except ValueError:
        input("ingrese solo valores numéricos, pulse enter...".upper())
        continue
    alumno.insert(len(alumno),str(alum))
    alumno.insert(len(alumno),input("Ingrese el Nombre:   ".upper()).upper())
    alumno.insert(len(alumno),input("Ingrese el apellido: ".upper()).upper())
    alumno.insert(len(alumno),input("Ingrese la materia:  ".upper()).upper())
    try:
        nota = int(input("Ingrese la nota:     ".upper()).upper())
    except ValueError:
        input("ingrese solo valores numéricos, pulse enter...".upper())
        continue
    alumno.insert(len(alumno),str(nota))
    print("")
    alumno[1:1]=" "
    alumno[3:3]=" "
    alumno[5:5]=" "
    alumno[7:7]=" "

    gra = input(f"{"-".ljust(35,"-")} {"Desea grabar el registro Si/No: ".upper()}")
    print(" ")
    if ((gra.lower()=="si")or(gra.lower()=="s")):
        if(os.path.exists(datos)):
            arch1 = open(datos,"a",encoding="utf-8")
            arch1.writelines(alumno)
            arch1.writelines("\n")
        else:
            with open(datos,"w",encoding="utf-8") as arch1:
                arch1.writelines(alumno)
                arch1.writelines("\n")
        print("el registro se guardo".center(100).upper())
        arch1.close()
    else:
        print("el registro no se guardo".upper().center(100))
    print(" ")
    res = input(f"{"-".ljust(35,"-")} {"Desea Ingresar otro alumno Si/No: ".upper()}")
    print(" ")
    if ((res.lower()=="si") or(res.lower()=="s")):
        continue
    else:
        break