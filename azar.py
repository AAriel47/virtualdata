"""
Esta es una práctica de lo nuevo que he aprendido\
espero hacerlo bien

"""
import random
import os
import math as mat
os.system("cls" if os.name=="nt" else "clear")
num = random.randint(1,10)
puntos = 10
nu = 4
#print("Hola!  "*3)
#print(mat.sqrt(nu))
i = 10
e = 10
seguir=True
while seguir==True:
    while (i>=1):
        print("-".rjust(36,"-"), "la elección de tú vida".upper(), num, "- oportunidades:".upper(), e,"-".ljust(36,"-"))
        num2 = input(f"mi número favorito es: ".upper())
        try:
            num2 = int(num2)
        except ValueError:
            print ("el valor ingresado no es valido".upper())
            input("presione enter para continuar...".upper())
            os.system("cls" if os.name=="nt" else "clear")
            continue
        if (num == num2 and i==10):
            print("eres el mejor".upper().center(120))
            print(" ".ljust(46,"-"), "ganaste:".upper(), puntos, "felicidades".upper(), " ".rjust(46,"-"))
            print(" ")
            input("presione entre para continuar...".upper())
            break
        elif (num == num2 and 9>=i>=1):
            print("ganaste", puntos, "felicidades".center(100))
            print("-".rjust(118,"-"))
            input("presione entre para continuar...".upper())
            break

        elif (num!=num2 and 10>=i>=1):
            print("perdedor, perdedor, perdedor".upper().center(100))
            print("-".rjust(118,"-"))
            input("presione entre para continuar...".upper())
        i -=1
        e -=1
        puntos -= 1
        os.system("cls" if os.name=="nt" else "clear")
    os.system("cls" if os.name=="nt" else "clear")
    res=input(f"{"<".ljust(40,"-")} {"Deseas seguir jugando s/n:".upper()} {">".rjust(40,"-")} ")
    seguir=res.lower()=="s" or res.lower()=="si"
    if seguir==True:
        os.system("cls" if os.name=="nt" else "clear")
        continue
    else:
        break
os.system("cls" if os.name=="nt" else "clear")