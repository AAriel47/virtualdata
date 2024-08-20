import os
os.system("cls" if os.name=="nt" else "clear")
valores = [2,4,6,8,10]
a = int(input("ingrese un numero: "))
if (a not in valores):
    print("no se encuentra en el rango".upper())
else:
    print("si se encuentra en el rango".lower())
    print(f"valor {a^2}")
    b = 4^2
    print(b)
input()
os.system("cls" if os.name=="nt" else "clear")
b = int(input("Ingrese otro número: ").upper())
if(b in valores):
    print("si se encuentra en el rango".lower())
else:
    print("no se encuentra en el rango".lower())
input()
os.system("cls" if os.name=="nt" else "clear")