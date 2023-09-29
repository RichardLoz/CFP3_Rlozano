Algoritmo Ej_3
	Definir dimensionArreglo, num, sumaNum Como Entero
	
	Imprimir "Ingrese la dimensión para el arreglo"
	Leer dimensionArreglo
	
	Dimension num[dimensionArreglo]
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "Ingrese un número para el arreglo"
		Leer num[i]
		Si num[i] % 2 = 0 Entonces
			sumaNum = num[i] + sumaNum
		Fin Si
	Fin Para
	
	Imprimir "La suma de todos los números pares es " sumaNum
	
FinAlgoritmo
