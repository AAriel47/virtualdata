import os
os.system("cls" if os.name=="nt" else "clear")
b = "ariel"
"""if (b.find("ariel")!=-1):
    print("existe")

if (b in "ariel"):
    print (f"si existe {b.capitalize()}")
if ((b.isalpha()) & (b.find("ariel")!=-1)):
    print(f"{"si existe ".capitalize()} {b.capitalize()}")"""

alumnos=[["alejandro", "ariel", "uñate"], ["rosa", "esther", "romero"], ["rosario", "del Carmen","nieva"],["mónica","silvina","romero"]]
i = 0
grabar = list()
for alumno in alumnos:
    
    control=[]
    largo= 0
    datos = "alumnos.txt"
    print(f"{"\t"}{"alumno: ".capitalize()}", end="")
    for alum in alumno:
        if 0 <= i <=2:
            print(f"{alum.capitalize()} ", end="")
            control += alum 
            if len(grabar)==0:
                grabar = alum.capitalize() + " "
            else:
                grabar = str(grabar) + alum.capitalize() + " "
        if (i==2):
            #largo = 78-(len(control)+8)
            #print(largo)
            grabar = grabar + "\n"
            print(f"{"*".rjust(int(66-(len(control)+8)),"*")}")
            print(f"{"\t""-".ljust(70,"-")}")
        i += 1
    i=0
print(f"{"\t""-".ljust(26,"-")} {"final del informe ".capitalize()}{"-".rjust(25,"-")}")
print()

if os.path.exists(datos):
    archi = open(datos,"a",encoding="utf-8")
    archi.writelines(grabar)
    archi.writelines(f"{"-".ljust(26,"-")} {"final del informe ".capitalize()}{"-".rjust(25,"-")}{"\n"}")
else:
    with open(datos,"w",encoding="utf-8") as archi:
        archi.writelines(grabar)
        archi.writelines(f"{"-".ljust(26,"-")} {"final del informe ".capitalize()}{"-".rjust(25,"-")}{"\n"}")
"""for ir in range(0,10):
    print(ir)
    num=[1,2,3,4]
    """