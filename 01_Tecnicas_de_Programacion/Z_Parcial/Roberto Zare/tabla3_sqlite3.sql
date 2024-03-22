CREATE table if not EXISTS Cliente (
	ID_Cliente INTEGER PRIMARY key AUTOINCREMENT,
	Nombre text,
	Apellido text,
	Email text,
	Telefono text 
	);

CREATE table if not EXISTS Reclamo (
	ID_Reclamo INTEGER PRIMARY key AUTOINCREMENT,
	Fecha datetime,
	hora datetime,
	Descripcion_Reclamo text,
	ID_Cliente INTEGER,
	Estado_del_Reclamo text,
	FOREIGN KEY(ID_Cliente)REFERENCES Cliente (ID_Cliente)
	);
	
	
CREATE table if not EXISTS Departamento (
	ID_Departamento INTEGER PRIMARY key AUTOINCREMENT,
	Nombre text
	);
	
	insert into Departamento(nombre) VALUES ('soporte_tecnico');
	insert into Departamento(Nombre)VALUES ('Facturacion');
	insert into Departamento(Nombre) VALUES ('Servicio_al_Cliente');
	

CREATE table if not EXISTS Empleado (
	ID_Empleado INTEGER PRIMARY key AUTOINCREMENT,
	Nombre text,
	Apellido text,
	ID_Departamento INTEGER,
	FOREIGN key(ID_Departamento)REFERENCES Departamento(ID_Departamento)
	);