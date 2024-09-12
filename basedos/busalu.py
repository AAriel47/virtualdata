import mysql.connector
def balu(mcodal):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="alumnosnotas",
    )
    cursor = conn.cursor(mcodal)
    cursor.execute(f"""select nombre, apellido from alumnos2 where codalu = {mcodal}
        """
    )
    valor = cursor.fetchall()
    
    #print (valor)
    conn.commit()
    conn.close()
    return valor