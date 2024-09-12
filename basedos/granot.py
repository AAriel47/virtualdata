import mysql.connector
import sys
def carnot(codmat, codalum, nota):
    """ esto es para usar desde consola con python granot.py 1 matematica 10
        if (len(sys.argv)!=4):
            print(len(sys.argv))
            input("se requieren 3 argumentos")
            sys.exit(1)
        print(sys.argv[0],sys.argv[1], sys.argv[2], sys.argv[3])
        input()
        sys.exit(1)
    """   

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="alumnosnotas",
    )
    cursor = conn.cursor()
    cursor.execute("""insert into notas (codmat, codalu, nota)
        values (%s, %s, %s)""",(codmat, codalum, nota)
    )
    conn.commit()
    conn.close()
#carnot(1,"mate",1) 