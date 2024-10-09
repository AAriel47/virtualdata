import os
import sys
import re
import csv
import time
archivo="practicavba.csv"
os.system("cls" if os.name=="nt" else "clear")
exec('os.chdir("repaso")')
sys.path.append('D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\Lib\\site-packages')
if (os.path.exists(archivo)):
    archi = open(archivo,encoding="utf-8")
    lectura = csv.reader(archi)
    archi2 = open("practicavba2.csv","a",newline="",encoding="utf-8")
    #archi.close()
    campos = list()
    for lec in lectura:
        campos.append(lec)
    print(campos)
    input()
    escribir=csv.writer(archi2)
    escribir.writerows(campos)

else:
    print(f"{"archivo".upper()} {archivo} {"inexistente".upper()}")
    time.sleep(3)
    
