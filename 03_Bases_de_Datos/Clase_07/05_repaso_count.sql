-- PRACTICA
-- 1. Cuantos vendedores hay en total en todas las sucursales?
select count(*) as Total_vendedores from vendedores
-- 2. Cuantos clientes estan registrados en nuestra DB?
select count(*) as Total_Clientes from Clientes
-- 3. Cuantos automoviles hay en total?
select count(*) as Total_Automoviles from Automoviles
-- 4. Cuantos vendedores en total tienen menos de 30 años?
select count(*) as Vendedor_Menor_30 from vendedores v 
	where v.edad < 30
-- 5. Cuantos clientes tienen entre 20 y 35 años?
select count(*) as Clientes from clientes c
where c.edad BETWEEN 20 and 35
-- 6. Cuantos automoviles hay en la sucursal 1?
select count(*) as Cantidad_Auto from Automoviles au
where au.id_sucursal = 1
-- 7. Cuantas sucursales tienen mas de 10 autos?
-- 8. Cuantos automoviles tienen transmision automatica?
select count(*) as Cantidad_transmision from Automoviles au
	where au.transmision like '%auto%'
-- 9. Cuantos clientes tienen entre 25 y 45 años inclusive?
select count(*) as Clientes_edades from Clientes c
	where c.edad BETWEEN 25 and 45
-- 10. Cuantos automoviles hay de color rojo en toda la DB
select count(*) as Autos_Rojo from Automoviles au
	where au.color like '%red%'