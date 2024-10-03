def modi(codigo):
    import limpiar
    import os
    import re
    limpiar.limp()
    empleados = "empleado.dat"
    info = list()
    bor =""
    patterncod=r"^[1-9]$|^[1-9][0-9]+$"
    patternnom=r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$"
    patternarea=r"^[1-9]$|^[1-9][0-9]+$"
    #info2 = list()
    #lineas = list()
    if (os.path.exists(empleados)):
        emple = open(empleados,"r",encoding="utf-8")
        informe = emple.readlines()
        emple.close()
        if len(informe)==0:
                print("ARCHIVO NO POSEE REGISTROS...".center(100))
                print("PULSE ENTER PARA CONTINUAR...".center(100))
                input()
                return
    else:
        input(f"{"empleado.dat, no existe, pulse enter...".center(100).upper()}")
        return

    for inf in informe:
        info.append(inf.split(","))
    i=0
    while i<len(info):
        limpiar.limp()
        if (int(info[i][0])==int(codigo)):
            print(f"{"\tcódigo empleado: ".upper()} {info[i][0]}")
            print(f"{"\tnombre empleado: ".upper()} {info[i][1]}")
            print(f"{"\tcódigo de área:  ".upper()} {info[i][2]}")            

            mod = input("\tDESEA MODIFICAR S/N: ")
            if (mod.lower()=="s"):
                print(f"{"\tcódigo empleado: ".upper()} {info[i][0]}")

                info[i][1]=input(f"{"\tnombre empleado: ".upper()}")
                
                nombre = info[i][1]
                expreg1 = re.compile(patternnom)
                val1 = expreg1.match(nombre)


                if not (val1):
                    input(f"Valor no valido {info[i][1]}, ejempo 'Carol Corina Correa', pulse enter...")
                    info.clear()
                    continue

                info[i][2]=input(f"{"\tCódigo de Area:  ".upper()}")

                area = info[i][2]
                expreg2 = re.compile(patternarea)
                val2 = expreg2.match(area)
                if not(val2):
                    input(f"Valor no valido {info[i][2]}, pulse enter...".upper().center(100))
                    info.clear()
                    continue
                info[i][2]=info[i][2]+"\n"
                carga=[",".join(line) for line in info]
                print(carga)
                if(os.path.exists(empleados)):
                    #input(type(info))
                    archi1 = open(empleados,"w",encoding="utf-8")
                    archi1.writelines(carga)
                    archi1.close()
                else:
                    with open(empleados,"w",encoding="utf-8") as archi1:
                        archi1.writelines(carga)
                        archi1.close()

                print("REGISTRO MODIFICADO CORRECTAMENTE".center(100))
                print("PULSE ENTER PARA CONTINUAR...".center(100))
                input()
            else:
                print("EL REGISTRO NO FUE MODIFICADO".center(100))
                print("PULSE ENTER PARA CONTINUAR...".center(100))
                input()
            return "existe"
        i = i + 1
    return "no existe"



#mostrar()



