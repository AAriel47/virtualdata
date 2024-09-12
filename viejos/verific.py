def mostrar():
    print("es función")

blanco=None
blanco=blanco if "blanco" in globals() and blanco else mostrar

if str(type(blanco)) == "<class 'function'>":
    blanco()
else:
    print("es caracter")