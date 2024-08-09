import os
os.system("cls" if os.name=="nt" else "clear")
"""class Auto:
    def __init__(selft, marca, modelo):
        selft.marca=marca
        selft.modelo=modelo
    
    def mostrar(selft):
        print(f"{"marca de auto:".upper()} {(selft.marca.upper())} {"modelo:".upper()} {selft.modelo}")

vehiculo = Auto("ford",1923)
vehiculo.mostrar()"""

def ver():
    print("hola a todos")

blanco = None
blanco = blanco if "blanco" in globals() and blanco else ver

if ((str(type(blanco)))=="<class 'function'>"):
    blanco()
else:
    print("listo")