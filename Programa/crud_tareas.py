from conexion_database import conexion, obtener_cursor

def ver_datos_tareas():
    con = conexion()
    if con:
        try:
            cursor = obtener_cursor(con)
            if cursor:
                cursor.execute("""
                    SELECT t.id_tareas, t.tarea, t.fecha_inicio, t.fecha_finalizacion, p.nombre_proyecto
                    FROM tareas t
                    INNER JOIN proyecto p ON t.PROYECTO_id_proyecto = p.id_proyecto
                """)
                for row in cursor:
                    print(row)
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        finally:
            if cursor:
                cursor.close()
            con.close()


def modificar_datos_tareas():
    columnas = {
        "1": "id_tareas",
        "2": "tarea",
        "3": "fecha_inicio",
        "4": "fecha_finalizacion",
        "5": "PROYECTO_id_proyecto"
    }

    print("Introduce la columna que quieras modificar de la tabla tareas. \n1. Código de tarea. \n2. Denominación de tarea. \n3. Fecha de inicio. \n4. Fecha de finalización. \n5. Proyecto.")
    opcion_columna = input()
    
    columna = columnas.get(opcion_columna)
    if not columna:
        print("Opción de columna no válida")
        return
    
    ver_datos_tareas()

    print("Introduce el código de tarea: ")
    id_tareas = input()
    
    print("Introduce el valor modificado: ")
    valor = input()
    
    con = conexion()
    if con:
        try:
            cursor = obtener_cursor(con)
            if cursor:
                query = f'UPDATE tareas SET {columna} = %s WHERE id_tareas = %s'
                cursor.execute(query, (valor, id_tareas))
                con.commit()
                print("Datos correctamente actualizados")
        except Exception as e:
            print(f"Error al actualizar los datos: {e}")
            con.rollback()
        finally:
            if cursor:
                cursor.close()
            con.close()
    else:
        print("No se pudo conectar a la base de datos")


def insertar_datos_tareas():
    print("Introduce los datos de la nueva tarea:")
    
    print("Código de tarea:")
    id_tareas = input()
    
    print("Denominación de tarea:")
    tarea = input()
    
    print("Fecha de inicio (YYYY-MM-DD):")
    fecha_inicio = input()
    
    print("Fecha de finalización (YYYY-MM-DD):")
    fecha_finalizacion = input()
    
    print("Proyecto")
    proyecto = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = '''
                INSERT INTO tareas (id_tareas, tarea, fecha_inicio, fecha_finalizacion, PROYECTO_id_proyecto)
                VALUES (%s, %s, %s, %s, %s)
                '''
                cursor.execute(query, (id_tareas, tarea, fecha_inicio, fecha_finalizacion, proyecto))
                con.commit()
                print("Datos insertados correctamente")
                ver_datos_tareas()
            except Exception as e:
                print(f"Error al insertar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")


def eliminar_datos_tareas():
    ver_datos_tareas()
    
    print("Introduce el código de la tarea que quieres eliminar:")
    id_tareas = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = 'DELETE FROM tareas WHERE id_tareas = %s'
                cursor.execute(query, (id_tareas,))
                con.commit()
                print("Datos eliminados correctamente")
            except Exception as e:
                print(f"Error al eliminar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")


def crud_tareas():
    while True:
        print("Elige la opción que deseas realizar:\n '1': Ver datos de la tabla tareas con su correspondiente proyecto.\n '2': Insertar datos en la tabla tareas.\n '3': Modificar datos de la tabla tareas.\n '4': Eliminar datos de la tabla tareas.")
        opcion = input() 
    
        if opcion == "1":
            ver_datos_tareas()
        elif opcion == "2":
            insertar_datos_tareas()
        elif opcion == "3":
            modificar_datos_tareas()
        elif opcion == "4":
            eliminar_datos_tareas()
        else:
            print("Opción no válida")
            break


##
