-- 					TEORIA
-- 1. GROUP BY: Se utiliza en SQL para agrupar filas que tienen el
-- mismo valor en una o mas columnas. Esto permite realizar operaciones
-- de agregacion como sumar, contar o calcular promedio, en cada grupo
-- de filas.
-- SINTAXIS:
	-- Select columna1, columna2, funcion_agregacion(columna)
	-- 	FROM TABLA
	-- GROUP BY columna1, columna2

-- Obtener el numero de ventas realizadas por cada vendedor
Select id_vendedor, count(*) as Cantidad_Ventas
from Ventas
group by id_vendedor;


-- 2. HAVING: La clausula HAVING se utiliza junto con GROUP BY para
-- filtrar grupos de filas basandose en una condicion. Es similar a
-- la clausula WHERE, pero se aplica después de agrupar filas

-- SINTAXIS.
	-- Select columna1, columna2, funcion_agregacion(columna)
	-- 	FROM TABLA
	-- GROUP BY columna1, columna2
	-- HAVING <CONDICION>

-- Obtener el numero de ventas realizadas por cada vendedor que haya
-- realizado mas de 5 ventas
select id_vendedor, count(*) as Cantidad_Ventas
from Ventas v
group by id_vendedor
HAVING Cantidad_Ventas > 5;

-- ================================================0
-- 3. JOIN: La clausula JOIN se utiliza para combinar filas de dos 
-- o mas tablas basandose en una condicion relacionada entre ellas.

-- SINTAXIS:
--		Select Columna1, Columna2, ColumnaN
--		from Table1
--		JOIN Tabla2
--		ON condiciones_union

-- Obtener el nombre del vendedor y el nombre del cliente para cada
-- venta.
Select VD.id_vendedor, VD.nombre as Vendedor, cl.nombre as Cliente
from Ventas v
JOIN vendedores VD
on v.id_vendedor = VD.id_vendedor
JOIN Clientes cl
order by 1

-- =====================================================0
-- 4. SUBCONSULTAS: Una subconsulta es una consulta anidada dentro
-- de otra consulta SQL, se puede utilizar en varias clausulas como
-- SELECT, FROM, WHERE, HAVING o JOIN.

-- SINTAXIS:
--		SELECT Columnas
--		FROM Tabla
--		WHERE Columna in (Select FROM otra_tabla WHERE <condicion>)

-- Obtener el ID del vendedor que ha realizado la venta con el 
-- precio mas alto.
select id_vendedor
from Ventas
where precio in (select max(precio) from ventas)

select id_vendedor
from Ventas
order by precio DESC
limit 1

-- 2. Obtener el nombre de la sucursal donde se realizo la venta con
-- el precio mas bajo.
select id_sucursal
from Ventas
where precio = (select min(precio) from ventas)

select id_sucursal,nombre
from Sucursales
where id_sucursal in (
	select id_sucursal
	from Ventas
	where precio = (select min(precio) from ventas)
	);
-- 3. Obtener el ID del auto mas caro vendido en cada Sucursal
select id_sucursal, max(id_auto)
from Ventas
group by id_sucursal
-- 4. Obtener el ID del cliente que ha realizado la compra mas reciente
select id_cliente
from Ventas
where fecha_compra in (select max(fecha_compra) from ventas)
-- 5. Obtener el nombre del cliente que realizo la compra mas cara.
select nombre
from Clientes
where id_cliente in(
	select id_cliente
	from Ventas
	where precio in (select max(precio) from ventas)
	);
	
	
-- Obtener el nombre del cliente y la fecha de compra para cada
-- venta realiazada, incluyendo la marca y modelo del auto vendido.
Select C.nombre as Nombre_Cliente, V.fecha_compra, A.marca, A.modelo
FROM Ventas V
JOIN clientes C ON V.id_cliente = C.id_cliente
JOIN Automoviles A ON V.id_auto = A.id_auto
							1


