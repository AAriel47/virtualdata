import mysql.connector
def carga(codigo, nombre, apellido):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="alumnosnotas",
    )
    cursor = conn.cursor()
    cursor.execute("""insert into alumnos2 (codalu, nombre, apellido)
        values (%s, %s, %s)""",(codigo, nombre, apellido)
    )
    conn.commit()
    conn.close()