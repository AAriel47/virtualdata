import limpiar
import subprocess
import os
import re
#import altabd
def mostrardb():
    print(f'{"-".rjust(35,"-")} "MANTENIMEINTO DE BASE DE DATOS" {"-".ljust(35,"-")}')
    print("\t\t | \t  1. Alta BD: ".upper())
    print("\t\t | \t  2. Baja DB: ".upper())
    print("\t\t | \t  3. Modificaciones DB: ".upper())
    print("\t\t | \t  4. Consulta DB: ".upper())
    print("\t\t | \t  5. Salir: ".upper())
    print("\t\t | \t".ljust(50,"-"))

def ejecutarbd(opcion):
    limpiar.limp()
    match (opcion):
        case 1:
            subprocess.run(["python","altabd.py"])
            #altabd()
            #pass
        case "2":
            pass
        case "3":
            pass
        case 4:
            subprocess.run(["python","consuldb.py"])
            #pass
        case 5:
            print("final del proceso!!!".upper().center(100))
            print("pulse enter para continuar...".upper().center(100))
            input()
        case _:
            print ("opción no valida!!!".upper())
            input("pulse enter para continuar...".upper())

def main():
    while True:
        patternruta= r"^(D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\repaso)$"
        ruta = re.compile(patternruta)
        verificar = ruta.match(os.getcwd())

        if verificar==None:
            os.chdir("repaso")

        limpiar.limp()
        mostrardb()
        try:
            opcion= int(input("\t\t | \t  Seleccione una Opción: ".upper()))
        except ValueError:
            print("valor incorrecto".upper().center(100))
            print("pulse enter...".upper().center(100))
            input()
        else:
            if opcion > 0 and opcion <5:
                ejecutarbd(opcion)
            elif opcion == 5:
                ejecutarbd(opcion)
                limpiar.limp()
                break
            else:
                ejecutarbd(opcion)
        finally:
            print(f'{"-".rjust(42,"-")} "FIN DE LA EJECUCIÓN" {"-".ljust(41,"-")}')
            input()
            limpiar.limp()
            #return

if __name__=="__main__":
    main()
