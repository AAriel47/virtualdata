import os
import sys
import re
import time
import limpiar
import csv
os.chdir("repaso")
class micontrol(Exception):
    pass
pattern = r'^[1-9]$|^[0-9]+$'
def verificar(edad):
    if int(edad)<18:
        raise micontrol(f"{"todavía eres menor de edad, ".upper()}tienes {edad} {"te faltan".upper()} {18-int(edad)}")
    return "FELICIDADES YA PUEDES JUGAR..."

try:
    limpiar.limp()
    edad = input(f"{"Ingrese su edad: ".upper()}")
    regexp = re.compile(pattern)
    val = regexp.match(edad)
    if val == None:
        print("no es una edad válida...".upper())
        time.sleep(3)
        sys.exit()
    mensaje = verificar(edad)
    print(mensaje)
    print("")
    time.sleep(3)
    datos=list()
    archi=open("practicavba.csv","r",encoding="utf-8")
    valor = csv.reader(archi)
    for va in valor:
        datos.append(va)
    print(datos)
    print("")
    time.sleep(3)
    archi2=open("practicavba2.csv","a",newline="",encoding="utf-8")
    escribir = csv.writer(archi2)
    escribir.writerows(datos)
    archi2.close()
except micontrol as m:
    print(f"{"problema con tu edad: ".upper()} {m}")
    print("")
    time.sleep(3)