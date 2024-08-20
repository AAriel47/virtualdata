#pip install mysql-connector-python
import os
import mysql.connector
os.system('cls' if os.name=='nt' else 'clear')
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "alumno"
)
cursor = conn.cursor()

cursor.execute('''
    insert into alumnos (nombre, apellido)
    values(%s, %s)''',(input("Ingrese el Nombre: ".upper()).upper(), input("Ingrese el apellido: ".upper()).upper())
)
conn.commit()
conn.close()
