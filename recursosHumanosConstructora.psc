Algoritmo recursosHumanosConstructora
	// Definimos variables
	Definir nombreUsuario, contrasena, usuarioIngresado, contrasenaIngresada como cadena
	
	// Datos registrados en el sistema
	nombreUsuario= "jfenoni"
	contrasena= "feno123"
	intentos=0 // Inicializa el contador de intentos
	
	// Inicio de sesi�n con limite de 3 intentos
	Escribir "Bienvenido al sistema de gesti�n de RRHH de Constructora Enju Fenoni"
	Mientras (usuarioIngresado <> nombreUsuario)
		Escribir "Por favor, ingrese su usuario"
		Leer usuarioIngresado
		Si (usuarioIngresado <> nombreUsuario)
			Escribir "Usuario no registrado"
		FinSi
	FinMientras
	
	Si (usuarioIngresado == nombreUsuario)
		Mientras (contrasenaIngresada <> contrasena) y intentos < 3 hacer
			Escribir "Por favor, ingrese su contrase�a"
			Leer contrasenaIngresada
			Si (contrasenaIngresada <> contrasena)
				Escribir "contrase�a incorrecta"
			FinSi
			intentos = intentos + 1 // Incrementa el contador de intentos
			Si intentos>=3 Entonces
				Escribir "Usuario bloqueado, por favor comun�quese con el administrador del sistema"
			FinSi
		FinMientras
	FinSi
	
	
	// Verificaci�n de usuario y contrase�a
	Si usuarioIngresado == nombreUsuario Y contrasenaIngresada == contrasena Entonces
		Escribir "Bienvenido, ", nombreUsuario
		// Mostrar men�
		Escribir "Seleccione una opci�n:"
		Escribir "1. Empleados"
		Escribir "2. Departamentos, proyectos y tareas"
		Escribir "3. Clientes"
		Escribir "4. Salir"
		Repetir
			Leer opcion
			// Procesar opci�n de men�
			Segun opcion Hacer
				1:  Escribir "1. Ver informaci�n de empleados"
					Escribir "2. Actualizar informaci�n de empleados"
				2: 	Escribir "1. Ver departamentos y proyectos asociados"
					Escribir "2. Agregar o Modificar proyectos y tareas"
				3:  Escribir "1. Ver informaci�n de clientes"
					Escribir "2. Actualizar informaci�n de clientes"
				4:  Escribir "Gracias por usar nuestro sistema."
			FinSegun				
		Hasta que opcion = 4 // Repite el men� hasta que el usuario elija salir
	FinSi
	
FinAlgoritmo
