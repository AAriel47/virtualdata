import os
import sys
sys.path.append('D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\Lib\\site-packages')
import mysql.connector
import re
mcod = 0

while True:
    os.system("cls" if os.name=="nt" else "clear")
    pattern = r'^[0-9]$|^[0-9]+$'
    expreg = re.compile(pattern)
    mcod= input(f"{"Código de empleado: ".upper()}")
    val = expreg.match(mcod)
    if val==None:
        print(f"{"No es un código numérico, pulse enter...".upper()}")
        input()
        continue
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password = "",
        database="datemple",
    )
    cursor = conn.cursor(mcod)
    cursor.execute(f"""select * from nomina where codigo = {int(mcod)}""")
    valor = list(cursor.fetchall())
    if valor == []:
        print(f"{"código de empleado inexistente, pulse enter...".upper()}")
        input()
    else:
        for val in valor:
            empleado=list((val))
            valor.clear()
            for emp in empleado:
                valor.append(emp)
            break
        os.system("cls" if os.name=="nt" else "clear")
        print(f"{"código de empleado: ".upper()} {mcod}")
        print(f"{"nombre de empleado: ".upper()} {valor[1]}")
        print(f"{"código de área:     ".upper()} {valor[2]}")
        input()
        
    seguir = True if input("Desea continuar s/n: ").lower()=="s" else False
    if seguir:
        continue
    else:
        print(f"{"final de la consulta".upper()}")
        input("PULSE ENTER....")
        break