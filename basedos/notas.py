import os
import granot
import basedos.busmat as busmat
import busalu
#import string

#va = valor.copy()
    #alumnos = list()
def carnot():
    while (True):
        os.system("cls" if os.name=="nt" else "clear")
        try:
            mcma = int(input("\t Codigo de la materia: ".upper()))
        except ValueError:
            input("valor no válido, pulse enter...".upper())
            continue
        verm=busmat.bnot(mcma)
        if (verm==[]):
            print(f"{"\tel código".upper()} {mcma} {"no existe".upper()}")
            input()
            continue
        mate= "".join(map(str,list(verm[0])))

        print(f"{"\t"}{" Materia: ".upper()} {mate}")
        try:
            mcal = int(input("\t codigo del alumno: ".upper()).upper())
        except ValueError:
            input("valor no válido, pulse enter...".upper())
            continue
        vera = busalu.balu(mcal)
        if (vera==[]):
            print(f"{"\tel código".upper()} {mcal} {"no existe".upper()}")
            input()
            continue
        alum = " ".join(map(str,list(vera[0])))
        print(f"{"\t"}{" alumno: ".upper()} {alum}")        
        try:
            mnot = int(input("\t nota (1-10): ".upper()).upper())
        except ValueError:
            input("valor no válido, pulse enter...".upper())
            continue
        mres = input("\t Desea grabar el registro s/n: ".upper())
        if ((mres.lower()=="s") or (mres.lower()=="si")):
            granot.carnot(mcma, mcal, mnot)
            input("El registro se grabo, pulse enter".upper().center(100))
        else:
            input("el registro no se grabo, pulse enter".upper().center(100))
        con = input("\t desea continuar s/n: ".upper())
        os.system("cls" if os.name=="nt" else "clear")
        if ((con.lower()=="si") or((con.lower()=="s"))):
            continue
        else:
            break