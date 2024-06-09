# BuildHR Manager

BuildHR Manager es un sistema integral de gestión de recursos humanos diseñado para optimizar y simplificar los procesos de administración de personal en empresas constructoras. Este sistema ofrece una solución completa para la gestión eficiente del talento humano.

## Descripción del Proyecto

**Proyecto Integrador - Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial - Cohorte 2024**

BuildHR Manager es desarrollado como parte del Proyecto Integrador para la Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Cohorte 2024.

### Asignaturas

- Base de Datos I [VER diagramas]((https://github.com/NoeliaSoto/Integrador-IPyBDI/tree/main/diagrama_ER))
- Ética y Deontología Profesional [VER wiki]((https://github.com/NoeliaSoto/Integrador-IPyBDI/wiki))
- Introducción a la Programación [VER código/pseudocódigo]([#](https://github.com/NoeliaSoto/Integrador-IPyBDI/tree/main/PPython))


### Autores

| Nombre             | Usuario de GitHub                                | DNI        | Email                       |
|--------------------|--------------------------------------------------|------------|-----------------------------|
| Angellotti Enzo    | [Enzoriukz](https://github.com/Enzoriukz "Enzoriukz")        | 32107971   | enzomakz@gmail.com          |
| Menón Nicolas      | [Nico0626](https://github.com/Nico0626 "Nico0626")           | 46129760   | nico.menon.2@gmail.com      |
| Moyano Juan Cruz   | [jcmoyano](https://github.com/jcmoyano "jcmoyano")           | 41002250   | juancruz.moyanocar@gmail.com|
| Leyria Federico    | [Federicoleyria](https://github.com/Federicoleyria "Federicoleyria") | 43523682   | fedeleyria2016@gmail.com    |
| Soto Noelia        | [NoeliaSoto](https://github.com/NoeliaSoto "NoeliaSoto")     | 41253579   | noeli4.soto@gmail.com       |

## Modularizacion del codigo

### main.py
Este archivo será nuestro archivo principal ya que tendra todos las funciones tanto en el mismo archivo, como la bienvenida y la autentificacion como archivos importados como los archivos .py donde realizaremos el crud.

### Conexion_database
Este archivo contendra la conexion a la base de datos myysql, deberemos importar las correspondiente librerias y realizar la conexion exitosa. a este archivo se le debera imporatr a los demas archivos del crud.

### Crear_tareas
Este archivo se realizara la accion del crud de crear nuevas tareas.

### Ver_tareas
Este archivo se realizara la accion del crud de ver las tareas realizadas en conjunto con la demas información en el campo con fecha de inicio y fecha de finalizacion, se identificara  através del Id de tareas.

### Modificar_tareas
Este archivo se realizara la accion del crud de modificar cualquier columna del campo tareas con el id de tareas.

### Eliminar_tareas
Este archivo se realizara la accion del crud de eliminar tareas y todas las tablas relacionada con ella, se identificara al igual que el ver tareas y modificar tareas, através del Id de tareas.

## Funcionalidades Clave

Algunas funcionalidades claves que ofrece BuildHR Manager son:

### Gestión de Empleados

- Registro detallado de información personal y laboral de los empleados.
- Actualización y seguimiento de datos, incluyendo información de contacto, historial laboral y formación académica.
- Asignación de roles y responsabilidades, y seguimiento del desempeño.

### Gestión de Departamentos y Proyectos

- Creación y asignación de departamentos y equipos de trabajo.
- Seguimiento detallado de proyectos y tareas asignadas a cada departamento o equipo.
- Asignación de recursos humanos según las necesidades específicas de cada proyecto.

### Gestión de Capacitación y Desarrollo

- Registro de actividades de capacitación, cursos realizados y certificaciones obtenidas.

### Gestión de Ausencias y Vacaciones

- Registro y seguimiento de ausencias, licencias y vacaciones de los empleados.
- Programación de vacaciones y gestión de calendarios de ausencias.

### Análisis y Reportes

- Generación de informes personalizados sobre datos de recursos humanos.
- Visualización de datos en tiempo real para facilitar la toma de decisiones estratégicas y la planificación.

## Análisis EPS

Este análisis detalla cómo las diferentes entradas (nombre de usuario, contraseña, opción del menú) se procesan en el sistema y qué salidas se generan en función de esas entradas y procesos.

### Entradas

1. **Usuario**: El nombre de usuario que el usuario ingresa para iniciar sesión en el sistema.
2. **Contraseña**: La contraseña correspondiente al nombre de usuario ingresado.
3. **Opción del Menú**: La opción seleccionada por el usuario en el menú principal después de iniciar sesión.

### Procesos

**Inicio de Sesión**:

1. El sistema solicita al usuario que ingrese su nombre de usuario.
2. El usuario ingresa su nombre de usuario.
3. El sistema solicita al usuario que ingrese su contraseña.
4. El usuario ingresa su contraseña.
5. El sistema verifica las credenciales ingresadas.
   - Si las credenciales son válidas, el usuario inicia sesión y se muestra el menú principal.
   - Si las credenciales son inválidas, el sistema muestra un mensaje de error y permite al usuario intentar nuevamente iniciar sesión.

**Menú Principal**:

1. El sistema muestra las opciones del menú disponibles.
2. El usuario selecciona una opción del menú.
3. El sistema procesa la opción seleccionada y ejecuta la funcionalidad correspondiente.
4. Después de completar la acción seleccionada, el sistema vuelve a mostrar el menú principal para que el usuario pueda seleccionar otra opción o salir del sistema.

### Salidas

1. **Inicio de Sesión Exitoso**:
   - Mensaje de bienvenida que incluye el nombre de usuario.
   - Menú principal con opciones para gestionar empleados, departamentos, proyectos, capacitación, ausencias, generar reportes o salir del sistema.

2. **Inicio de Sesión Fallido**:
   - Mensaje de error indicando que las credenciales son incorrectas.
   - Opción para volver a intentar iniciar sesión.

3. **Selección de Opción del Menú**:
   - Ejecución de la funcionalidad correspondiente según la opción seleccionada.
   - Mensajes de confirmación o resultados de la acción realizada.
   - Regreso al menú principal para seleccionar otra opción o salir del sistema.




