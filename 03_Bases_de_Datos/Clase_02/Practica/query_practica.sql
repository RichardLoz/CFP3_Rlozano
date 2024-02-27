-- PRACTICA SQL
-- Teniendo en cuenta la tabla Productos, realiar las siguientes consultas:
--1. Recuperar el id_producto, nombre y precio de la tabla Productos
select id_producto, nombre, precio from Productos
--2. Recuperar los registros con los id_producto 44,45,46 y 49
select * from Productos where id_producto in (44,45,46,49)
--3. Recuperar los registros con precio mayor a 4000
select * from Productos where precio > 4000
--4. Recuperar el id_producto y precio de los productos con valor entre
-- 1000 y 5000.
select id_producto, precio from Productos 
where precio BETWEEN 1000 and 5000
--5. Eliminar los registro con los id_producto 50,51,52,53,54,55
delete from Productos where id_producto in (50,51,52,53,54,55)
delete from Productos where id_producto BETWEEN 50 and 55
--6. Recuperar los registros que empiecen con la letra "C".
select * from Productos where nombre like '%20%'

update Productos set nombre = 'Lampara de 20 mtrs' where id_producto = 46

select * from Productos where nombre like '%Alicate%'
