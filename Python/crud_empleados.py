from conexion_database import conexion, obtener_cursor

def ver_datos_empleados():
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            cursor.execute("SELECT * FROM empleados")
            for row in cursor:
                print(row)
            cursor.close()
        con.close()

def modificar_datos_empleados():
    columnas = {
        "1": "dni",
        "2": "fecha_nacimiento",
        "3": "genero",
        "4": "nombre_completo",
        "5": "numero_telefono",
        "6": "fecha_contrato",
        "7": "direccion",
        "8": "puesto",
        "9": "departamento"
    }

    print("Introduce la columna que quieras modificar de la tabla Empleados. 1.Dni. 2. Fecha de nacimiento. 3. Genero. 4. Nombre completo. 5. Numero de telefono. 6. Fecha de contrato. 7. Direccion. 8. Puesto. 9. Departamento")
    opcion_columna = input()
    
    columna = columnas.get(opcion_columna)
    if not columna:
        print("Opción de columna no válida")
        return
    
    ver_datos_empleados()

    
    print("Introduce el DNI del empleado: ")
    dni = input()
    
    print("Introduce el valor modificado")
    valor = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = f'UPDATE empleados SET {columna} = %s WHERE dni = %s'
                cursor.execute(query, (valor, dni))
                con.commit()
                print("Datos correctamente actualizados")
            except Exception as e:
                print(f"Error al actualizar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")

def insertar_datos_empleados():
    print("Introduce los datos del nuevo empleado:")
    
    print("DNI:")
    dni = input()
    
    print("Fecha de nacimiento (YYYY-MM-DD):")
    fecha_nacimiento = input()
    
    print("Género:")
    genero = input()
    
    print("Nombre completo:")
    nombre_completo = input()
    
    print("Número de teléfono:")
    numero_telefono = input()
    
    print("Fecha de contrato (YYYY-MM-DD):")
    fecha_contratado = input()
    
    print("Dirección:")
    direccion = input()
    
    print("Puesto:")
    puesto = input()
    
    print("Departamento:")
    departamento = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = '''
                INSERT INTO empleados (dni, fecha_nacimiento, genero, nombre_completo, numero_telefono, fecha_contratado, direccion, puesto, DEPARTAMENTO_id_departamento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(query, (dni, fecha_nacimiento, genero, nombre_completo, numero_telefono, fecha_contratado, direccion, puesto, departamento))
                con.commit()
                print("Datos insertados correctamente")
                ver_datos_empleados()
            except Exception as e:
                print(f"Error al insertar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")


def eliminar_datos_empleados():
    ver_datos_empleados()
    
    print("Introduce el DNI del empleado que quieres eliminar:")
    dni = input()
    
    con = conexion()
    if con:
        cursor = obtener_cursor(con)
        if cursor:
            try:
                query = 'DELETE FROM empleados WHERE dni = %s'
                cursor.execute(query, (dni,))
                con.commit()
                print("Datos eliminados correctamente")
            except Exception as e:
                print(f"Error al eliminar los datos: {e}")
                con.rollback()
            cursor.close()
        con.close()
    else:
        print("No se pudo conectar a la base de datos")


def crud_empleados():
    while True:
        print("Elige la opción que deseas realizar: 1. Ver datos de la tabla empleados. 2. Insertar datos en la tabla empleados. 3. Modificar datos de la tabla empleado. 4. Eliminar datos de la tabla empleados")
        opcion = input() 
    
        if opcion == "1":
            ver_datos_empleados()
        elif opcion == "2":
            insertar_datos_empleados()
        elif opcion == "3":
            modificar_datos_empleados()
        elif opcion == "4":
            eliminar_datos_empleados()
        else:
            print("Opción no válida")
            break

crud_empleados()
