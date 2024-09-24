def ver(codigo):
    import limpiar
    import os
    limpiar.limp()
    empleados = "empleado.dat"
    info = list()
    bor =""
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
            
            bor = input("\tDESEA BORRAR S/N: ")
            if (bor.lower()=="s"):
                mcod = info[i][0]
                del info[i]
                #informe.remove(info[i][0])
                while i < len(info):
                    info[i][0]=mcod
                    mcod = str(int(mcod) + 1)
                    i = i + 1
                carga=[",".join(line) for line in info]

                if(os.path.exists(empleados)):
                    #input(type(info))
                    archi1 = open(empleados,"w",encoding="utf-8")
                    archi1.writelines(carga)
                    archi1.close()
                else:
                    with open(empleados,"w",encoding="utf-8") as archi1:
                        archi1.writelines(carga)
                        archi1.close()

                print("REGISTRO BORRADO CORRECTAMENTE".center(100))
                print("PULSE ENTER PARA CONTINUAR...".center(100))
                input()
            else:
                print("EL REGISTRO NO FUE BORRADO".center(100))
                print("PULSE ENTER PARA CONTINUAR...".center(100))
                input()
            return "existe"
        i = i + 1
    return "no existe"



#mostrar()



