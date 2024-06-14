USE mydb;

-- Mostrar la tabla departamento
SELECT * FROM departamento;

-- Mostrar solo las columnas id_cliente y nombre de la tabla cliente
SELECT id_cliente, nombre FROM cliente;

-- Muestra la tabla empleados pero limitandola a 5 resultados
SELECT * FROM empleados LIMIT 5;

-- Mostrar los proyectos que estan en progreso
SELECT * FROM proyecto 
WHERE estado = 'En progreso';

-- Mostrar los proyectos que tengan fecha de inicio desde 2023-01-01 al 2023-12-31
SELECT * FROM proyecto 
WHERE fecha_inicio 
BETWEEN '2023-01-01' AND '2023-12-31';



-- Mostrar el nombre completo de los empleados y el departamento donde pertenecen
SELECT e.nombre_completo, d.nombre_departamento 
FROM empleados e
INNER JOIN departamento d ON e.DEPARTAMENTO_id_departamento = d.id_departamento;

-- Mostrar el nombre de los empleados y su departamento que tengan proyectos en progreso
SELECT e.nombre_completo, d.nombre_departamento, p.nombre_proyecto
FROM empleados e
INNER JOIN departamento d ON e.DEPARTAMENTO_id_departamento = d.id_departamento
INNER JOIN proyecto p ON d.PROYECTO_id_proyecto = p.id_proyecto
WHERE p.estado = 'En progreso';
