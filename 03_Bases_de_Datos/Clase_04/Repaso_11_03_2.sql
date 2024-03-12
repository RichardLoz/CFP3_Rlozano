-- Ejercicio:
-- Construya una tabla en la cual se tengan las siguientes columnas:
--ID del cliente PRIMARY KEY
--Nombre del cliente
--Apellido del cliente
--Email
--Fecha de nacimiento
-- La empresa le solicita la cantidad de clientes que han otorgado su email, tambien le son solicitadas las 
-- fechas de nacimiento de todos los clientes, esto para poder regalarles en su cumple años una tarjeta 
--promoción.
-- Para finalizar obtenga la cantidad de tarjetas promoción que deben ser fabricadas
select * from Premios
--1
select count(email) as 'Personas con email' from premios
--2
select fecha_nac, nombre_cliente from Premios
--3
select count(fecha_nac) as 'Tarjetas a realizar' from premios
