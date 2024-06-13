USE mydb;
DELETE FROM cliente WHERE id_cliente = 1;

-- Insertar datos en la tabla cliente
INSERT INTO cliente (id_cliente, nombre) VALUES
(1, 'Anahí Hernandez'),
(2, 'Julián Conde'),
(3, 'Emily Davis'),
(4, 'Sebastian Duarde');

-- Insertar datos en la tabla proyecto
INSERT INTO proyecto (id_proyecto, nombre_proyecto, estado, fecha_inicio, fecha_finalizacion, CLIENTE_id_cliente) VALUES
(1, 'Estelar Estates', 'En progreso', '2023-02-01', '2024-06-14', 1),
(2, 'Terra Nova', 'Completado', '2017-02-15', '2018-07-30', 2),
(3, 'Serenity Springs', 'Planeado', '2024-03-01', NULL, 3),
(4, 'SuperGourmet', 'Completado', '2016-11-13', '2017-05-13', 4);

-- Tuvimos que alterar la tabla departamente para ingresar una descripcion_departamento mas larga.
ALTER TABLE departamento MODIFY COLUMN descripcion_departamento VARCHAR(255) NOT NULL;
-- Insertar datos en la tabla departamento
INSERT INTO departamento (id_departamento, nombre_departamento, descripcion_departamento, PROYECTO_id_proyecto) VALUES
(1, 'Departamento de Ingeniería y Diseño', ' Ingeniería del proyecto, diseño estructural, planos, especificaciones técnicas y cálculos de ingeniería necesarios para llevar a cabo los proyectos de construcción.', 1),
(2, 'Departamento de Proyectos', 'Planificación, coordinación y ejecución de los proyectos de construcción', 3),
(3, 'Departamento HHRR', 'Recursos Humanos', 3),
(4, 'Departamento Marketing', 'Publicidad y Marketing', 3),
(5, 'Departamento Finanzas', 'Gestión financiera, contabilidad, presupuestos, análisis financiero.',2);




-- Insertar datos en la tabla empleados
INSERT INTO empleados (dni, fecha_nacimiento, genero, nombre_completo, numero_telefono, fecha_contratado, direccion, puesto, DEPARTAMENTO_id_departamento) VALUES
(33123456, '1985-05-20', 'M', 'Juan Perez', '3541-484627', '2015-01-10', 'Calle Falsa 123', 'Ingeniero Civil', 1),
(36789123, '1990-11-10', 'F', 'Ana Gomez', '3548-356285', '2016-04-15', 'Avenida Siempre Viva 456', 'Gerente de Recursos Humanos', 3),
(37456789, '1991-07-25', 'M', 'Carlos Martinez', '3541-372846', '2016-09-23', 'Calle Real 789', 'Especialista en Marketing', 4),
(36456789, '1999-04-05', 'F', 'Martina Busto', '3541-372846', '2015-06-23', 'Calle Fraga 776', 'Contador', 5),
(33827464, '1986-03-14', 'M', 'Alex Morassut', '3541-348269', '2015-05-16', 'Avenida Colon 34', 'Gerente de Planificación de Proyectos', 2);

-- modificamos la tabla tareas para agregar nulos simulando los datos de finalizaciond de proyecto que cuando se terminen cambiaremos los datos nulos
ALTER TABLE tareas MODIFY COLUMN fecha_finalizacion DATE NULL;


INSERT INTO tareas (id_tareas, tarea, fecha_inicio, fecha_finalizacion, PROYECTO_id_proyecto) VALUES
(1, 'Control de calidad', '2024-03-20', '2024-06-30', 1),
(2, 'Selección de Personal', '2022-02-15', '2022-05-31', 2),
(3, 'Campaña de Publicidad', '2024-03-01', '2024-06-30', 1),
(4, 'Planificacion del proyecto', '2024-03-01', NULL, 3),
(5, 'Financiamiento y estructura de capital', '2024-03-01', NULL, 3);
