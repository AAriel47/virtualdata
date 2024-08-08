import os
os.system("cls" if os.name=="nt" else "clear")
import string

def minus(c):
    #a=""
    i = 0
    for a in c:
        #print(a in string.ascii_lowercase)
        if (a in string.ascii_lowercase):
            print(f"{"\t"*i} {a}", end='')
            print()
        if (a in string.ascii_uppercase):
            print(f"{"\t" *i} {a}", end="")
            print()
        if (a in string.digits):
            print(f"{"\t" *i} {a}", end="")
            print()
        if (a==" "):
            print(f"{"\t"*i} {a}", end="")
            print()
        i+= 1
    return c.upper()

ver = minus(input("Ingrese un mensaje: "))
print(ver)