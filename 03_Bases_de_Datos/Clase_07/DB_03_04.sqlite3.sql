BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Sucursales" (
	"id_sucursal"	INTEGER NOT NULL,
	"nombre"	text NOT NULL,
	"direccion"	text NOT NULL,
	"telefono"	text NOT NULL,
	PRIMARY KEY("id_sucursal" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "vendedores" (
	"id_vendedor"	INTEGER NOT NULL,
	"nombre"	text NOT NULL,
	"apellido"	text NOT NULL,
	"edad"	INTEGER NOT NULL,
	"direccion"	text NOT NULL,
	"id_sucursal"	integer,
	FOREIGN KEY("id_sucursal") REFERENCES "Sucursales"("id_sucursal"),
	PRIMARY KEY("id_vendedor" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Clientes" (
	"id_cliente"	INTEGER NOT NULL,
	"nombre"	text NOT NULL,
	"apellido"	text NOT NULL,
	"edad"	INTEGER NOT NULL,
	"direccion"	text NOT NULL,
	"telefono"	text NOT NULL,
	"correo"	text NOT NULL,
	PRIMARY KEY("id_cliente" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Automoviles" (
	"id_auto"	INTEGER NOT NULL,
	"marca"	text NOT NULL,
	"modelo"	text NOT NULL,
	"anio"	datetime NOT NULL,
	"color"	text NOT NULL,
	"tipo_combustible"	 NOT NULL,
	"transmision"	text NOT NULL,
	"id_sucursal"	INTEGER,
	FOREIGN KEY("id_sucursal") REFERENCES "Sucursales"("id_sucursal"),
	PRIMARY KEY("id_auto" AUTOINCREMENT)
);
INSERT INTO "Sucursales" VALUES (1,'Nuñez','PO Box 27517','629 506 9157');
INSERT INTO "Sucursales" VALUES (2,'Nordelta','Room 1786','644 922 4490');
INSERT INTO "Sucursales" VALUES (3,'Escobar','PO Box 11746','822 530 4972');
INSERT INTO "Sucursales" VALUES (4,'Devoto','15th Floor','159 968 1549');
INSERT INTO "Sucursales" VALUES (5,'Belgrano','20th Floor','781 680 0723');
INSERT INTO "Sucursales" VALUES (6,'Once','Suite 62','168 269 5408');
INSERT INTO "Sucursales" VALUES (7,'Palermo','PO Box 17435','630 827 7834');
INSERT INTO "Sucursales" VALUES (8,'Colegiales','6th Floor','742 416 1099');
INSERT INTO "Sucursales" VALUES (9,'Saavedra','PO Box 80242','655 812 5592');
INSERT INTO "Sucursales" VALUES (10,'Benavidez','PO Box 32474','990 974 9054');
INSERT INTO "vendedores" VALUES (1,'Missy','Eccles',31,'3907 Karstens Avenue',4);
INSERT INTO "vendedores" VALUES (2,'Harry','Kingzett',50,'736 Anniversary Point',5);
INSERT INTO "vendedores" VALUES (3,'Bartram','Ciottoi',50,'32712 Longview Circle',8);
INSERT INTO "vendedores" VALUES (4,'Darcie','Abrahams',49,'161 Butterfield Way',6);
INSERT INTO "vendedores" VALUES (5,'Joyann','Tennison',22,'6187 Superior Crossing',8);
INSERT INTO "vendedores" VALUES (6,'Cosetta','Press',41,'62610 Forest Trail',2);
INSERT INTO "vendedores" VALUES (7,'Cloris','Freen',26,'96421 Basil Point',7);
INSERT INTO "vendedores" VALUES (8,'Loree','Blenkensop',57,'57780 Superior Park',2);
INSERT INTO "vendedores" VALUES (9,'Velvet','Wagg',30,'46 Marquette Circle',9);
INSERT INTO "vendedores" VALUES (10,'Lorrayne','Vogt',49,'380 Veith Pass',10);
INSERT INTO "vendedores" VALUES (11,'Emmit','Torrese',57,'64 Burning Wood Avenue',9);
INSERT INTO "vendedores" VALUES (12,'Johanna','Knobell',25,'2 Debs Way',8);
INSERT INTO "vendedores" VALUES (13,'Winn','Charlick',53,'6455 Mayfield Court',10);
INSERT INTO "vendedores" VALUES (14,'Mal','Tubridy',44,'947 Ridge Oak Hill',3);
INSERT INTO "vendedores" VALUES (15,'Ingaborg','Louden',41,'57451 Melrose Court',8);
INSERT INTO "vendedores" VALUES (16,'Xerxes','McCurtain',48,'894 Division Street',7);
INSERT INTO "vendedores" VALUES (17,'Elicia','Rogliero',26,'7396 Scott Plaza',7);
INSERT INTO "vendedores" VALUES (18,'Veronique','Beran',34,'28263 Porter Terrace',6);
INSERT INTO "vendedores" VALUES (19,'Mufi','Camier',51,'74731 Village Parkway',9);
INSERT INTO "vendedores" VALUES (20,'Wallis','Garber',28,'28 Pawling Avenue',8);
INSERT INTO "vendedores" VALUES (21,'Eamon','Spurgin',57,'0700 Eagan Alley',1);
INSERT INTO "vendedores" VALUES (22,'Rurik','Phillipson',22,'1 Portage Parkway',10);
INSERT INTO "vendedores" VALUES (23,'Randall','Kielt',57,'2900 Forest Dale Park',8);
INSERT INTO "vendedores" VALUES (24,'Rene','Kelston',32,'23630 Barby Lane',9);
INSERT INTO "vendedores" VALUES (25,'Bendick','Tripe',20,'70 Oriole Plaza',2);
INSERT INTO "vendedores" VALUES (26,'Anabelle','Leek',54,'68 Stang Drive',1);
INSERT INTO "vendedores" VALUES (27,'Robinette','Silverthorn',24,'8667 Barby Lane',3);
INSERT INTO "vendedores" VALUES (28,'Jocelyn','Howsan',26,'6606 Bultman Junction',7);
INSERT INTO "vendedores" VALUES (29,'Reinaldo','Filip',38,'7 Hagan Trail',3);
INSERT INTO "vendedores" VALUES (30,'Rosette','Cheevers',34,'4451 Mayfield Terrace',4);
INSERT INTO "vendedores" VALUES (31,'Levey','Torrent',51,'6331 Luster Pass',1);
INSERT INTO "vendedores" VALUES (32,'Wendel','Eacott',20,'15 Arizona Plaza',1);
INSERT INTO "vendedores" VALUES (33,'Kettie','Gutowski',54,'2980 Pond Lane',9);
INSERT INTO "vendedores" VALUES (34,'Felisha','Barsham',49,'47 Ruskin Park',1);
INSERT INTO "vendedores" VALUES (35,'Gilberte','Purtell',58,'1297 Buhler Circle',1);
INSERT INTO "vendedores" VALUES (36,'Gay','Dehn',34,'722 Charing Cross Alley',3);
INSERT INTO "vendedores" VALUES (37,'Roanne','Manoelli',27,'48 Vidon Park',10);
INSERT INTO "vendedores" VALUES (38,'Angeline','Dell ''Orto',37,'85242 Duke Road',6);
INSERT INTO "vendedores" VALUES (39,'Grove','Haldene',21,'532 Corben Circle',5);
INSERT INTO "vendedores" VALUES (40,'Caressa','Franek',20,'2424 Bultman Plaza',6);
INSERT INTO "Clientes" VALUES (1,'Nicoline','Trustie',56,'7 Marquette Avenue','607 502 2663','ntrustie0@people.com.cn');
INSERT INTO "Clientes" VALUES (2,'Neddy','Kelberman',65,'388 Hoard Hill','693 146 4070','nkelberman1@apple.com');
INSERT INTO "Clientes" VALUES (3,'Melessa','Scrimgeour',60,'095 Katie Point','248 723 1532','mscrimgeour2@rambler.ru');
INSERT INTO "Clientes" VALUES (4,'Taddeusz','Greatbach',74,'86596 Paget Hill','311 997 9450','tgreatbach3@bbb.org');
INSERT INTO "Clientes" VALUES (5,'Dita','Ridgers',50,'4664 Ridgeview Street','605 254 3816','dridgers4@nationalgeographic.com');
INSERT INTO "Clientes" VALUES (6,'Minetta','Aspital',44,'0 Reinke Junction','720 679 8095','maspital5@typepad.com');
INSERT INTO "Clientes" VALUES (7,'Hadrian','Luto',34,'0526 Fairview Point','467 760 7812','hluto6@wikimedia.org');
INSERT INTO "Clientes" VALUES (8,'Otha','Saben',42,'08 Rusk Road','840 128 2120','osaben7@nationalgeographic.com');
INSERT INTO "Clientes" VALUES (9,'Trenton','Gaythor',52,'66802 Thierer Alley','523 193 6383','tgaythor8@addtoany.com');
INSERT INTO "Clientes" VALUES (10,'Steffie','Fronek',57,'077 Southridge Road','933 165 1515','sfronek9@wikimedia.org');
INSERT INTO "Clientes" VALUES (11,'Stefanie','Sargood',72,'9 Linden Point','164 228 1219','ssargooda@businessinsider.com');
INSERT INTO "Clientes" VALUES (12,'Galven','Tyers',79,'46 Superior Drive','229 958 0382','gtyersb@microsoft.com');
INSERT INTO "Clientes" VALUES (13,'Helenelizabeth','Huyge',66,'8 Bayside Terrace','840 369 1790','hhuygec@pen.io');
INSERT INTO "Clientes" VALUES (14,'Salomo','Mohun',48,'061 Barby Hill','953 838 3486','smohund@ed.gov');
INSERT INTO "Clientes" VALUES (15,'Currey','Eeles',68,'452 Lotheville Junction','361 154 0490','ceelese@weibo.com');
INSERT INTO "Clientes" VALUES (16,'Delia','Itzchaky',54,'6 Manitowish Center','632 457 9884','ditzchakyf@cafepress.com');
INSERT INTO "Clientes" VALUES (17,'Mable','Brockington',49,'08515 Pond Center','412 758 3214','mbrockingtong@nyu.edu');
INSERT INTO "Clientes" VALUES (18,'Alverta','Lambotin',34,'66 Stang Hill','112 316 9482','alambotinh@webs.com');
INSERT INTO "Clientes" VALUES (19,'Hershel','Kayser',50,'147 Cascade Terrace','408 172 4145','hkayseri@rambler.ru');
INSERT INTO "Clientes" VALUES (20,'Delphinia','Trembey',24,'19 Acker Crossing','279 371 9218','dtrembeyj@vistaprint.com');
INSERT INTO "Clientes" VALUES (21,'Timotheus','Fillery',21,'54 Lukken Circle','848 474 2085','tfilleryk@e-recht24.de');
INSERT INTO "Clientes" VALUES (22,'Theressa','Dhillon',70,'55 Transport Center','947 894 6518','tdhillonl@springer.com');
INSERT INTO "Clientes" VALUES (23,'Sinclare','Byram',45,'195 Rieder Street','149 478 4577','sbyramm@paypal.com');
INSERT INTO "Clientes" VALUES (24,'Kaila','Prangley',26,'99 Scofield Center','639 550 1826','kprangleyn@mail.ru');
INSERT INTO "Clientes" VALUES (25,'Danielle','Lintin',41,'4 Bluejay Place','339 918 5189','dlintino@skype.com');
INSERT INTO "Clientes" VALUES (26,'Nanete','Cappleman',64,'678 Thackeray Court','947 441 6543','ncapplemanp@nbcnews.com');
INSERT INTO "Clientes" VALUES (27,'Baird','Slyme',55,'8 Vidon Hill','862 715 7378','bslymeq@va.gov');
INSERT INTO "Clientes" VALUES (28,'Sauncho','Fairbank',23,'87 Lotheville Place','562 960 9629','sfairbankr@parallels.com');
INSERT INTO "Clientes" VALUES (29,'Washington','Nice',54,'303 Elmside Street','948 951 9672','wnices@disqus.com');
INSERT INTO "Clientes" VALUES (30,'Bendick','Tackett',42,'146 Messerschmidt Trail','565 361 9032','btackettt@plala.or.jp');
INSERT INTO "Clientes" VALUES (31,'Waldo','Davidavidovics',23,'9 6th Street','355 283 8994','wdavidavidovicsu@furl.net');
INSERT INTO "Clientes" VALUES (32,'Dag','Davidde',36,'86 Charing Cross Circle','254 856 5263','ddaviddev@scientificamerican.com');
INSERT INTO "Clientes" VALUES (33,'Lambert','Casson',68,'7 Melvin Circle','114 849 6685','lcassonw@bloomberg.com');
INSERT INTO "Clientes" VALUES (34,'Elvira','Everest',78,'41604 Hayes Lane','483 349 3126','eeverestx@aol.com');
INSERT INTO "Clientes" VALUES (35,'Donnie','De Ferraris',70,'6563 Badeau Road','569 446 1015','ddeferrarisy@yale.edu');
INSERT INTO "Clientes" VALUES (36,'Ev','Gallaccio',59,'52 Hayes Road','832 187 5815','egallaccioz@webs.com');
INSERT INTO "Clientes" VALUES (37,'Binny','Strangeway',31,'617 Monica Parkway','530 950 4491','bstrangeway10@usgs.gov');
INSERT INTO "Clientes" VALUES (38,'Beauregard','Hawney',42,'8120 Canary Point','606 767 1945','bhawney11@imgur.com');
INSERT INTO "Clientes" VALUES (39,'Ambrose','Fielding',76,'93960 Sullivan Place','595 553 8024','afielding12@instagram.com');
INSERT INTO "Clientes" VALUES (40,'Sophronia','Johantges',72,'669 Cherokee Parkway','691 729 6755','sjohantges13@stanford.edu');
INSERT INTO "Automoviles" VALUES (1,'Dodge','Ram Wagon B150',1994,'Indigo','Diesel','Manual',1);
INSERT INTO "Automoviles" VALUES (2,'Subaru','Legacy',1991,'Aquamarine','Nafta','Automatico',2);
INSERT INTO "Automoviles" VALUES (3,'Dodge','Ram 2500',2009,'Green','Electrico','Automatico',8);
INSERT INTO "Automoviles" VALUES (4,'Toyota','Prius',2004,'Goldenrod','Nafta','Automatico',9);
INSERT INTO "Automoviles" VALUES (5,'Jaguar','XJ Series',2001,'Yellow','Nafta','Manual',9);
INSERT INTO "Automoviles" VALUES (6,'Volkswagen','Quantum',1984,'Khaki','Nafta','Manual',10);
INSERT INTO "Automoviles" VALUES (7,'Mitsubishi','Lancer',2003,'Teal','Nafta','Manual',10);
INSERT INTO "Automoviles" VALUES (8,'Buick','Park Avenue',2003,'Green','Electrico','Automatico',1);
INSERT INTO "Automoviles" VALUES (9,'Pontiac','Grand Prix',1974,'Khaki','Electrico','Automatico',5);
INSERT INTO "Automoviles" VALUES (10,'Oldsmobile','Bravada',2000,'Orange','Diesel','Manual',2);
INSERT INTO "Automoviles" VALUES (11,'Volkswagen','Passat',1988,'Indigo','Diesel','Manual',8);
INSERT INTO "Automoviles" VALUES (12,'Volvo','V50',2011,'Green','Diesel','Manual',8);
INSERT INTO "Automoviles" VALUES (13,'Daewoo','Leganza',2002,'Yellow','Diesel','Manual',4);
INSERT INTO "Automoviles" VALUES (14,'Nissan','Versa',2011,'Crimson','Diesel','Automatico',10);
INSERT INTO "Automoviles" VALUES (15,'Buick','Riviera',1992,'Maroon','Nafta','Automatico',6);
INSERT INTO "Automoviles" VALUES (16,'Honda','Civic',2004,'Pink','Nafta','Automatico',1);
INSERT INTO "Automoviles" VALUES (17,'BMW','X5',2013,'Yellow','Electrico','Automatico',7);
INSERT INTO "Automoviles" VALUES (18,'Plymouth','Sundance',1992,'Crimson','Diesel','Automatico',6);
INSERT INTO "Automoviles" VALUES (19,'Audi','A8',2001,'Yellow','Nafta','Manual',6);
INSERT INTO "Automoviles" VALUES (20,'Lexus','GX',2008,'Aquamarine','Nafta','Automatico',1);
INSERT INTO "Automoviles" VALUES (21,'Cadillac','Fleetwood',1996,'Mauv','Diesel','Manual',9);
INSERT INTO "Automoviles" VALUES (22,'Ford','F-Series Super Duty',2011,'Aquamarine','Electrico','Manual',4);
INSERT INTO "Automoviles" VALUES (23,'Chevrolet','Blazer',1992,'Orange','Electrico','Manual',1);
INSERT INTO "Automoviles" VALUES (24,'Mitsubishi','Pajero',1988,'Teal','Electrico','Manual',5);
INSERT INTO "Automoviles" VALUES (25,'Ford','ZX2',2001,'Blue','Diesel','Automatico',2);
INSERT INTO "Automoviles" VALUES (26,'Plymouth','Colt Vista',1993,'Maroon','Electrico','Manual',8);
INSERT INTO "Automoviles" VALUES (27,'Lexus','LS',1991,'Crimson','Electrico','Automatico',4);
INSERT INTO "Automoviles" VALUES (28,'Dodge','Ram Van 2500',1995,'Turquoise','Diesel','Automatico',10);
INSERT INTO "Automoviles" VALUES (29,'Volvo','XC70',2003,'Crimson','Electrico','Manual',9);
INSERT INTO "Automoviles" VALUES (30,'Suzuki','X-90',1996,'Purple','Nafta','Manual',3);
INSERT INTO "Automoviles" VALUES (31,'Chrysler','Town & Country',1995,'Khaki','Diesel','Automatico',9);
INSERT INTO "Automoviles" VALUES (32,'Mercury','Topaz',1990,'Orange','Electrico','Automatico',4);
INSERT INTO "Automoviles" VALUES (33,'Mercedes-Benz','SLK-Class',2003,'Aquamarine','Nafta','Manual',9);
INSERT INTO "Automoviles" VALUES (34,'Pontiac','Sunbird',1989,'Aquamarine','Diesel','Automatico',10);
INSERT INTO "Automoviles" VALUES (35,'Land Rover','Range Rover',2010,'Yellow','Electrico','Manual',6);
INSERT INTO "Automoviles" VALUES (36,'Lexus','CT',2011,'Pink','Diesel','Automatico',8);
INSERT INTO "Automoviles" VALUES (37,'Ford','Windstar',1999,'Turquoise','Electrico','Automatico',1);
INSERT INTO "Automoviles" VALUES (38,'Ford','Thunderbird',1986,'Purple','Electrico','Automatico',9);
INSERT INTO "Automoviles" VALUES (39,'Honda','Civic',1994,'Red','Nafta','Manual',4);
INSERT INTO "Automoviles" VALUES (40,'Lincoln','Navigator L',2010,'Indigo','Diesel','Manual',1);
INSERT INTO "Automoviles" VALUES (41,'Toyota','Corolla',1998,'Teal','Electrico','Manual',10);
INSERT INTO "Automoviles" VALUES (42,'BMW','530',2002,'Teal','Diesel','Automatico',3);
INSERT INTO "Automoviles" VALUES (43,'Lotus','Elan',1993,'Green','Diesel','Automatico',4);
INSERT INTO "Automoviles" VALUES (44,'Hyundai','Entourage',2007,'Crimson','Electrico','Manual',6);
INSERT INTO "Automoviles" VALUES (45,'Mitsubishi','GTO',1991,'Puce','Electrico','Automatico',10);
INSERT INTO "Automoviles" VALUES (46,'Ford','Fusion',2010,'Khaki','Diesel','Manual',1);
INSERT INTO "Automoviles" VALUES (47,'GMC','Savana',2007,'Red','Nafta','Automatico',4);
INSERT INTO "Automoviles" VALUES (48,'Chrysler','Cirrus',2000,'Puce','Diesel','Automatico',6);
INSERT INTO "Automoviles" VALUES (49,'Scion','xB',2009,'Khaki','Diesel','Automatico',3);
INSERT INTO "Automoviles" VALUES (50,'Infiniti','Q',2002,'Green','Electrico','Manual',3);
INSERT INTO "Automoviles" VALUES (51,'Nissan','Maxima',2001,'Orange','Nafta','Manual',1);
INSERT INTO "Automoviles" VALUES (52,'Pontiac','Firefly',1990,'Violet','Nafta','Manual',4);
INSERT INTO "Automoviles" VALUES (53,'Land Rover','Discovery',2006,'Pink','Nafta','Manual',9);
INSERT INTO "Automoviles" VALUES (54,'Chevrolet','Express 1500',2011,'Crimson','Electrico','Manual',10);
INSERT INTO "Automoviles" VALUES (55,'Land Rover','Range Rover',1995,'Puce','Diesel','Automatico',6);
INSERT INTO "Automoviles" VALUES (56,'Volkswagen','New Beetle',2003,'Aquamarine','Nafta','Manual',7);
INSERT INTO "Automoviles" VALUES (57,'Land Rover','Discovery',2011,'Aquamarine','Nafta','Manual',7);
INSERT INTO "Automoviles" VALUES (58,'Ford','Club Wagon',1996,'Red','Nafta','Automatico',8);
INSERT INTO "Automoviles" VALUES (59,'Lincoln','MKS',2012,'Maroon','Electrico','Automatico',8);
INSERT INTO "Automoviles" VALUES (60,'Mercedes-Benz','R-Class',2009,'Yellow','Electrico','Manual',7);
INSERT INTO "Automoviles" VALUES (61,'Ford','Expedition',2005,'Khaki','Diesel','Automatico',4);
INSERT INTO "Automoviles" VALUES (62,'Chevrolet','3500',2000,'Violet','Nafta','Manual',5);
INSERT INTO "Automoviles" VALUES (63,'Isuzu','Hombre',2000,'Maroon','Diesel','Manual',6);
INSERT INTO "Automoviles" VALUES (64,'Chevrolet','Aveo',2009,'Orange','Electrico','Manual',4);
INSERT INTO "Automoviles" VALUES (65,'Audi','A6',2004,'Pink','Diesel','Automatico',1);
INSERT INTO "Automoviles" VALUES (66,'Cadillac','CTS',2009,'Blue','Diesel','Manual',4);
INSERT INTO "Automoviles" VALUES (67,'Mercury','Villager',1995,'Mauv','Diesel','Automatico',3);
INSERT INTO "Automoviles" VALUES (68,'Lexus','ES',1991,'Khaki','Electrico','Automatico',2);
INSERT INTO "Automoviles" VALUES (69,'Chevrolet','Express 2500',2007,'Purple','Diesel','Manual',8);
INSERT INTO "Automoviles" VALUES (70,'Honda','Fit',2010,'Khaki','Electrico','Automatico',4);
INSERT INTO "Automoviles" VALUES (71,'Lexus','HS',2010,'Indigo','Nafta','Automatico',5);
INSERT INTO "Automoviles" VALUES (72,'Mazda','Miata MX-5',2011,'Indigo','Electrico','Manual',10);
INSERT INTO "Automoviles" VALUES (73,'Volkswagen','Cabriolet',2001,'Yellow','Electrico','Automatico',6);
INSERT INTO "Automoviles" VALUES (74,'Chevrolet','2500',1995,'Teal','Nafta','Automatico',9);
INSERT INTO "Automoviles" VALUES (75,'Audi','Allroad',2005,'Fuscia','Diesel','Automatico',5);
INSERT INTO "Automoviles" VALUES (76,'Mercedes-Benz','CL-Class',2009,'Blue','Electrico','Manual',8);
INSERT INTO "Automoviles" VALUES (77,'Land Rover','Range Rover',2006,'Yellow','Electrico','Automatico',7);
INSERT INTO "Automoviles" VALUES (78,'Volvo','V70',2007,'Khaki','Nafta','Automatico',4);
INSERT INTO "Automoviles" VALUES (79,'Infiniti','G',2000,'Mauv','Diesel','Automatico',3);
INSERT INTO "Automoviles" VALUES (80,'Chrysler','Prowler',2001,'Goldenrod','Diesel','Manual',9);
INSERT INTO "Automoviles" VALUES (81,'Chevrolet','Camaro',1967,'Green','Diesel','Manual',7);
INSERT INTO "Automoviles" VALUES (82,'Ford','F350',2000,'Red','Diesel','Manual',8);
INSERT INTO "Automoviles" VALUES (83,'Chrysler','300M',2002,'Turquoise','Electrico','Manual',8);
INSERT INTO "Automoviles" VALUES (84,'Mercury','Sable',1998,'Maroon','Nafta','Manual',2);
INSERT INTO "Automoviles" VALUES (85,'Mazda','B2600',1989,'Goldenrod','Diesel','Manual',5);
INSERT INTO "Automoviles" VALUES (86,'Toyota','Paseo',1995,'Blue','Diesel','Manual',9);
INSERT INTO "Automoviles" VALUES (87,'Dodge','Ram 1500',2005,'Red','Diesel','Automatico',10);
INSERT INTO "Automoviles" VALUES (88,'Dodge','Grand Caravan',2010,'Pink','Nafta','Manual',4);
INSERT INTO "Automoviles" VALUES (89,'Porsche','Boxster',1997,'Indigo','Electrico','Automatico',7);
INSERT INTO "Automoviles" VALUES (90,'Chevrolet','G-Series 2500',1996,'Crimson','Nafta','Manual',1);
INSERT INTO "Automoviles" VALUES (91,'Nissan','Frontier',2012,'Indigo','Nafta','Manual',4);
INSERT INTO "Automoviles" VALUES (92,'Honda','Pilot',2003,'Maroon','Electrico','Manual',10);
INSERT INTO "Automoviles" VALUES (93,'Ford','GT',2006,'Crimson','Nafta','Automatico',5);
INSERT INTO "Automoviles" VALUES (94,'Chevrolet','Corvette',1969,'Puce','Diesel','Manual',4);
INSERT INTO "Automoviles" VALUES (95,'Hyundai','Scoupe',1992,'Teal','Diesel','Automatico',9);
INSERT INTO "Automoviles" VALUES (96,'Mitsubishi','Galant',1996,'Pink','Nafta','Manual',10);
INSERT INTO "Automoviles" VALUES (97,'Volkswagen','New Beetle',2010,'Red','Nafta','Manual',3);
INSERT INTO "Automoviles" VALUES (98,'Porsche','928',1989,'Purple','Diesel','Automatico',2);
INSERT INTO "Automoviles" VALUES (99,'Suzuki','Esteem',2001,'Khaki','Nafta','Manual',8);
INSERT INTO "Automoviles" VALUES (100,'Maserati','GranSport',2005,'Purple','Nafta','Manual',10);
COMMIT;
