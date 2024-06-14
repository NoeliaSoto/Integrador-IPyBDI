from conexion_database import conexion, obtener_cursor

def ver_datos_departamento():
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            cursor.execute("SELECT * FROM departamento")
            for row in cursor:
                print(row)
            cursor.close()
        con.close()

def modificar_datos_departamento():
    columnas = {
        "1": "id_departamento",
        "2": "nombre_departamento",
        "3": "descripcion_departamento",
        "4": "proyecto",
    }

    print("Introduce la columna que quieras modificar de la tabla Departamento. \n1.id_departamento.\n.Nombre del departamento.\n 3. Descripcion del departamento.\n 4. Proyectos.")
    opcion_columna = input()
    
    columna = columnas.get(opcion_columna)
    if not columna:
        print("Opción de columna no válida")
        return
    
    ver_datos_departamento()

    
    print("Introduce el id del departamento: ")
    id = input()
    
    print("Introduce el valor modificado: ")
    valor = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = f'UPDATE departamento SET {columna} = %s WHERE id_departamento = %s'
                cursor.execute(query, (valor, id))
                con.commit()
                print("Datos correctamente actualizados")
            except Exception as e:
                print(f"Error al actualizar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")

def insertar_datos_departamento():
    print("Introduce los datos del nuevo departamento: ")
    
    print("ID: ")
    id = input()
    
    print("Nombre del departamento: ")
    nombre_departamento = input()
    
    print("Descripción:")
    descripcion_departamento = input()
    
    print("Proyecto:")
    proyecto = input()
    
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = '''
                INSERT INTO DEPARTAMENTO (id_departamento, nombre_departamento, descripcion_departamento, PROYECTO_id_proyecto)
                VALUES (%s, %s, %s, %s)
                '''
                cursor.execute(query, (id, nombre_departamento, descripcion_departamento, proyecto))
                con.commit()
                print("Datos insertados correctamente")
                ver_datos_departamento()
            except Exception as e:
                print(f"Error al insertar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")


def eliminar_datos_departamento():
    ver_datos_departamento()
    
    print("Introduce el ID del departamento que quieres eliminar:")
    id = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = 'DELETE FROM empleados WHERE id_departamento = %s'
                cursor.execute(query, (id,))
                con.commit()
                print("Datos eliminados correctamente")
            except Exception as e:
                print(f"Error al eliminar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")


def crud_departamento():
    while True:
        print("Elige la opción que deseas realizar:\n '1': Ver datos de la tabla departamento.\n '2': Insertar datos en la tabla departamento.\n '4': Modificar datos de la tabla departamento.\n '5': Eliminar datos de la tabla departamento")
        opcion = input() 
    
        if opcion == "1":
            ver_datos_departamento()
        elif opcion == "2":
            insertar_datos_departamento()
        elif opcion == "3":
            modificar_datos_departamento()
        elif opcion == "4":
            eliminar_datos_departamento()
        else:
            print("Opción no válida")
            break


