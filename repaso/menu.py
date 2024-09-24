import os
import subprocess
import alta
import re
import consultas
import borrar
import modificar

def mostrar():
    print("\t1. Alta: ".upper())
    print("\t2. Baja: ".upper())
    print("\t3. Modificaciones: ".upper())
    print("\t4. Consulta: ".upper())
    print("\t5. Salir: ".upper())

def opciones(opcion):
    match (opcion):
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
        opcion = input("\tSeleccion una opción: ".upper())
        if opcion != "5" :
            opciones(opcion)
        elif opcion == "5":
            opciones(opcion)
            os.system("cls" if os.name=="nt" else "clear")
            break

if __name__=="__main__":
    main()