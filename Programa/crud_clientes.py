from conexion_database import conexion, obtener_cursor

def ver_datos_cliente():
    con = conexion()
    if con:
        try:
            cursor = obtener_cursor(con)
            if cursor:
                cursor.execute("""
                    SELECT c.id_cliente, c.nombre, p.nombre_proyecto 
                    FROM cliente c 
                    INNER JOIN proyecto p 
                    ON c.id_cliente = p.CLIENTE_id_cliente
                """)
                for row in cursor:
                    print(row)
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        finally:
            if cursor:
                cursor.close()
            con.close()


def modificar_datos_cliente():
    columnas = {
        "1": "id_cliente",
        "2": "nombre"
    }

    print("Introduce la columna que quieras modificar de la tabla Cliente. '1': id_cliente. '2': nombre.")
    opcion_columna = input()
    
    columna = columnas.get(opcion_columna)
    if not columna:
        print("Opcion de columna no valida")
        return
    
    ver_datos_cliente()
    
    print("Introduce el id del cliente: ")
    id = input()
    
    print("Introduce el valor modificado: ")
    valor = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = f'UPDATE cliente SET {columna} = %s WHERE id_cliente = %s'
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

def insertar_datos_cliente():
    print("Introduce los datos del nuevo cliente: ")
    
    print("ID: ")
    id = input()
    
    print("Nombre: ")
    nombre = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = '''
                INSERT INTO cliente (id_cliente, nombre)
                VALUES (%s, %s)
                '''
                cursor.execute(query, (id, nombre))
                con.commit()
                print("Datos insertados correctamente")
                ver_datos_cliente()
            except Exception as e:
                print(f"Error al insertar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")

def eliminar_datos_cliente():
    ver_datos_cliente()
    
    print("Introduce el ID del cliente que quieres eliminar:")
    id = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = 'DELETE FROM cliente WHERE id_cliente = %s'
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

def crud_cliente():
    while True:
        print("Elige la opción que deseas realizar:\n '1': Ver datos de la tabla cliente con su proyecto correspondiente.\n '2': Insertar datos en la tabla cliente.\n '3': Modificar datos de la tabla cliente.\n '4': Eliminar datos de la tabla cliente.")
        opcion = input() 
    
        if opcion == "1":
            ver_datos_cliente()
        elif opcion == "2":
            insertar_datos_cliente()
        elif opcion == "3":
            modificar_datos_cliente()
        elif opcion == "4":
            eliminar_datos_cliente()
        else:
            print("Opcion no valida")
            break


