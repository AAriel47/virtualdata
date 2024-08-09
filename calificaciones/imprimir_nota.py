import os
#os.system("cls" if os.name=="nt" else "clear")
alumnos = list()
notas = list()
archivoA = "alumno.txt"
archivoN = "notas.txt"
codigo=0
while (True):
    os.system("cls" if os.name=="nt" else "clear")
    try:
        codigo= int(input("codigo: ".upper()))
    except ValueError:
        input("codigo invalido, pulse enter...".upper())
        continue
    if os.path.exists(archivoA):
        archi1 = open(archivoA,"r",encoding="utf-8")
        alumnos=archi1.readlines()
    else:
        input("No existe el archivo alumnos.txt...".upper())
        break
    
    if os.path.exists(archivoN):
        archi = open(archivoN,"r",encoding="utf-8")
        notas = archi.readlines()
    else:
        input("No existe el archivo notas.txt...".upper())
        break
    #alumnos.insert(1,",")
    i = 0
    for alum1 in alumnos:
        alum=alum1.split(",")
        if (int(alum[0]) == codigo):
            i = 1
            for nota1 in notas:
                nota = nota1.split(",")
                if(int(nota[0])==codigo):
                    i = 2
                    cursos = alum[2]
                    print(f"{"nombre:".upper()} {alum[1]} - {"curso:".upper()} {cursos[0:int(len(cursos))-1]} - {"Nota: ".upper()} {nota[1]}")
    if i == 0:
        print("no posee nota  o alumno inexistente".upper())
    archi1.close()
    seguir = input("desea seguir consultando: ".upper())
    if (seguir.lower()=="s" or seguir.lower()=="si"):
        alumnos = list()

        continue
    else:
        break
print("que descanses, buenas tardes...".upper())
print()