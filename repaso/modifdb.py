import limpiar
import listado
import sys
sys.path.append('D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\Lib\\site-packages')
import os
import re
pattern = r'^[0-9]$|^[0-9]+$'
patternom = r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$"
import time
import mysql.connector

import csv
borrar = [1,2,3]
datos = open("practicavba.csv","a",encoding="utf-8")
datos.write()

while True:
    limpiar.limp()
    codigo = input(f"{"Código de empleado: ".upper()}")
    expreg = re.compile(pattern)
    val = expreg.match(codigo)
    if val==None:
        print(f"{"código de empleado no válido...".upper().center(100)}")
        time.sleep(1)
        print(f"{"pulse enter para continuar...".upper().center(100)}")
        continue
    valor = listado.listar(codigo)
    if valor ==None:
        print(f"{"código de empleado inexistente...".upper().center(100)}")
        time.sleep(1)
        input(f"{"pulse enter para continuar...".upper().center(100)}")
        continue
    print("")
    print(f"{"-".ljust(43,"-")} {"modificación de empleados".upper()} {"-".rjust(43,"-")}")
    nombre = input(f"{"Nombre de empleado: ".upper()}")
    exrenom = re.compile(patternom)
    val1 = exrenom.match(nombre)
    if val1 == None:
        print(f"{"nombre de empleado no válido...".upper().center(100)}")
        time.sleep(1)
        input(f"{"pulse enter para continuar...".upper().center(100)}")
        continue

    area = input(f"{"área de trabajo: ".upper()}")
    exrearea = re.compile(pattern)
    val2 = exrearea.match(area)
    if val2 == None:
        print(f"{"código de area no válido...".upper().center(100)}")
        time.sleep(1)
        input(f"{"pulse enter para continuar...".upper().center(100)}")
        continue
    mres = input(f"{"desea modificar el registro s/n:".upper()}")
    if mres.lower()=="s" or mres.lower()=="si":
        conn= mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="datemple"
        )
        cursor = conn.cursor(codigo)

        cursor.execute(
            """update nomina set nombre=%s, area=%s where codigo = %s""",(nombre, area, codigo)
        )
        conn.commit()
        cursor.execute("""select * from nomina""")
        nomina = cursor.fetchall()
        
        nomina.sort()
        #print(nomina)
        #input("nomina")
        time.sleep(1)
        for nom in nomina:
            print(list(nom))
            time.sleep(1)
        conn.close()
        
        print("")
        print(f"{"registro actualizado".upper().center(100)}")
        time.sleep(1)
        input(f"{" ".ljust(42," ")}{"PULSE ENTER..."}")
    else:
        print(f"{"no se actualizó".upper().center(100)}")
        time.sleep(1)
        input(f"{" ".ljust(42," ")}{"PULSE ENTER..."}")
    salir = input(f"{"desea continuar s/n: ".upper()}")
    if salir.lower()=="s" or salir.lower()=="si":
        continue
    else: 
        break