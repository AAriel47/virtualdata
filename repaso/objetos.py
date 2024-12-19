import limpiar
import sys
import os
import time

class punto:
    pass

class rectangulo:
    pass

def graficar(caja,P):
    y = 1
    x = 1

    while True:
        if int(P.y)== 0:
            break
        if y == int(P.y):
            #input("bien")
            break
        else:
            print("\n")
        y = y + 1

    while True:
        if (int(P.x))==0:
            print(f'{".".ljust(int(caja.largo)*4,"-")}.')
            break
        if x == (int(P.x)+1):
            print(f'{"\t"*x}{".".ljust(int(caja.largo)*4,"-")}.')
            break
        else:
            print(f'{"".ljust(1," ")}',end="")
        x = x + 1
    y = 1
    while True:
        if int(P.y)== 0:
            if y == int(caja.alto):
                print(f'{"|".ljust(int(caja.largo)*4," ")}|')
                #input("bien")
                break
            else:
                print(f'{"|".ljust(int(caja.largo)*4," ")}|')
        else:
            if y == int(caja.alto):
                print(f'{"\t"*x}{"|".ljust(int(caja.largo)*4," ")}|')
                #input("bien")
                break
            else:
                print(f'{"\t"*x}{"|".ljust(int(caja.largo)*4," ")}|')
        y = y + 1
    x = 1

    while True:
        if (int(P.x))==0:
            print(f'{".".ljust(int(caja.largo)*4,"-")}.')
            break
        if x == (int(P.x)+1):
            print(f'{"\t"*x}{".".ljust(int(caja.largo)*4,"-")}.')
            break
        else:
            print(f'{"".ljust(1," ")}',end="")
        x = x + 1
    print(" ")
    time.sleep(5)



def inicio():
    caja = rectangulo()
    P = punto()
    P.x = input(f"{"ingrese el punto x: ".upper()}")
    P.y = input(f"{"ingrese el punto y: ".upper()}")
    caja.largo = input(f"{"ingrese el largo: ".upper()}")
    caja.alto =  input(f"{"ingrese el alto: ".upper()}")
    graficar(caja,P)

limpiar.limp()
inicio()