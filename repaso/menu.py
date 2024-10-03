import os
import subprocess
import alta
import re
import consultas
import borrar
import modificar
#import menubd

def mostrar():
    print("\t1. Alta: ".upper())
    print("\t2. Baja: ".upper())
    print("\t3. Modificaciones: ".upper())
    print("\t4. Consulta: ".upper())
    print("\t5. base de datos: ".upper())
    print("\t6. Salir: ".upper())

def opciones(opcion1):
    match (opcion1):
        case "1":
            #subprocess.run(["python","alta.py"])
            alta.alt()
        case "2":
            #subprocess.run(["python","baja.py"])
            borrar.bo()
        case "3":
            #subprocess.run(["python","modif.py"])
            modificar.modi2()
        case "4":
            #subprocess.run(["python","consultas.py"])
            consultas.con()
        case"5":
            subprocess.run(["python","menubd.py"])
            #menubd.main()
        case "6":
            input("Final de ejecución del sistema".upper().center(100))
        case _:
            input("opción no válida ".upper().center(100))

def main():
    while True:
        os.system("cls" if os.name=="nt" else "clear")
        mostrar()
        dir1 = r"^(D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\repaso)$"
        dir2 = re.compile(dir1)
        val = dir2.match(os.getcwd())
        if val:
            pass
        else:
            exec('os.chdir("repaso")')
        opcion1 = input("\tSeleccion una opción: ".upper())
        if opcion1 != "6" :
            opciones(opcion1)
        elif opcion1 == "6":
            opciones(opcion1)
            os.system("cls" if os.name=="nt" else "clear")
            break

if __name__=="__main__":
    main()