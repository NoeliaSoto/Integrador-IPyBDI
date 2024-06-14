
from conexion_database import conexion, obtener_cursor

def ver_datos_proyectos():
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                cursor.execute("SELECT * FROM proyecto WHERE fecha_finalizacion IS NULL;")
                for row in cursor:
                    print(row)
            except Exception as e:
                print(f"Error al obtener los datos: {e}")
            finally:
                cursor.close()
        con.close()

def modificar_datos_proyectos():
    columnas = {
        "1": "nombre_proyecto",
        "2": "estado_proyecto",
        "3": "fecha_inicio",
        "4": "fecha_finalizacion"
    }

    print("Introduce la columna que quieras modificar de la tabla Proyecto. 1. Nombre del proyecto. 2. Estado del proyecto. 3. Fecha de inicio. 4. Fecha de finalización.")
    opcion_columna = input().strip()
    
    columna = columnas.get(opcion_columna)
    if not columna:
        print("Opción de columna no válida")
        return
    
    ver_datos_proyectos()

    print("Introduce el ID del proyecto: ")
    id_proyecto = input().strip()
    
    print("Introduce el valor modificado:")
    valor = input().strip()
    
    if columna in ["fecha_inicio", "fecha_finalizacion"] and not validar_fecha(valor):
        print("Fecha no válida. Use el formato YYYY-MM-DD.")
        return
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = f'UPDATE proyecto SET {columna} = %s WHERE id_proyecto = %s'
                cursor.execute(query, (valor, id_proyecto))
                con.commit()
                print("Datos correctamente actualizados")
            except Exception as e:
                print(f"Error al actualizar los datos: {e}")
                con.rollback()
            finally:
                cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")

def insertar_datos_proyectos():
    print("Introduce los datos del nuevo proyecto:")
    
    nombre_proyecto = input("Nombre del proyecto: ").strip()
    estado_proyecto = input("Estado del proyecto: ").strip()
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
    fecha_finalizacion = input("Fecha de finalización (YYYY-MM-DD): ").strip()
    
    if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_finalizacion):
        print("Una o más fechas no son válidas. Use el formato YYYY-MM-DD.")
        return
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = '''
                INSERT INTO proyecto (nombre_proyecto, estado_proyecto, fecha_inicio, fecha_finalizacion)
                VALUES (%s, %s, %s, %s)
                '''
                cursor.execute(query, (nombre_proyecto, estado_proyecto, fecha_inicio, fecha_finalizacion))
                con.commit()
                print("Datos insertados correctamente")
                ver_datos_proyectos()
            except Exception as e:
                print(f"Error al insertar los datos: {e}")
                con.rollback()
            finally:
                cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")

def eliminar_datos_proyectos():
    ver_datos_proyectos()
    
    id_proyecto = input("Introduce el ID del proyecto que quieres eliminar: ").strip()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = 'DELETE FROM proyecto WHERE id_proyecto = %s'
                cursor.execute(query, (id_proyecto,))
                con.commit()
                print("Datos eliminados correctamente")
            except Exception as e:
                print(f"Error al eliminar los datos: {e}")
                con.rollback()
            finally:
                cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")

def validar_fecha(fecha):
    from datetime import datetime
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def crud_proyectos():
    while True:
        print("Elige la opción que deseas realizar:\n '1': Ver datos de la tabla proyectos en curso.\n '2': Insertar datos en la tabla proyectos.\n '3': Modificar datos de la tabla proyectos.\n '4': Eliminar datos de la tabla proyectos.")
        opcion = input().strip()
    
        if opcion == "1":
            ver_datos_proyectos()
        elif opcion == "2":
            insertar_datos_proyectos()
        elif opcion == "3":
            modificar_datos_proyectos()
        elif opcion == "4":
            eliminar_datos_proyectos()
        else:
            print("Opción no válida")
            break

