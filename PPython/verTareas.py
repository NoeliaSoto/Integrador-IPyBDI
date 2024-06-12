from conexion_database import conexion, obtener_cursor

def consulta_database():
    tablas = {
        "1":"cliente",
        "2":"departamento",
        "3":"empleados",
        "4":"proyecto",
        "5":"tareas"
    }
    print("Elige la tabla que quieres ver los datos. 1.Cliente, 2.Departamento, 3.Empleados, 4.Proyectos, 5.Tareas")
    opcion = input()
    
    tabla = tablas.get(opcion)
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            cursor.execute(f"SELECT * FROM {tabla}")
            tareas = cursor.fetchall()
            for tarea in tareas:
                print(tarea)
            cursor.close()
        con.close()
    else:
       print("No se pudo obtener el cursor")

