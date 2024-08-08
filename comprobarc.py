import os
import string

carac=""
while (True):
    os.system("cls" if os.name=="nt" else "clear")
    palabra=input("Ingrese una palabra: ")
    for c in palabra:
        print(c.isalpha(), c)
        if (c.isalpha())&(c==c.upper()):
            print("Es un caracte alfabetico y esta en mayuscula".upper())
        elif (c.isalpha())&(c==c.lower()):
            print("Es un caracte alfabetico y esta en minuscula".lower())
        else:
            print("es un caracter numerico".upper())
    
    seguir=input("Desea seguir s/n: " )
    if (seguir.lower()=="s") or (seguir.lower()=="si"):
        continue
    else:
        break
