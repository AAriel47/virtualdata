import os
os.system("cls" if os.name=="nt" else "clear")
import subprocess
import cargar

def mostrar():
    print(f"{"\t"}{"1. alta".upper()}")
    print(f"{"\t"}{"2. consulta".upper()}")
    print(f"{"\t"}{"5. cargar db".upper()}")
    print(f"{"\t"}{"6. salir".upper()}")

def ejecutar(opcion):
    if (int(opcion) == 1):
        print("llego")
        subprocess.run(["python","alta.py"])
    elif (int(opcion) == 2):
        subprocess.run(["python","consulta.py"])
    elif(int(opcion)==5):
        #subprocess.run(["python","cargar.py"])
        cargar.ca()
    elif(int(opcion) == 6):
        input(f"{"\t"}hasta luego, pulse enter...".upper())

def main():
    while (True):
        mostrar()
        opcion = input(f"{"\t"}{"Ingrese su respuesta: ".upper()}")
        if int(opcion) !=6:
            ejecutar(opcion)
            #os.system("cls" if os.name=="nt" else "clear")
        else:
            ejecutar(opcion)
            os.system("cls" if os.name=="nt" else "clear")
            break

if __name__=="__main__":
    main()
