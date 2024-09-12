import os
os.system("cls" if os.name=="nt" else "clear")
import ver
men=ver.consul()
if(men==None):
    print("alumnos.dbf".upper().center(100))
    #input()
else:
    print(men)
    input()
print(f"{"-".rjust(40,"-")} {"< final del listado >".upper()} {"-".ljust(40,"-")}")
input()
os.system("cls" if os.name=="nt" else "clear")