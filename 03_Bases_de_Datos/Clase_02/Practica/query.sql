-- DDL
-- CREATE
-- CREATE TABLE if not EXISTS Alumnos (
-- 	id_alumno INTEGER,
-- 	nombre text(20),
-- 	edad INTEGER
-- 	);
-- 
-- DROP (Elimino un objeto)
-- drop TABLE alumnos;	
-- 
-- ALTER  (EDITAR COLUMNAS DE UNA TABLA)
-- alter table Alumnos add COLUMN direccion text
-- 
-- ALTER - DROP
-- alter table Alumnos DROP COLUMN edad
-- 
-- ALTER - RENAME
-- alter table Alumnos RENAME COLUMN direccion to direcc

-- CREAMOS LA TABLA PRODUCTOS
-- create table Productos (
-- 	id_producto integer PRIMARY KEY AUTOINCREMENT,
-- 	nombre text(30) NOT NULL,
-- 	precio INTEGER not null,
-- 	peso real not null,
-- 	fecha_alta datetime not null,
-- 	fecha_baja datetime
-- 	);

	
INSERT INTO Productos (nombre, precio, peso, fecha_alta, fecha_baja) VALUES
  ('Tornillos M6x10 (100 unidades)', 500, 0.5, '2024-02-22', NULL),
  ('Martillo de carpintero', 1200, 1.0, '2024-02-21', NULL),
  ('Cinta métrica 5 metros', 350, 0.2, '2024-02-20', NULL),
  ('Nivel láser autonivelante', 4500, 1.5, '2024-02-19', NULL),
  ('Escalera telescópica 4x4', 8000, 20.0, '2024-02-18', NULL),
  ('Caja de herramientas 20 compartimentos', 2500, 2.5, '2024-02-17', NULL),
  ('Llave inglesa ajustable', 800, 0.8, '2024-02-16', NULL),
  ('Destornillador Phillips PH2', 300, 0.1, '2024-02-15', NULL),
  ('Alicate de corte diagonal', 500, 0.3, '2024-02-14', NULL),
  ('Gafas de seguridad transparentes', 200, 0.1, '2024-02-13', NULL),
  ('Guantes de trabajo talla L', 400, 0.2, '2024-02-12', NULL),
  ('Casco de seguridad con visera', 1500, 0.8, '2024-02-11', NULL),
  ('Mascarilla antipolvo FFP2', 100, 0.1, '2024-02-10', NULL),
  ('Cinta adhesiva de embalaje 50m', 400, 0.5, '2024-02-09', NULL),
  ('Film plástico transparente 5m x 2m', 600, 1.0, '2024-02-08', NULL),
  ('Bolsas de basura negras 100 unidades', 300, 0.5, '2024-02-07', NULL),
  ('Palet de madera europeo 80x120cm', 1200, 20.0, '2024-02-06', NULL),
  ('carretilla de mano plegable', 2500, 5.0, '2024-02-05', NULL),
  ('Transpaleta manual 2500kg', 4000, 50.0, '2024-02-04', NULL);
	
	
delete from Productos WHERE id_producto = 28


-- UPDATE
update Productos set precio = 1500 where id_producto = 40

-- SELECT (Seleccionar - recuperar una lista de campos)
SELECT columna1, columna2 FROM nombre_Tabla WHERE Criterio de seleccion

Select * FROM Productos
Select  nombre, precio FROM Productos

Select * from Productos where precio < 1000
-- Consulta para traer precios distintos de 5000
select nombre,precio, peso from Productos where precio != 5000

-- Consulta para actualizar el precio a 5000 del id_producto 41

-- IN
update Productos set precio = 5000 where id_producto = 41
update Productos set precio = 5000 where id_producto = 43
update Productos set precio = 5000 where id_producto = 47

update Productos set precio = 5000 where id_producto in (41,43,47)
delete from Productos where id_producto in (42,44,46)
select * from Productos where id_producto in (41,43,47)
select * from Productos

-- EJERCICIOS
-- 1- Mostrar los productos con precio mayor a 1000 y peso mayor a 1
select * from Productos where precio > 1000 and peso > 1
-- 2- Mostrar los productos con precio distinto a 1000
Select * from Productos where precio != 1000
-- 3- Mostrar id_producto, nombre y precio de los productos con el precio mayor a 3000
select id_producto, nombre, precio from Productos where precio > 3000
-- 4- Mostrar los productos con precio entre 1000 y 5000
select * from Productos where precio BETWEEN 1000 and 5000
select * from Productos where precio >= 1000 and precio <= 5000

-- like
Select * from productos where precio like '3%'
update Productos set nombre = 'M' where id_producto = 40

