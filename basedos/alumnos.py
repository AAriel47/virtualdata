import os
import grabar
    #alumnos = list()
def caralu():
    while (True):
        os.system("cls" if os.name=="nt" else "clear")
        try:
            mcod = int(input("\t Codigo del alumno: ".upper()))
        except ValueError:
            input("valor no válido, pulse enter...".upper())
            continue
        mnom = input("\t Nombres del alumno: ".upper()).upper()
        mapl = input("\t Apellido del Alumno: ".upper()).upper()
        mres = input("\t Desea grabar el registro s/n: ".upper())
        if ((mres.lower()=="s") or (mres.lower()=="si")):
            grabar.carga(mcod, mnom, mapl)
            input("El registro se grabo, pulse enter".upper().center(100))
        else:
            input("el registro no se grabo, pulse enter".upper().center(100))
        con = input("\t desea continuar s/n: ".upper())
        os.system("cls" if os.name=="nt" else "clear")
        if ((con.lower()=="si") or((con.lower()=="s"))):
            continue
        else:
            break