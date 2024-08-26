import os
import basedatos
#input("cargar")
def ca():
    os.system("cls" if os.name=="nt" else "clear")
    alumno = list()
    datos = "alumnos.txt"
    if (os.path.exists(datos)):
        arch=open(datos,"r",encoding="utf-8")
        alumno=arch.readlines()
        arch.close()
        #alumnos="".join(alumno)
        #alum = alumnos.split(",")
        i=0
        e=0
        datalum=list()
        for alumnos in alumno:
            datalum  = alumnos.split(" ")
            while (i<len(datalum)):
                i += 1
            #print(i)
            if i==6:
                codigo = datalum[0]
                nombre = datalum[1]+" "+datalum[2]
                apellido = datalum[3]
                curso = datalum[4]
                nota = datalum[5]
            else:
                codigo = datalum[0]
                nombre = datalum[1]+" "+datalum[2]+" "+datalum[3]
                apellido = datalum[4]
                curso = datalum[5]
                nota = datalum[6]
            #input("pul")
            #print((codigo,nombre,apellido,curso,nota))
            basedatos.cardat(codigo,nombre,apellido,curso,nota)
    else:
        print("archivo inexistente".upper())
ca()