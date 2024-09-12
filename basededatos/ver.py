import os
os.system("cls" if os.name=="nt" else "clear")
def consul():
    datos = "alumnos.txt"
    if (os.path.exists(datos)):
        archi = open(datos,"r",encoding="utf-8")
        alumnos = archi.readlines()
        archi.close()
    else:
        mensaje = "archivo inexistente".upper()
        return mensaje
    print(f"{"-".rjust(40,"-")} {"< listado de alumnos >".upper()} {"-".ljust(40,"-")}")
    for i in alumnos:
        print(i)
    #return "si"
#consul()