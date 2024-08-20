import os
os.system("cls" if os.name=="nt" else "clear")
class persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar(self):
        print(f"{"Nombre: ".upper()} {self.nombre} {"Edad: ".upper()} {self.edad}")
        print("")

per = persona(input("Ingrese un nombre: ".upper()),input("Ingrese su edad: ".upper()))
per.mostrar()
