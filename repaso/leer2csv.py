import os
import sys
import csv
import time
os.chdir("repaso")
archivo = "practicavba.csv"
archivo2 = "practicavba2.csv"
os.system("cls" if os.name=="nt" else "clear")
if os.path.exists(archivo):
    file = open(archivo,encoding="utf-8")
    lectura = csv.reader(file)
else:
    print(f"{"archivo ".capitalize()}{archivo} inexistente...")
    time.sleep(4)
    sys.exit()
datos = list()
for lec in lectura:
    datos.append(lec)
print(datos)

time.sleep(3)

file2 = open(archivo2,"a",newline="",encoding="utf-8")

escribir = csv.writer(file2)
escribir.writerows(datos)