import os
import string

carac=""
while (True):
    os.system("cls" if os.name=="nt" else "clear")
    palabra=input("Ingrese una palabra: ")
    for c in palabra:
        #print(c.isalpha(), c)
        for a in string.ascii_uppercase:
            if (c.find(a)!=-1):
                print(f"{"es un caracter en mayuscula".upper()} , {"letra"} {c}")
        for e in string.ascii_lowercase:
            if (c.find(e)!=-1):
                print(f"{"es un caracter en minuscula".upper()} , {"letra"} {c}")    
        for i in string.digits:
            if (c.find(i)!=-1):
                print(f"{"es un caracter numérico".upper()} , {"numero"} {c}")
    seguir=input("Desea seguir s/n: " )
    if (seguir.lower()=="s") or (seguir.lower()=="si"):
        continue
    else:
        break
