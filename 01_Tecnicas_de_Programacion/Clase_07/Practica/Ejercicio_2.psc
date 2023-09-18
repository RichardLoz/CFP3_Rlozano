Algoritmo Ejercicio_2
	definir dimensionArreglo, valoresArreglo Como Entero
	Imprimir "Ingresar la dimension del arreglo: "
	leer dimensionArreglo
	dimension valoresArreglo[dimensionArreglo]
	
	//Pedimos los numeros del arreglo
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "Ingresar los numeros del arreglo: "
		leer valoresArreglo[i]
	Fin Para
	mayor = valoresArreglo[0]
	menor = valoresArreglo[0]
	
	Para i = 1 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Si valoresArreglo[i] > mayor Entonces
			mayor = valoresArreglo[i]
		SiNo
			Si valoresArreglo[i] < menor Entonces
				menor = valoresArreglo[i]
			Fin Si
		Fin Si
	Fin Para
	Imprimir "El numero mayor es: " mayor
	Imprimir "El numero menor es: " menor
	
FinAlgoritmo
