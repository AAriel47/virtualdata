import mysql.connector
def cardat(codigo1, nombre1, apellido1, materia1, nota1):
    
    global mysql
    #print(codigo1, nombre1, apellido1, materia1, nota1,"base")
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "alumnosnotas",
    )
    cursor = conn.cursor()
    cursor.execute("""insert into alumnos (codigo, nombre, apellido, materia, nota)
        values(%s,%s,%s,%s,%s)""",(codigo1,nombre1,apellido1,materia1,nota1)
        )
    conn.commit()
    conn.close()
