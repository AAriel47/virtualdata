import mysql.connector
def carmat(codigo, nombre):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="alumnosnotas",
    )
    cursor = conn.cursor()
    cursor.execute("""insert into materia (codmat, materia)
        values (%s, %s)""",(codigo, nombre)
    )
    conn.commit()
    conn.close()