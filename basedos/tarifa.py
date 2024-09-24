import os
os.system("cls" if os.name=="nt" else "clear")
tarifa={"Alejandro":100, "Esther": 50, "Romina":40, "Carmen":70}
estudiantes = tarifa.keys()
for estudiante in estudiantes:
    print(" %+20s %+20d" %(estudiante,tarifa[estudiante]))
