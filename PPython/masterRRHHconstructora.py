from cliente import clientes
from empleado import empleados
from proyectos import proyecto

def mensaje_bienvenida():
    mensaje="Bienvenido al sistema de gestión de RRHH de Constructora Enju Fenoni"
    borde= "*" * (len(mensaje)+2)
    print(borde)
    print("",mensaje)
    print(borde)
mensaje_bienvenida()

def menu_opciones():
    print("Seleccione una opción:")
    print("1. Empleados")
    print("2. Departamentos, proyectos y tareas")
    print("3. Clientes")
    print("4. Salir")
    
    opcion=""
    while opcion!="4":
        opcion = input()
        if opcion == "1":
            empleados()
        elif opcion == "2":
            proyecto()
        elif opcion == "3":
            clientes()
        elif opcion == "4":
            print("Gracias por usar nuestro sistema.")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")
      
def autenticar_usuario():
    # Datos registrados en el sistema
    nombre_usuario = "jfenoni"
    contrasena = "feno123"
    intentos = 0  # Inicializa el contador de intentos

    usuario_ingresado = input("Por favor, ingrese su usuario: ") #verifica el nombre de usuario
    while usuario_ingresado != nombre_usuario:
        print("Usuario no registrado")
        usuario_ingresado = input("Por favor, ingrese su usuario: ")

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
autenticar_usuario()