import limpiar
import os
import re
limpiar.limp
import sys
sys.path.append('D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\Lib\\site-packages')
import mysql.connector

#import consultbd

linea = list()
archivo = "empleado.dat"
i = 0
while True:
    if os.path.exists(archivo):
        datos = open(archivo,"r",encoding="utf-8")
        lista = datos.readlines()
        datos.close()
    else:
        print(f"{"-".ljust(45,"-")}{" base de datos ".upper()}{"-".rjust(45,"-")}")
        print()
        print(" ".ljust(32," "),"%s" %("el archivo: ".upper()),"{:s}".format(archivo.upper()),"%s" %("no existe...".upper()))
        print()
        print(f"{"-".ljust(45,"-")}{" base de datos ".upper()}{"-".rjust(45,"-")}")
        input()
        #break
    
        
        
    for registro in lista:
        linea.append(registro.split(","))

    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "datemple",
    )
    cursor=conn.cursor(linea)
    cursor.execute(""" select * from nomina""")
    ver = cursor.fetchall()
    #input(ver)
    #cursor.close()

    if ver == []:
        input("entro primero")
        mcod = 0
        mnom = "" 
        marea = 0
        cursor1=conn.cursor()
        while i < len(linea):
            mcod = linea[i][0]
            mnom = linea[i][1]
            marea = linea[i][2]

            cursor1.execute("""insert into nomina(codigo, nombre, area)
            values(%s, %s, %s)""",(mcod, mnom,marea))
            i = i + 1
            #print(mcod,mnom,marea)
            #input()
        conn.commit()
        cursor1.execute("""select * from nomina""")
        ver1 = cursor1.fetchall()            
        print(ver1)
    else:
        mcod=0
        i = 0
        cursor1=conn.cursor(mcod)
        while i < len(linea):
            mcod=int(linea[i][0])
            
            cursor1.execute(f"""select * from nomina where codigo = {mcod}""")
            ver1=cursor1.fetchall()
            if ver1==[]:
                cursor1.execute("""insert into nomina(codigo, nombre, area)
                                values(%s, %s, %s)""",(int(linea[i][0]), linea[i][1], int(linea[i][2]))
                )
            i = i + 1
        conn.commit()
    conn.close()
    break
