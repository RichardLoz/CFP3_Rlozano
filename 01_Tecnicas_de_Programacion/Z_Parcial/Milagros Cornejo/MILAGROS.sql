create table  if not exists  Ventas(
 ID_ventas INTEGER PRIMARY key AUTOINCREMENT not NULL,
 id_clientes integer , 
 ID_productos integer not NULL,
 ID_metododepago interger not NULL ,
 total real not null , 
   FOREIGN KEY (ID_productos) REFERENCES productos ( ID_productos),
   FOREIGN key (ID_Clientes) REFERENCES  clientes (Id_clientes),
   FOREIGN key (ID_metododepago) REFERENCES Metododepago (ID_metododepago)
 );
  
  drop table ventas
 
 
 
 
create table if not EXISTS clientes(
 ID_Clientes INTEGER PRIMARY key AUTOINCREMENT not NULL ,
 nombre  text not null , 
 apellidos text not null , 
 CUIL      text not null , 
 telefono  text not null  ,
 direccion  text not null 
 );
 
create table if not exists  Metododepago(
 ID_Metododepago INTEGER PRIMARY key AUTOINCREMENT not NULL , 
 efectivo text  not null , 
 tarjeta   text not null ,
 transferencia text not null 
 );
 
create table if not EXISTS productos(
ID_Productos INTEGER PRIMARY key AUTOINCREMENT not NULL,
tipo text not null ,
rubro text not null , 
peso real not null ,
marca text not null ,
precio_unidad real not null  , 
stock text not null 
);
