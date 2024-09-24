def mostrar(codigo):
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
            print(f"{"código existente: ".upper()} {info[i][0]} {"- código Ingresado: ".upper()} {codigo}".center(100))
            print("EL CÓDIGO DE EMPLEADO YA EXISTE".center(100))
            input("Pulse enter...".upper().center(100))
            return "existe"
        i = i + 1
    return "siga"



#mostrar()



