Algoritmo ejercicio3
	Definir arregloNum Como Entero
	Imprimir " ingrese la dimension del arreglo "
	leer dimArreglo
	Dimension arregloNum[dimArreglo]
	acumulador = 0
	Para i = 0 Hasta dimArreglo - 1 Con Paso 1 Hacer
		Imprimir " ingrese los numeros para el arreglo: "
		leer arregloNum[i]
		acumulador = acumulador + arregloNum[i]
	Fin Para
	Imprimir " la suma de todos loa numeros es: " acumulador
FinAlgoritmo
