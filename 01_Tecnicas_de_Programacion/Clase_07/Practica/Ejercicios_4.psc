Algoritmo Ejercicios_4
	definir arregloAzar Como Entero
	Imprimir "Ingresar la dimension del arreglo: "
	leer dimensionArreglo
	
	dimension arregloAzar[dimensionArreglo]
	
	para i = 0 Hasta dimensionArreglo - 1 Hacer
		arregloAzar[i] = Azar(50)
		Imprimir arregloAzar[i]
		// Otra forma de escribirlo en una sola linea
		//Imprimir Sin Saltar arregloAzar[i], " "
	FinPara
	
FinAlgoritmo
