-- CLAUSULAS (AS, SUM, MIN, MAX, AVG)
-- 1. Cual es la edad maxima de los vendedores de las sucursales
select max(edad) as Edad_Maxima from vendedores

-- 2. Cual es el año del auto mas antiguo?
select min(anio) as Auto_viejo from Automoviles

-- 3. Cual es la suma total de las edades de todos los clientes
select sum(edad) as Edad_total from clientes

-- 4. Cual es el promedio de edad de los vendedores
select avg(edad) as Edad_Promedio from vendedores

-- Cual es el año mas reciente de los Automoviles
select max(anio) as Modelo_actual from Automoviles

-- PRACTICAR
-- Cual es el auto mas antiguo de la sucursal 3
select min(anio) as Auto_Antiguo from Automoviles 
	where id_sucursal = 3
-- Cual es el promedio de años de los automoviles de la sucursal 4
select avg(anio) as Promedio_Auto from Automoviles 
	where id_sucursal = 4
-- Cual es el auto mas antiguo de la marca Ford
select min(anio) as auto_antiguo from Automoviles 
	where marca like '%ford%' 
-- Cual es el promedio de edad de los vendedores de la sucursal 3
select avg(edad) as Edad_Promedio from vendedores
	where id_sucursal = 3
-- Cual es el año mas reciente de los automoviles de color verde
select max(anio) as Auto_actual from Automoviles
	where color = 'Green'

-- Cual es el modelo del automovil mas antiguo de las sucursales
select modelo as Modelo_antiguo
from Automoviles
where anio = (select min(anio) from Automoviles)

-- Cual es el nombre del empleado mas joven de las Sucursales
select nombre as Vendedor_Joven
from vendedores
where edad = (Select min(edad) from vendedores) limit 1