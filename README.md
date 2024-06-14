
BuildHR Manager es un sistema que apunta a una gestión integral de recursos humanos diseñado para optimizar y simplificar los procesos de administración de personal en empresas constructoras. Este sistema ofrece una solución completa para la gestión eficiente del talento humano.

## Descripción del Proyecto

**Proyecto Integrador - Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial - Cohorte 2024**

Como parte del "Proyecto Integrador" para la Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Cohorte 2024, nos propusimos a desarrollar una base de datos que apunta principalmente a la gestión de tareas de los empleados de una constructora. Para esto creamos el CRUD (Create, Read, Update, Delate o en español Crear, Leer, Actualizar y Borrar) de las 5 tablas que la componen para así poder interactuar con las mismas que a partir de los archivos que se muestran en este documento, cumpla con las funcionalidades planteadas a continuacion

### Asignaturas y sus respectivos contenidos

- Base de Datos I
     - [Ver Diagrama Entidad - Relación »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/BD/diagramas/Diagrama_ER.jpg "Ver Diagrama Entidad - Relación »")
     - [Ver Diagrama Crow's Foot »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/BD/diagramas/Diagrama_CF.jpg.png "Ver Diagrama Crow's Foot »")
     - [Ver Creación de Base de Datos o Schema »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/BD/database_scheme_creation.sql "Ver Creación Base de Datos »")
     - [Ver Inserción de Datos »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/BD/database_insertion_data.sql "Ver Inserción de Datos »")
     - [Ver Consultas en Base de Datos »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/BD/database_insertion_data.sql "Ver Inserción de Datos »")


- Ética y Deontología Profesional
     -  [Ver Wiki »](https://github.com/NoeliaSoto/Integrador-IPyBDI/wiki/%C3%89tica-y-Deontolog%C3%ADa-Profesional "Ver Wiki »")

       
- Introducción a la Programación
     - [Ver pseudocódigo »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/recursosHumanosConstructora.psc "Ver pseudocódigo »")
     - [Ver CRUD tabla Empleados »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/Python/crud_empleados.py "Ver CRUD tabla Empleados »")
     - [Ver CRUD tabla Proyectos »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/Python/crud_proyecto.py "Ver CRUD tabla Proyectos »")
     - [Ver CRUD tabla Clientes »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/Python/crud_clientes.py "Ver CRUD tabla Clientes »")
     - [Ver CRUD tabla Departamentos »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/Python/crud_departamentos.py "Ver CRUD tabla Departamentos »")
     - [Ver CRUD tabla Tareas »](https://github.com/NoeliaSoto/Integrador-IPyBDI/blob/main/Python/crud_tareas.py "Ver CrRUD tabla Tareas »")


### Autores

| Nombre             | Usuario de GitHub                                | DNI        | Email                       |
|--------------------|--------------------------------------------------|------------|-----------------------------|
| Angellotti Enzo    | [Enzoriukz](https://github.com/Enzoriukz "Enzoriukz")        | 32107971   | enzomakz@gmail.com          |
| Menón Nicolas      | [Nico0626](https://github.com/Nico0626 "Nico0626")           | 46129760   | nico.menon.2@gmail.com      |
| Moyano Juan Cruz   | [jcmoyano](https://github.com/jcmoyano "jcmoyano")           | 41002250   | juancruz.moyanocar@gmail.com|
| Leyria Federico    | [Federicoleyria](https://github.com/Federicoleyria "Federicoleyria") | 43523682   | fedeleyria2016@gmail.com    |
| Soto Noelia        | [NoeliaSoto](https://github.com/NoeliaSoto "NoeliaSoto")     | 41253579   | noeli4.soto@gmail.com       |

## Modularizacion del codigo

## Modularizacion del codigo

### main.py
Este archivo es nuestro archivo principal ya que tendra todos las funciones tanto en el mismo archivo, como la bienvenida y la autentificacion como archivos importados como los archivos .py donde realizaremos el CRUD.

### Conexion_database
Este archivo contendra la conexion a la base de datos myysql, deberemos importar las correspondiente librerias y realizar la conexion exitosa. a este archivo se le debera imporatr a los demas archivos del crud.

### CRUD_tabla
Estos archivos contienen los CRUD de las tablas que nos permiten interactuar con la que se haya elegido, por ejemplo CRUD_clientes


## Funcionalidades Clave del sistema:

### Gestión de Empleados

- Registro detallado de información personal y laboral de los empleados.
- Actualización y seguimiento de datos, incluyendo información de contacto, historial laboral y formación académica.
- Asignación de roles y responsabilidades, y seguimiento del desempeño.

### Gestión de Departamentos y Proyectos

- Creación y asignación de departamentos y equipos de trabajo.
- Seguimiento detallado de proyectos.
- Asignación de recursos humanos según las necesidades específicas de cada proyecto.
- Gestión de clientes según proyecto al que pertenecen

### Gestión de Tareas
- Asignación de tareas según proyectos y clientes
- Visualización y seguimiento de las tareas de los empleados según el proyecto asignado
- Previsión de plazos para cumplir las tareas


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

## Archivos esenciales y uso de la aplicación

Este repositorio contiene varios archivos esenciales para el funcionamiento de BuildHR Manager, estos son:

1. **main.py**: Archivo principal que gestiona la interfaz de usuario, incluyendo la bienvenida, autenticación y el menú principal.
2. **conexion_database.py**: Maneja la conexión a la base de datos MySQL, necesaria para que otros archivos interactúen con la base de datos.
3. **crud_empleados.py**: Permite crear, leer, actualizar y borrar registros de empleados.
4. **crud_proyecto.py**: CRUD para la gestión de proyectos.
5. **crud_clientes.py**: CRUD para la gestión de clientes.
6. **crud_departamentos.py**: CRUD para la gestión de departamentos.
7. **crud_tareas.py**: CRUD para la gestión de tareas.

Para usar la aplicación, se deben instalar Visual Studio Code, MySQL y MySQL Workbench. Luego, se clona el repositorio y se ejecutan los scripts SQL proporcionados para crear y poblar la base de datos. Finalmente, se ejecuta el archivo `main.py` desde Visual Studio Code. El sistema pedirá un nombre de usuario y contraseña para acceder, y mostrará un menú principal para gestionar empleados, proyectos, clientes, departamentos y tareas, permitiendo a cualquier usuario interactuar con la aplicación sin necesidad de conocimientos previos en programación.



