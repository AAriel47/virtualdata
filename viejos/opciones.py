import os
os.system("cls" if os.name=="nt" else "clear")
def mostrar():
    print("hola... como estas?".upper())
    input()
    #return

blanco = None
blanco = blanco if "blanco" in globals() and blanco else mostrar
print(type(blanco))

if str(type(blanco))=="<class 'function'>":
    blanco()
else:
    print("Caracteres alfanumericos".upper())

