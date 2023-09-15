Algoritmo dimensionDinamica3
	// Definimos el tipo de dato del arreglo
	Definir numerosArreglo Como Entero
	
	//Definimos la dimension del arreglo
	Imprimir "Introducir la dimension del arreglo"
	leer dimensionArreglo
	
	//Asignamos la dimension al arreglo
	dimension numerosArreglo[dimensionArreglo]
	
	
	Para i = 0 Hasta dimensionArreglo-1 Con Paso 1
		Imprimir "Ingresar los valores del array:"
		leer numerosArreglo[i]
	Fin Para
	
	Para i = 0 Hasta dimensionArreglo-1 Con Paso 1
		Imprimir numerosArreglo[i]
	Fin Para
	
FinAlgoritmo