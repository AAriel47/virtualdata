def mostrar1(codigo):
    import limpiar
    import os
    limpiar.limp()
    empleados = "empleado.dat"
    info = list()
    #info2 = list()
    #lineas = list()
    if (os.path.exists(empleados)):
        emple = open(empleados,"r",encoding="utf-8")
        informe = emple.readlines()
        emple.close()
    else:
        input(f"{"empleados.txt, no existe, pulse enter...".center(100).upper()}")
        return

    for inf in informe:
        info.append(inf.split(","))
    i=0
    while i<len(info):
        if (int(info[i][0])==int(codigo)):
            print(f"{"\tcódigo empleado: ".upper()} {info[i][0]}")
            print(f"{"\tnombre empleado: ".upper()} {info[i][1]}")
            print(f"{"\tcódigo de área: ".upper()} {info[i][2]}")            
            print("PULSE ENTER PARA CONTINUAR".center(100))
            return "existe"
        i = i + 1
    return "no existe"



#mostrar()



