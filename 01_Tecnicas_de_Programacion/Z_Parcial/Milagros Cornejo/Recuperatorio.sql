--seleccinar todos los reclamos realizados en el 2013 y ordenarlos por hora
SELECT * FROM Reclamo where 2013 ORDER by hora

--seleccionar los 4 primeros empleados del departamento 3 y ordenarlos por nombre de forma descendente.
SELECT * from Empleado  WHERE ID_Departamento=3  ORDER by Nombre LIMIT 4
--seleccionar los 3 primeros clientes cuyo correo termine en ".com" y ordenarlos por apellido de forma descenddente
SELECT * from Cliente WHERE Email like '%.com' ORDER  by Apellido DESC limit 3 
--Actualizar el estado de los reclamos a "ARCHIVADO" DE LOS RECLAMOS ENTRE EL 01/01/2023 Y 01/07/2023
UPDATE Reclamo set Estado_del_Reclamo = 'Archivado' where Fecha BETWEEN '1/1/2023' and  '7/1/2023'
select * from  Reclamo  where Fecha BETWEEN '1/1/2023' and  '7/1/2023'  order by 2

--Contabilizar la cantiddad de reclamos con estado en " proceso"
SELECT count (ID_Reclamo) as ' Total_Proceso' from Reclamo where Estado_del_Reclamo='En evaluación'
SELECT * from Reclamo where Estado_del_Reclamo='Proceso'




