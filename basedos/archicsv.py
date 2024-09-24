import os
import csv
os.system("cls" if os.name=="nt" else "clear")
archi = "alumnos.csv"
if (os.path.exists(archi)):
        archi1 = open(archi,"r")
        reader = csv.reader(archi1)
        print("veamos")
        print(os.getcwd())
        input()
else:
        with open(archi,"r") as archi1:
                reader = csv.reader(archi1)

for r, row in enumerate(reader):
        print (r, row)
for i in reader:
        valor = i
        print(valor)