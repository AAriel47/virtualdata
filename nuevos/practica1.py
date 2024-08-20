import os
import random
#numeros = [1,2,10,15,9,8,29,18,5,7]
numeros=[0]*10
encontrados=[]
ordenado = []
mi = 0
ma = 0
def generar():
    global numeros
    global ordenado
    global mi
    global ma
    for i in range(10):
        numeros[i]=random.randint(1,20)
    print(numeros)
    numeros.sort()
    #ordenado = numeros
    mi = numeros[0]
    ma = numeros[-1]

def comparar(min,max):
    global numeros
    global encontrados
    #global encon
    for num in numeros:
        if(int(min)<=int(num)<=int(max)):
            encontrados.insert(len(encontrados),num)
    encontrados.sort()
    print(encontrados)



def mostrar():
    seguir=""
    while (True):
        global encontrados
        os.system("cls" if os.name=="nt" else "clear")
        generar()
        print(f"{"valor minimo:".upper()} {mi} - {"valor máximo:".upper()} {ma}")
        try:
            min = input("Ingrese el número mínimo: ")
            if not(int(min)>=int(mi)):
                input("el mínimo ingresado no es válido".upper())
                continue
            max = input("Ingrese el número máximo: ")
            if not(int(max)<=int(ma)):
                input("el máximo ingresado no es válido".upper())
                continue
            if (int(min)>=int(max)):
                input("los valores mínimos y máximos son iguales".upper())
        except ValueError:
            input("El valor ingresado no es valido ".upper() + "'String'," + " pulse enter...".upper())
            continue

        comparar(min,max)
        seguir = input("Desea seguir s/n: ")
        if ((seguir.lower()=="s")or(seguir.lower()=="si")):
            encontrados = []
            continue
        else:
            break

mostrar()


