import mysql.connector
def bnot(codmat):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="alumnosnotas",
    )
    cursor = conn.cursor(codmat)
    cursor.execute(f"""select materia from materia where codmat = {codmat}
        """
    )
    valor = cursor.fetchall()
    
    #print (valor)
    conn.commit()
    conn.close()
    return valor
