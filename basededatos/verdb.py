import os

import mysql.connector
def verlos():
    os.system("cls" if os.name=="nt" else "clear")
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "alumnosnotas",
        )
    cursor = conn.cursor()
    cursor.execute("""select * from alumnos"""
            )
        #conn.commit()
    im = cursor.fetchall()
    conn.close()
    i=0
    for datos in im:
        print(f"{"\t"}{datos}")
        i +=1
        if (i==10):
            input("presione enter para continuar...".upper())
            os.system("cls" if os.name=="nt" else "clear")
    input("presione enter para continuar1...".upper())
    os.system("cls" if os.name=="nt" else "clear")
