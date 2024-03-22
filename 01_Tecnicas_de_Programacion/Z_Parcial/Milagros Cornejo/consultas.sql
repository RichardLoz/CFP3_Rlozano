-- 1.Seleccionar los empleados cuyo nombre empiece con la letra "S" y ordenarlos por ID de forma descendente
-- 2.Seleccionar todos los reclamos y ordenarlos por hora de forma descendente
-- 3. Contabilizar la cantidad de reclamos del cliente 10
-- 4. Actualizar el nombre del departamento "Servicio_cliente" por "Servicio al cliente"
-- 5. Seleccionar todos los  clientes cuyo correo termine en ".com" y ordenarlos por ID_Cliente


--1-
select * from Empleado where nombre like 'S%' ORDER by ID_Empleado DESC

--2-
select * from Reclamo  ORDER by hora  DESC

--3--
select count (id_Reclamo) as 'total reclamos' from Reclamo

--4--

update departamento  set nombre = 'servicio al cliente'  where ID_Departamento = 3


--5--
select * from cliente where correo_electronico like '%.com' order by  ID_Cliente
