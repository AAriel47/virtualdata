import os
def duplicar1(mensaje):
    archivo1 = "datos.dat"
    archivo2 = "datosnuevos.dat"
    #print("bien")
    #while True:
    if os.path.exists(archivo1):
        archi1 = open(archivo1,"r",encoding="utf-8")
        pasar = archi1.read() + mensaje
        if os.path.exists(archivo2):
            archi2 = open(archivo2,"a",encoding="utf-8")
            archi2.write(pasar)
        else:
            with open(archivo2,"w",encoding="utf-8") as archi2:
                archi2.write(pasar)
    else:
        input("archivo inexistente...".upper())
        #break
    archi1.close()
    archi2.close()
#duplicar()