import os
os.system("cls" if os.name=="nt" else "clear")
import subprocess
import cargar
import verdb
import verdbcod
import borrardbcod
def mostrar():
    print(f"{"\t"}{"1. alta".upper()}")
    print(f"{"\t"}{"2. consulta".upper()}")
    print(f"{"\t"}{"3. consulta db".upper()}")
    print(f"{"\t"}{"4. consulta por codigo".upper()}")
    print(f"{"\t"}{"5. cargar db".upper()}")
    print(f"{"\t"}{"6. borrar por codigo".upper()}")
    print(f"{"\t"}{"7. salir".upper()}")

def ejecutar(opcion):
    if (int(opcion) == 1):
        print("llego")
        subprocess.run(["python","alta.py"])
    elif (int(opcion) == 2):
        subprocess.run(["python","consulta.py"])
    elif (int(opcion) == 3):
        #subprocess.run(["python","verdb.py"])
        verdb.verlos()
    elif (int(opcion) == 4):
        verdbcod.veracod()
    elif(int(opcion)==5):
        #subprocess.run(["python","cargar.py"])
        cargar.ca()
    elif(int(opcion) ==6):
        borrardbcod.borracod()
    elif(int(opcion) == 7):
        input(f"{"\t"}hasta luego, pulse enter...".upper())

def main():
    while (True):
        mostrar()
        opcion = input(f"{"\t"}{"Ingrese su respuesta: ".upper()}")
        if int(opcion) !=7:
            ejecutar(opcion)
            #os.system("cls" if os.name=="nt" else "clear")
        else:
            ejecutar(opcion)
            os.system("cls" if os.name=="nt" else "clear")
            break

if __name__=="__main__":
    main()
