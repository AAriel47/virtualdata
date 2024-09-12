import os
import re
#fecha=r"((^[10-31]+)|(^[1-9]))\/(([10-12]+)|([1-9]))\/([\d]+)"
#dia="11/06/2024"
#va = re.match(fecha,dia)
control = r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$"

while True:
    os.system("cls" if os.name=="nt" else "clear")
    nombre=input(f"{"Nombre y Apellido: ".upper()}")
    print(nombre)
    input()
    val = re.match(control,nombre)
    print(val)
    input()
    if not(val):
        input(f"{"Ingrese bien el nombre y el apellido,".upper()} {"pulse enter...".upper()}")
        continue
    else:
        input(f"{"Todo bien...".upper()}, {val.group()}")
    #res =input("Desea continuar s/n: ")
    res =True if(input("Desea continuar s/n: ").lower())=="s" else False
    #if (res.lower()=="s" or res.lower()=="S"):
    if (res):
        continue
    else:
        #input("no")
        os.system("cls" if os.name=="nt" else "clear")
        break




