class persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def mostrar(self):
        print(f"{"nombre: ".capitalize()} {self.nombre.upper()} {"apellido: ".capitalize()} {self.apellido.upper()}")

per1 = persona(input("Ingrese el nombre: "), input("Ingrese el apellido: "))

per1.mostrar()