Algoritmo arregloDimencional
	//3-	Declara un arreglo unidimensional llamado "numeros" con dimensi� dinamica. 
	//Luego llenar el arreglo con n�meros enteros ingresados por el usuario. 
	//Luego, calcular y muestrar la suma de todos los n�meros pares en el arreglo.
	Definir numArreglo Como Entero
	Imprimir "ingrese la dimension del arreglo: "
	leer num 
	Dimension numArreglo[5]
	Para i=0 Hasta 5-1 Con Paso 1 Hacer
		Imprimir "Ingrese el valor para la posicion: " i, " del arreglo: "
		leer numArreglo[i]
	Fin Para
	Para i = 0 Hasta 5-1 Con Paso 1 Hacer
		Imprimir "El valor es la posicion ", i , " es: ", numArreglo[i]
	Fin Para
	
FinAlgoritmo
