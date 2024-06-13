from crud_empleados import crud_empleados

def mensaje_bienvenida():
    mensaje="Bienvenido al sistema de gestión de RRHH de Constructora Enju Fenoni"
    borde= "*" * (len(mensaje)+2)
    print(borde)
    print("",mensaje)
    print(borde)
mensaje_bienvenida()

def menu_opciones():

 while True:
        print("Seleccione la tabla en la que quieras trabajar:")
        print("1. Tabla Empleados")
        print("2. Tabla Clientes")
        print("3. Tabla Departamentos")
        print("4. Tabla Proyectos")
        print("5. Tabla Tareas")
        opcion = input()
        if opcion == "1":
            crud_empleados()
        elif opcion == "2":
            
        elif opcion == "3":
            
        elif opcion == "4":
           
        elif opcion == "5":
            print("Gracias por usar nuestro sistema.")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")
      
def autenticar_usuario():
    # Datos registrados en el sistema
    nombre_usuario = "elon"
    contrasena = "123"
    intentos = 0  # Inicializa el contador de intentos

    usuario_ingresado = input("Por favor, ingrese su usuario: ") #verifica el nombre de usuario
    while usuario_ingresado != nombre_usuario:
        print("Usuario no registrado")
        usuario_ingresado = input("Por favor, ingrese su usuario: ")
        intentos += 1  # Incrementa el contador de intentos
        if intentos >= 3:
                print("Usuario bloqueado, por favor comuníquese con el administrador del sistema")
                break

    if usuario_ingresado == nombre_usuario: #si el usuario coincide verifica la contraseña incorrecta en 3 intentos y bloquea
        contrasena_ingresada = ""
        while contrasena_ingresada != contrasena and intentos < 3:
            contrasena_ingresada = input("Por favor, ingrese su contraseña: ")
            if contrasena_ingresada != contrasena:
                print("Contraseña incorrecta")
                intentos += 1  # Incrementa el contador de intentos
                if intentos >= 3:
                    print("Usuario bloqueado, por favor comuníquese con el administrador del sistema")
                    break

    # Verificación de usuario y contraseña correctos
    if usuario_ingresado == nombre_usuario and contrasena_ingresada == contrasena: 
        print("Bienvenido,", nombre_usuario)
        # Mostrar función del menú
        menu_opciones()


    
    
        
if __name__ == "__main__":
    autenticar_usuario()