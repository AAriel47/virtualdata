

    def veridb(selft):
        import limpiar
        import os
        input(os.getcwd())
        import mysql.connector
        
        i = 0
        linea = list()
        input("llego")
        for registro in selft.lista:
            linea.append(registro.split(","))
        input("li")

        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "datemple",
        )
        cursor=conn.cursor(linea)
        cursor.execute(""" select * from nomina""")
        ver = cursor.fetchall()
        print(ver)
    
