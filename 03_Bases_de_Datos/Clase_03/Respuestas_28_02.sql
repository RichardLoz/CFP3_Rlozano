--1- Seleccionar todos los campos de la tabla Alumnos
Select * from Alumnos; -- OK
--2- Actualizar la direccion de "Juan Perez" nacido en 1995-05-10 a "Calle Uruguay 200"
select * from Alumnos where nombre = 'Juan' and apellido = 'Perez' 
and fecha_nac like '%1995-05-10%'
update Alumnos set direccion = 'Calle Uruguay 200' where ID_Alumno = 1
--3- Borrar el registro de "Maria Gonzalez"
select * from Alumnos where nombre = 'Maria' and apellido = 'Gonzalez'
delete from Alumnos where ID_Alumno = 2
--4- Seleccionar todos los alumnos nacidos en 1995
select * from Alumnos where fecha_nac like '%1995%'
select * from Alumnos where fecha_nac BETWEEN '1995-01-01' and '1995-12-31'
--5- Seleccionar los alumnos cuyo nombre empiece con "A"
select * from Alumnos where nombre like 'A%'
--6- Seleccionar los alumnos cuya direccion contenga "calle"
select * from Alumnos where direccion like '%calle%'
--7- Seleccionar los alumnos cuyo nombre este en la lista ("Juan", "Maria","Pedro")
select * from Alumnos where nombre in ('Juan','Maria','Pedro')
--8- Seleccionar los alumnos cuya fecha de nacimiento este entre '1990-01-01' y 
--'1995-01-01' y ordenarlos por fecha de nacimiento de forma descendente.
select * from Alumnos where fecha_nac BETWEEN '1990-01-01' and '1995-01-01' 
order by fecha_nac desc