import os
os.system("cls" if os.name=="nt" else "clear")
class empleado:
    def __init__(selft,nombre,edad):
        selft.nombre = nombre
        selft.edad = edad

    def lista(selft):
        print("Nombre: {:>10} - Edad: {:d}".format(selft.nombre,selft.edad))
        print("nombre: %s - edad: %d" %(selft.nombre,selft.edad))

carga=empleado("Alejandro Ariel Uñate".upper(),48)
carga.lista()