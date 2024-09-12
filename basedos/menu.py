import os
import mysql.connector
import subprocess
import alumnos
import notas
import materias
os.system("cls" if os.name=="nt" else "clear")

def mostrar():
    print("1. Ingresar alumno:".upper())
    print("2. ingresar materias:".upper())
    print("3. Ingresar Notas:".upper())
    print("4. Salir s/n: ".upper())

def ejecutar(opciones):
    if (int(opciones)==1):
        #subprocess.run(["python","alumnos.py"])
        alumnos.caralu()
    elif (int(opciones)==2):
        #subprocess.run(["python","materias.py"])
        materias.carmat()
    elif (int(opciones)==3):
        #subprocess.run(["python","notas"])
        notas.carnot()
    elif (int(opciones)==4):
        input("hasta pronto, pulse enter...".upper())
    else:
        input("opción no válida, pulse enter...".upper())

def main():
    while (True):
        mostrar()
        opciones = input("selecciones una opción: ".upper())
        if (int(opciones)==4):
            ejecutar(opciones)
            os.system("cls" if os.name=="nt" else "clear")
            break
        else:
            ejecutar(opciones)
            os.system("cls" if os.name=="nt" else "clear")

if __name__ == "__main__":
    main()
