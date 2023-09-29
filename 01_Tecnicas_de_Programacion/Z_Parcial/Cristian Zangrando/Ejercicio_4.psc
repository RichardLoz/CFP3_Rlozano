Algoritmo Ejercicio_4
	//Definir nombres
	Definir nombres Como Caracter;
	Definir i Como Entero;
	//inicializar variable
	i <- 0;
	//Dimensionar variable
	Dimension nombres[5];
	//inicializar variable 
	Para i <- 0 Hasta 5 Hacer
		nombres[i] <- " ";
	FinPara
	//lectura de variable
	Para i <- 0 Hasta 5 Hacer
		Escribir "ingrese el nombre",i + 1;
		Leer nombres[i];
	FinPara
	//Mostrar la variable
	Para i <- 0 Hasta 5 Hacer
		 Escribir nombres[i] , " " 
		FinPara
	FinAlgoritmo
