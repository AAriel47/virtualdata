import os
import gramat
    #alumnos = list()
def carmat():
    while (True):
        os.system("cls" if os.name=="nt" else "clear")
        try:
            mcod = int(input("\t Codigo de materia: ".upper()))
        except ValueError:
            input("valor no válido, pulse enter...".upper())
            continue
        mnom = input("\t Nombres de materia: ".upper()).upper()
        mres = input("\t Desea grabar el registro s/n: ".upper())
        if ((mres.lower()=="s") or (mres.lower()=="si")):
            gramat.carmat(mcod, mnom)
            input("El registro se grabo, pulse enter".upper().center(100))
        else:
            input("el registro no se grabo, pulse enter".upper().center(100))
        con = input("\t desea continuar s/n: ".upper())
        os.system("cls" if os.name=="nt" else "clear")
        if ((con.lower()=="si") or((con.lower()=="s"))):
            continue
        else:
            break