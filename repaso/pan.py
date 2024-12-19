import os
import time
class hora:
    pass

def elaborar():
    inicio = hora()
    inicio.ho = 8
    inicio.mi = 30
    inicio.se = 20
    return inicio
def entrega():
    final = hora()
    final.ho = 3
    final.mi = 10
    final.se = 30
    return final

valor1 = elaborar()
valor2 = entrega()
def sumar(valor1, valor2):
    entrega = hora()
    entrega.ho = valor1.ho + valor2.ho
    entrega.mi = valor1.mi + valor2.mi
    entrega.se = valor1.se + valor2.se
    return entrega

entre = sumar(valor1, valor2)

def imprimir(entre):
    os.system("cls" if os.name=="nt" else "clear")
    print(f"{"Hora de entrega: ".upper()}{entre.ho} : {"minutos: ".upper()}{entre.mi} {"segundos: ".upper()}{entre.se}")
    time.sleep(5)

imprimir(entre)