import limpiar
import time
class Punto:
    pass
    def ver(blanco):
        print(f"{"("}{str(blanco.x)},{str(blanco.y)}{")"}")
    def medio(caja):
        p = Punto()
        print(f"Punto medio: {"("}{(int(caja.esquina.x)+int(caja.longitud))/2},{(int(caja.esquina.y)+int(caja.altura))/2}{")"}")
        p.x = str((int(caja.esquina.x)+int(caja.longitud))/2)
        p.y = str((int(caja.esquina.y)+int(caja.altura))/2)
        return p
print("")
blanco = Punto()
limpiar.limp()
blanco.x = input("Ingrese X: ")
blanco.y = input("Ingrese y: ")

Punto.ver(blanco)

class rectangulo:
    pass
caja=rectangulo()
caja.altura=input("Ingrese altura: ")
caja.longitud=input("Ingrese la longitud: ")

print(f"altura: {caja.altura}, longitud: {caja.longitud}")

caja.altura=input("Ingrese altura2: ")
caja.longitud=input("Ingrese la longitud2: ")

print(f"altura: {caja.altura}, longitud: {caja.longitud}")

caja.esquina=Punto()
caja.esquina.x=int(input("ingrese esquina x: "))
caja.esquina.y=int(input("Ingrese esquina y: "))

mitad=Punto.medio(caja)
Punto.ver(mitad)
time.sleep(5)
"""class Punto:
    def __init__(selft,x,y):
        selft.x= x
        selft.y= y
    

    limpiar.limp()

    #blanco.x=3.0
    #blanco.y=4.0
    #print(f"{"("}{str(blanco.x)},{str(blanco.y)}{")"}")
    def ver(selft):
        print(f"{"("}{str(selft.x)},{str(selft.y)}{")"}")
        #print(selft.x)

blanco = Punto(input("ingrese x= "),input("ingrese y= "))
blanco.ver()"""