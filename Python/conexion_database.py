# conexion.py
import mysql.connector

def conexion():
    try:
        con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='valeria11',
                database='mydb')
        print("Conexion exitosa")
        return con
    except mysql.connector.Error as e:
        print(f"Problemas de conexion {e}")
        return None

def obtener_cursor(con):
    if con is not None:
        cursor = con.cursor()
        return cursor
    else:
        return None
    


    
    




