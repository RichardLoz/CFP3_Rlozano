-- SQL 
--DDL ==> Sirve para trabajar sobre los objetos(DB,Tablas,Vistas,SP)
	-- CREATE - ALTER - DROP - TRUNCATE
	-- DROP TABLE ALUMNOS ==> Eliminar toda la tabla Alumnos
	-- TRUNCATE ==> ELIMINAR LA TABLA y la vuelve a crear
--DML ==> Sirve para trabajar sobre los registros:
	-- INSERT : Insertar datos en una determinada tabla
	-- SELECT : Devuelve registros de una determinada tabla
	-- UPDATE : MODIFICAR DATOS DE UNA REGISTRO
	-- DELETE : ELIMINAR UN REGISTRO/S DE UNA TABLA

-- PK: PRIMARY KEY : Identificar de manera unica cada registro
-- FK: FOREIGN KEY : Relacionar las tablas

-- PRACTICA
CREATE TABLE if not EXISTS Profesores (
	id_profesor INTEGER PRIMARY key AUTOINCREMENT NOT NULL,
	NOMBRE TEXT,
	APELLIDO TEXT,
	edad INTEGER
	);
	
DROP TABLE Profesores;
	
-- INSERT
insert into Profesores (nombre, APELLIDO,edad) VALUES
('Pablo','Esparta',59),
('Florencia','Dominguez', 44),
('Sol','Porton',21),
('Norma','Cisne', 62),
('Nancy','Solanas', 66)

-- SELECT
Select nombre, APELLIDO FROM Profesores
select id_profesor, nombre, APELLIDO,edad from profesores
select * from Profesores

-- WHERE : APLICAR UNA CONDICION
-- SELECT COLUMNA1, COLUMNAN FROm NOMBRETABLA WHERE <CONDICION>
select * from Profesores where edad > 30
select * from profesores where edad != 36

-- UPDATE
select * from Profesores;
update Profesores set edad = 36 where id_profesor = 3;

-- DELETE
Delete from Profesores where id_profesor = 7;
Delete from Profesores where id_profesor = 8;
Delete from Profesores where id_profesor = 9;

-- IN: incluir uno o mas registros
delete from Profesores where id_profesor in (7)
select * from Profesores where id_profesor in (2,3,4)

-- DISTINCT : Ayuda a obtener datos unicos de ciertas columnas
select * from Profesores
-- SELECT DISTINCT COLUMNA1,COLUMNAN FROM NOMBRETABLA
select DISTINCT nombre, APELLIDO, edad from Profesores

-- ORDER BY: Ayuda a ordenar los registros de una tabla
-- SELECT COLUMNA1, COLUMNAN FROM NOMBRETABLA WHERE <CONDICION> ORDER BY
select * from Profesores where edad > 20 order by edad desc 

-- LIMIT: Nos ayuda a limitar la cantidad de registros que se quieren mostrar
select * from Profesores limit 3
select * from Profesores where edad < 40 order by edad desc limit 4
-- QUIERO SELECCIONAR LOS PROFESORES PERO NO REPETIR LOS REGISTROS CON LA MISMA EDAD
select DISTINCT nombre, apellido, edad from Profesores
select * from Profesores
select DISTINCT nombre from Profesores

-- 
-- SELECCIONAR LOS PROFESORES CUYA NOMBRE EMPIECE CON LA LETRA F
Select * from Profesores where nombre like 'F%'

-- COUNT: Nos sirve para contabilizar registros de una tabla
-- Select count(NOMBRECOLUMNA) FROM NOMBRETABLA
-- AS : Renombrar el nombre de una tabla de manera temporal
select count(id_profesor) as Total_Profesores from Profesores
select count(id_profesor) as 'Total Profesores' from Profesores

-- Quiero la cantidad de profesores pero con nombres unicos
select count(DISTINCT nombre) as 'Nombres unicos' from Profesores
select count(nombre) from Profesores
