import limpiar
import listado
import re
import sys
import time
conf = False
pattern = r'^[0-9]$|^[0-9]+$'
sys.path.append('D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\Lib\\site-packages')
import mysql.connector
while True:
    limpiar.limp()
    codigo = input(f"{"codigo del empleado: ".upper()}")
    expreg = re.compile(pattern)
    val = expreg.match(codigo)
    if val == None:
        print(f"{"codigo erroneo, ".upper()}{codigo}".center(100))
        input(f"{"pulse enter...".upper()}".center(100))
        continue

    seguir = listado.listar(codigo)
    if seguir == False:
        continue

    print(f"{" ".ljust(45," ")} {"desea borrar s/n: ".upper()}",end="")
    mres=input()
    print("")
    resp = True if mres.lower()=="s" or mres.lower()=="si" else False
    if resp:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="datemple"
        )
        cursor = conn.cursor(codigo)
        cursor.execute(f"""delete from nomina where codigo={codigo}""")
        conn.commit()
        
        cursor.execute("""select * from nomina""")
        lista=cursor.fetchall()
        lista.sort()
        conn.close()
        for lis in lista:
            print(list(lis))
            time.sleep(1)
        
        print("SE BORRO EL REGISTRO...".center(110))
        print(" ")
        input(f"{" ".ljust(45," ")} PULSE ENTER...")
    else:
        print("NO SE BORRO NINGUN REGISTRO".center(110))
        print(" ")
        input(f"{" ".ljust(45," ")} PULSE ENTER...")
    limpiar.limp()
    print(f"{" ".ljust(45," ")} DESEA CONTINUAR S/N: ", end="")
    conf = input()
    
    if conf.lower() =="s" or conf.lower()=="si":
        continue
    else:
        break