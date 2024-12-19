import os
import sys
import limpiar
import time
import re
os.chdir("repaso")
class triangulo:
    pass
def gratri(origen, area):
    tri = {"x": origen.x, "y": origen.y, "base": area.base, "altura":area.altura}
    #print(origen.x, origen.y)
    #print(area.base, area.altura)
    pmedio= (int(tri["base"])/2)
    i = 1
    o = 1
    a = 1
    e = 1
    while True:
        if i == int(tri["y"]):
            break
        print("")    
        i = i + 1
    altura = int(tri["altura"])

    while True:
        if o > (int(tri["x"])+ pmedio):
            if int(tri["x"])==0:
                print(f"{"|".ljust(0," ")}{"\\".rjust(int(a)," ")}")
            #sal = a + a
            else:
                print(f"{"/".ljust(int(a)," ")}{"\\".rjust(a," ")}")
            a = a + 1
            
            #print(a)
            #print(int(tri["x"])+ pmedio)
            e = e + 1
            o = 0
        else:
            if o < ((int(tri["x"])+ pmedio)-e):
                if int(tri["x"]) == 0:
                    print(f"{"".ljust(0," ")}", end="")
                else:
                    print(f"{"".ljust(1," ")}", end="")

        o = o + 1
        if a >altura:
            if int(tri["x"])==0:
                izq = 0
                der = int(tri["altura"])+2
            else:
            #input(f"{a} {altura}")
                if int(tri["altura"])%2==0 and int(tri["base"])%2!=0:
                    izq = int(int(tri["x"])+ pmedio)-a
                    der = (int(tri["altura"]) * 2)+2
                elif int(tri["altura"])%2!=0 and int(tri["base"])%2!=0:
                    izq = int(int(tri["x"])+ pmedio)-a
                    der = (int(tri["altura"]) * 2)+2

                else:
                    izq = int(int(tri["x"])+ pmedio)-(a+1)
                    der = (int(tri["altura"]) * 2)+2
            break 
    #print(f"{"".ljust(int(tri["x"])-5," ")}{"-".rjust(int(tri["base"])+2,"-")}")
    print(f"{"".ljust(izq," ")}{"-".rjust(der,"-")}")
    time.sleep(5)
    print()
    print(f"{"base del triangulo: ".upper()}{tri['base']}{" - Altura del triángulo: ".upper()}{tri['altura']} - {"formula: (base*altura)/2"}".center(120))
    print()
    print(f"{"".ljust(42," ")} Area del Triángulo: {(int(area.base)*int(area.altura)/2)}")




def tri():
    pattern = r'^[0-9]$|^[1-9][0-9]$'
    expreg = re.compile(pattern)
    patterny = r'^[1-9]$|^[1-9][0-9]$'
    expregy = re.compile(patterny)
    patternb = r'^[1-9]$|^[1-9][0-9]$'
    expregb = re.compile(patternb)
    patterna = r'^[1-9]$|^[1-9][0-9]$'
    exprega = re.compile(patterna)
    while True:
        limpiar.limp()
        origen = triangulo()
        origen.x= input("Ingrese x= ")
        valx = expreg.match(origen.x)
        if valx == None:
            print(f"{"valor no permitido: ".upper()} {origen.x} {"String" if origen.x.isalpha()==True else "Float"}")
            time.sleep(2)
            continue
        
        origen.y= input("ingrese y= ")
        valy = expregy.match(origen.y)
        if valy == None:
            print(f"{"valor no permitido: ".upper()} {origen.y} {"String" if origen.y.isalpha()==True else "Float"}")
            time.sleep(2)
            continue

        area = triangulo()
        area.base = input("ingrese la base= ")
        valb = expregb.match(area.base)
        if valb ==None:
            print(f"{"valor no permitido: ".upper()} {area.base} {"String" if area.base.isalpha()==True else "Float"}")
            time.sleep(2)
            continue

        area.altura = input("Ingrese la altura= ")
        vala = exprega.match(area.altura)
        if vala ==None:
            print(f"{"valor no permitido: ".upper()} {area.altura} {"String" if area.altura.isalpha()==True else "Float"}")
            time.sleep(2)
            continue
        time.sleep(1)
        gratri(origen, area)
        time.sleep(3)
        #os.system("cls" if os.name=="nt" else "clear")
        print()
        res = input(f"{"desea seguir graficando S/N: ".capitalize().rjust(70," ")}")
        if res.lower() == "s" or res.lower()=="si":
            continue
        else:
            break
    print("")
    print(f"{"Gracias por participar...".upper()}".center(113))
    time.sleep(4)
    limpiar.limp()
tri()
