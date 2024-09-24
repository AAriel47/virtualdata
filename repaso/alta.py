def alt():
    import os
    import limpiar
    import re
    import consulta

    emple = list()
    empleados = "empleado.dat"
    patterncod=r"^[1-9]$|^[1-9][0-9]+$"
    patternnom=r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$"
    patternarea=r"^[1-9]$|^[1-9][0-9]+$"
    res = ""
    while True:
        limpiar.limp()
        emple.append(input("Código Empleado: ".upper()))
        codigo=emple[0]
        expreg=re.compile(patterncod)
        val = expreg.match(codigo)
        if (val):
            #print("bien", val.group())
            pass
        else:
            input(f"Valor no valido {emple[0]}, pulse enter...".upper())
            emple.clear()
            continue
        if (consulta.mostrar(codigo)=="existe"):
            emple.clear()
            continue
        print("Código Empleado: ",emple[0])
        emple.append(", ")
        emple.append(input("Nombre Empleado: ".upper()))
        nombre = emple[2]
        expreg1 = re.compile(patternnom)
        val1 = expreg1.match(nombre)


        if not (val1):
            input(f"Valor no valido {emple[2]}, ejempo 'Carol Corina Correa', pulse enter...")
            emple.clear()
            continue
        emple.append(", ")
        emple.append(input("Código de Area:  ".upper()))
        area = emple[4]
        expreg2 = re.compile(patternarea)
        val2 = expreg2.match(area)
        if not(val2):
            input(f"Valor no valido {emple[4]}, pulse enter...".upper().center(100))
            emple.clear()
            continue
        emple.append("\n")
        #print(emple)
        res = input("Desea Grabar s/n: ".upper()).lower()
        if res=="s" or res=="si":
            if (os.path.exists(empleados)):
                arch = open(empleados,"a",encoding="utf-8")
                arch.writelines(emple)
                arch.close()
            else:
                with open(empleados,"w",encoding="utf-8") as arch:
                    arch.writelines(emple)
                    arch.close()

            print("se grabó correctamente".upper().center(100))
            input("Pulse enter para continuar...".upper().center(100))
        else:
            print("No se grabó el registro".upper().center(100))
            input("Pulse enter para continuar...".upper().center(100))

        if (True if(input("Desea continuar s/n: ".upper()).lower()=="s")else False):
            emple.clear()
            continue
        else:
            limpiar.limp()
            break