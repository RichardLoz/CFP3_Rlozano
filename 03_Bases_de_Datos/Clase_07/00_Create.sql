-- Sobre Concesionaria de autos
-- Vendedores (ID_vendedor, nombre, apellido, edad, direccion,id_sucursal)
-- Clientes (ID_cliente, nombre, apellido,edad,direccion,telefono,correo)
-- Automoviles (Id_auto, marca, modelo, año, color, tipo_combustible, id_sucursal,
-- tipo_caja, transmision)
-- Sucursales (ID_sucursal, nombre, direccion,telefono)

Create table if not EXISTS Sucursales (
id_sucursal INTEGER PRIMARY key AUTOINCREMENT not null,
nombre text not null,
direccion text not null,
telefono text not NULL
);

Create table if not EXISTS vendedores (
id_vendedor INTEGER PRIMARY key AUTOINCREMENT not null,
nombre text not null,
apellido text not null,
edad INTEGER not null,
direccion text not null,
id_sucursal integer,
	FOREIGN key (id_sucursal) REFERENCES Sucursales (id_sucursal)
);

create table if not EXISTS Clientes (
id_cliente INTEGER PRIMARY key AUTOINCREMENT not null,
nombre text not null,
apellido text not null,
edad INTEGER not null,
direccion text not null,
telefono text not null,
correo text not NULL
);

create table if not EXISTS Automoviles (
id_auto INTEGER PRIMARY key AUTOINCREMENT not null,
marca text not null,
modelo text not null,
anio datetime not null,
color text not null,
tipo_combustible not null,
transmision text not NULL,
id_sucursal INTEGER,
	FOREIGN key (id_sucursal) REFERENCES Sucursales (id_sucursal)
);



