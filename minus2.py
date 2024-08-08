import os
os.system("cls" if os.name=="nt" else "clear")
import string

def minus(c):
    #a=""
    i = 0
    for a in c:
        #print(a in string.ascii_lowercase)
        if ("a"<=a<="z"):
            print(f"{"\t"*i} {a}", end='')
            print()
        if ("A"<=a<="Z"):
            print(f"{"\t" *i} {a}", end="")
            print()
        if (a in string.digits):
            print(f"{"\t" *i} {a}", end="")
            print()
        if (a in string.whitespace):
            print(f"{"\t"*i} {"-"}", end="")
            print()
        i+= 1
    return c.upper()

ver = minus(input("Ingrese un mensaje: "))
print(ver)