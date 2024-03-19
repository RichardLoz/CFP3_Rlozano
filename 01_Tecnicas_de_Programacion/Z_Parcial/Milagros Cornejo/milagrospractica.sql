create table if not EXISTS Ventas(
    ID_Ventas integer PRIMARY KEY AUTOINCREMENT,
	ID_Clientes integer ,
	ID_Productos integer ,
	ID_Meto_Pagos integer ,
	ID_Envios integer  ,
	FOREIGN KEY (ID_Clientes) REFERENCES Clientes (ID_Clientes),
	FOREIGN KEY (ID_Productos) REFERENCES Productos (ID_Productos),
	FOREIGN KEY (ID_Meto_Pagos ) REFERENCES Met_Pagos (ID_Meto_Pagos),
	FOREIGN KEY (ID_Envios) REFERENCES Envios (ID_Envios)
	)
	
	
create table if not EXISTS clientes (
  ID_Clientes integer PRIMARY KEY AUTOINCREMENT,
  nombre text, 
  apelidos text,
  documento text ,
  telefono text, 
  direccion text ,
  Email TEXT 
  )
  
  
  CREATE table if not EXISTS  Productos (
  ID_Productos integer PRIMARY KEY AUTOINCREMENT ,
  ID_Cat_Productos iNTEGER  ,
  ID_Proveedores INTEGER ,
  peso text ,
  stock REAL ,
  FOREIGN KEY (ID_Cat_Productos) REFERENCES  Cat_Productos (ID_Cat_Productos),
  FOREIGN Key (ID_Proveedores ) REFERENCES Provedores (ID_Provedores)
  );
  
CREATE TABLE Cat_Productos (
ID_Cat_Productos INTEGER PRIMARY KEY AUTOINCREMENT ,
nombre text ,
F_Alta datetime ,
ID_Proveedores integer ,
FOREIGN key ( ID_Proveedores) REFERENCES Provedores (ID_Provedores) 
);
 drop  table Cat_Productos 
 
 
CREATE TABLE Meto_pagos (
ID_Meto_Pagos INTEGER PRIMARY KEY AUTOINCREMENT,
nombres text,
F_Alta datetime,
F_Baja datetime
);

CREATE TABLE ENVIOS (
ID_Envios INTEGER PRIMARY KEY AUTOINCREMENT,
ID_Ventas integer ,
fecha  datetime ,
destino text ,
remitente text ,
FOREIGN KEY (ID_Ventas) REFERENCES ventas  (ID_Ventas)
);


create table Comprobantes (
ID_Comprobantes INTEGER PRIMARY KEY AUTOINCREMENT ,
ID_Tipo_cromprobantes integer ,
fecha datetime ,
IVA text ,
total real ,
FOREIGN KEY (ID_Tipo_cromprobantes)  REFERENCES Tipo_Comprobantes (ID_Tipo_cromprobantes)
);

create table Tipo_Combrobantes (
ID_Tipo_Combrobantes INTEGER PRIMARY KEY AUTOINCREMENT , 
nombre text ,
F_Alta datetime ,
F_Baja datetime 
);


create table Cat_producto(
ID_Cat_Producto INTEGER PRIMARY KEY AUTOINCREMENT,
ID_provedores integer ,
FOREIGN KEY ( ID_provedores )  REFERENCES Provedores (ID_Provedores)
);

create table Devoluciones (
ID_Devoluciones INTEGER PRIMARY KEY AUTOINCREMENT ,
ID_Productos integer ,
fecha datetime ,
FOREIGN KEY (ID_Productos)  REFERENCES Productos (ID_Productos)
);

create table Proveedores (
ID_Proveedores INTEGER PRIMARY KEY AUTOINCREMENT ,
ID_Clientes  INTEGER ,
nombre  TEXT ,
direccion TEXT ,
CUIT TEXT , 
DNI TEXT,
FOREIGN KEY ( ID_Clientes ) REFERENCES clientes ( ID_Clientes)

);



	