def listar(codigo):
    import sys
    import os
    sys.path.append('D:\\Aprender\\CapacitacionesNuevas\\VisualStudioCode\\PracticaPython\\PracticaPy1\\virtualdata\\Lib\\site-packages')
    import mysql.connector
    import limpiar
    import time
    while True:
        limpiar.limp()
        print(f"{"-".ljust(45,"-")} {"busqueda de empleado".upper()} {"-".rjust(45,"-")}")

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="datemple"
        )
        cursor = conn.cursor(codigo)
        cursor.execute(f"""select * from nomina where codigo = {codigo}""")
        datos = cursor.fetchall()
        cursor.close()
        empleado = list()
        if datos != []:
            print(f"{"código de empleado:  ".upper()}{codigo}")
            for sacar in datos:
                empleado = list(sacar)

            print(f"{"nombre del empleado:".upper()} {empleado[1]}")
            print(f"{"código de Area:     ".upper()} {empleado[2]}")
            #input()
            time.sleep(2)
            return True
        else:
            print("EMPLEADO INEXISTENTE, PULSE ENTER....")
            #input()
            time.sleep(2)
            return False
        #break
