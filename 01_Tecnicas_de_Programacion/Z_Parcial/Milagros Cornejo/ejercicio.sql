create table if not EXISTS  cliente(
ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT ,
nombre text ,
apellido text, 
correo_electronico text,
telefono text 
)

create table if not EXISTS Reclamo (
ID_Reclamo INTEGER PRIMARY KEY AUTOINCREMENT,
fecha datetime,
hora datetime ,
descripcion_Recla text ,
ID_Cliente integer ,
estado_Recla text, 
FOREIGN KEY (ID_Cliente) REFERENCES Cliente (ID_Cliente)
)

CREATE table if not EXISTS Departamento (
ID_Departamento INTEGER PRIMARY KEY AUTOINCREMENT ,
nombre text
)

Drop table  Departamento

Create table if not EXISTS Empleado (
ID_Empleado INTEGER PRIMARY KEY AUTOINCREMENT ,
nombre text,
apellido text,
ID_Departamento integer ,
FOREIGN key (ID_Departamento) REFERENCES Departamento ( ID_Departamento)
)


insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Corette', 'Carl', 'ccarl0@army.mil', '678-997-0293');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Colby', 'Clitsome', 'cclitsome1@comcast.net', '102-730-6064');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Debby', 'Purveys', 'dpurveys2@latimes.com', '436-486-0658');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Artus', 'Piner', 'apiner3@businessinsider.com', '676-831-1544');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Siward', 'Rodd', 'srodd4@dagondesign.com', '565-896-5389');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Hendrik', 'Stut', 'hstut5@discuz.net', '459-204-8369');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Devon', 'Marzellano', 'dmarzellano6@boston.com', '811-793-8004');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Lesley', 'Garrow', 'lgarrow7@ebay.co.uk', '126-377-6973');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Andrey', 'MacCurley', 'amaccurley8@deviantart.com', '670-733-6792');
insert into cliente (nombre, apellido, correo_electronico, telefono) values ('Sybille', 'Weldrick', 'sweldrick9@cmu.edu', '473-799-2924');


insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('7/10/2023', '3:20 AM', 'Obstructive sleep apnea (adult) (pediatric)', 10, 'Obstructive sleep apnea (adult) (pediatric)');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('12/8/2023', '2:13 PM', 'Other nerve root and plexus disorders', 2, 'Other nerve root and plexus disorders');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('7/7/2023', '10:34 AM', 'Military firearm discharge, undetermined intent, init encntr', 5, 'Military firearm discharge, undetermined intent, initial encounter');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('20/7/2023', '12:22 PM', 'Prem separtn of placenta w coag defect, unsp, second tri', 1, 'Premature separation of placenta with coagulation defect, unspecified, second trimester');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('3/10/2023', '2:03 AM', 'Person on outside of car injured in collision w SUV in traf', 6, 'Person on outside of car injured in collision with sport utility vehicle in traffic accident');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('28/10/2023', '5:35 AM', 'Poisoning by alpha-adrenocpt antagonists, accidental, init', 10, 'Poisoning by alpha-adrenoreceptor antagonists, accidental (unintentional), initial encounter');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('29/9/2023', '1:30 PM', 'Other superficial bite of right elbow, subsequent encounter', 10, 'Other superficial bite of right elbow, subsequent encounter');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('1/10/2023', '3:43 AM', 'Legal intervnt w unsp firearm disch, law enforc offl injured', 7, 'Legal intervention involving unspecified firearm discharge, law enforcement official injured');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('9/10/2023', '1:32 PM', 'Encounter for suprvsn of normal pregnancy, first trimester', 10, 'Encounter for supervision of other normal pregnancy, first trimester');
insert into Reclamo (fecha, hora, descripcion_Recla, id_cliente, estado_Recla) values ('30/6/2023', '12:04 AM', 'Animl-ridr injured by fall fr horse in nonclsn acc, sequela', 5, 'Animal-rider injured by fall from or being thrown from horse in noncollision accident, sequela');

insert into Departamento (nombre) values ('soporte_tecnico');
insert into Departamento (nombre) values ('facturacion');
insert into Departamento (nombre) values ('servicio_cliente');


insert into empleado (nombre, apellido, id_departamento) values ('Tiertza', 'Camden', 1);
insert into empleado (nombre, apellido, id_departamento) values ('Peirce', 'Allden', 1);
insert into empleado (nombre, apellido, id_departamento) values ('Libbie', 'Rousby', 2);
insert into empleado (nombre, apellido, id_departamento) values ('Ike', 'Gerran', 3);
insert into empleado (nombre, apellido, id_departamento) values ('Siegfried', 'Sitford', 3);
insert into empleado (nombre, apellido, id_departamento) values ('Seumas', 'Baskerfield', 2);
insert into empleado (nombre, apellido, id_departamento) values ('Vinson', 'Levings', 1);
insert into empleado (nombre, apellido, id_departamento) values ('Lem', 'Lindl', 1);
insert into empleado (nombre, apellido, id_departamento) values ('Jack', 'Sheed', 2);
insert into empleado (nombre, apellido, id_departamento) values ('Elonore', 'Songist', 3);
