import os
import time
class hora:
    pass

def elaborar():
    inicio = hora()
    inicio.ho = 8
    inicio.mi = 30
    inicio.se = 20
    ini = [inicio.ho, inicio.mi, inicio.se]
    final = hora()
    final.ho= 3
    final.mi = 10
    final.se = 30
    fin = [final.ho, final.mi, final.se]
    return ini, fin

valor1 = list(elaborar())

def sumar(valor1):
    entrega = hora()
    entrega.ho = valor1[0][0] + valor1[1][0]
    entrega.mi = valor1[0][1] + valor1[1][1]
    entrega.se = valor1[0][2] + valor1[1][2]
    return entrega

entre = sumar(valor1)

def imprimir(entre):
    os.system("cls" if os.name=="nt" else "clear")
    print(f"{"Hora de entrega: ".upper()}{entre.ho} : {"minutos: ".upper()}{entre.mi} {"segundos: ".upper()}{entre.se}")
    time.sleep(5)

imprimir(entre)