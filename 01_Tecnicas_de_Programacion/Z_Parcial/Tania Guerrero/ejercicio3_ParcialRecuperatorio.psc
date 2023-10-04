Algoritmo ejercicio3_ParcialRecuperatorio
	// 3-	Declara un arreglo unidimensional llamado "numeros" con dimensión dinamica. 
	//Luego llenar el arreglo con números enteros ingresados por el usuario. 
	//Luego, calcular y muestrar la suma de todos los números pares en el arreglo.
	
	Definir arregloNum , dimensionArreglo Como Entero
	Imprimir " Ingrese la dimension que desea: "
	leer dimensionArreglo
	Dimension arregloNum[dimensionArreglo]
	
	
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "Ingresar los numeros para el arreglo: "
		Leer arregloNum[i]
	Fin Para
	
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Si arregloNum[i] % 2 = 0 Entonces
			acumulador = acumulador + arregloNum[i]		 
		Fin Si
	Fin Para
	Imprimir " La suma de todos los numeros pares del arreglo es: " acumulador
	
FinAlgoritmo
