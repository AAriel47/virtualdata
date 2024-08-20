import os
os.system('cls' if os.name == 'nt' else 'clear')
archi = "datos.dat"
if (os.path.exists(archi)):
    archi2 = open (archi,"r",encoding="utf-8")
    archi3=archi2.read()
    archi2.close()
    print(archi3)
else:
    print(f"El archivo: {archi} no existe")

