import os
import time

class hora:
    pass

def inicial():
    hini = hora()
    hini.ho= 8
    hini.mi = 0
    hini.se = 00
    return hini

def salida():
    os.system("cls" if os.name == "nt" else "clear")
    hsal = hora()
    hsal.ho = int(input("Hora de salida:    "))
    hsal.mi = int(input("Minuto de salida:  "))
    hsal.se = int(input("Segundo de salida: "))
    return hsal
vin = inicial()
vsa = salida()

def proceso(vin, vsa):
    hres = hora()
    hres.ho = vsa.ho - vin.ho
    hres.mi = vsa.mi - vin.mi
    hres.se = vsa.se - vin.se
    if hres.se >= 60:
        hres.se = hres.se - 60
        hres.mi = hres.mi + 1

    if hres.mi >=60:
        hres.mi = hres.mi - 60
        hres.ho = hres.ho + 1
    return hres

imp = proceso(vin,vsa)

def imprimir(imp):
    
    print(f"{"Horas trabajadas: ".upper()} {imp.ho} - {"minutos trabajados: ".upper()} {imp.mi} - {"segundos trabajados: ".upper()} {imp.se}")
    time.sleep(15)
    os.system("cls" if os.name=="nt" else "clear")

imprimir(imp)