import os
os.system("cls" if os.name=="nt" else "clear")
Valor = 12
otro = 88
def mostrar():
    global Valor
    print(otro)
    #otro = input("otro: ")
    print(Valor)
    Valor = int(input ("Ingrese un numero: "))
    print(Valor)

def listo():
    global Valor
    print(Valor)
    Valor = input("Ingrese otro número: ")
    print(Valor)

mostrar()
listo()