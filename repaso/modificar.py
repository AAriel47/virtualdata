
def modi2():
    import os
    import limpiar
    import re
    import modif

    emple = list()
    empleados = "empleado.dat"
    patterncod=r"^[1-9]$|^[1-9][0-9]+$"
    #patternnom=r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$"
    #patternarea=r"^[1-9]$|^[1-9][0-9]+$"
    res = ""
    while True:
        limpiar.limp()
        emple.append(input("\tCódigo Empleado: ".upper()))
        codigo=emple[0]
        expreg=re.compile(patterncod)
        val = expreg.match(codigo)
        if (val):
            #print("bien", val.group())
            pass
        else:
            input(f"Valor no valido {emple[0]}, pulse enter...".upper().center(100))
            emple.clear()
            continue
        if (modif.modi(codigo)=="no existe"):
            input(f"{"código inexistente, pulse enter...".upper().center(100)}")
            emple.clear()
            continue

        if (True if(input(f"{"\tDesea continuar s/n: ".upper()}").lower()=="s") else False):
            emple.clear()
            continue
        else:
            limpiar.limp()
            break