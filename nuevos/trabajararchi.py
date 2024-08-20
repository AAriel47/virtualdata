import os
os.system('cls' if os.name == 'nt' else 'clear')
archi = "datos.dat"
if (os.path.exists(archi)):
    archi2 = open (archi,"a",encoding="utf-8")
    archi2.write(input("ingrese un texto: "))
    archi2.write("\n")
else:
    with open(archi,"w", encoding="utf-8") as archi2:
        archi2.write(input("ingrese un texto: "))
        archi2.write("\n")
archi2.close()
