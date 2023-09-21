Algoritmo Ejercicios_8
	definir arregloNumeros Como Entero
	Dimension arregloNumeros[10]
	numMayor = 0
	Para i = 0 Hasta 10 - 1 Con Paso 1 Hacer
		arregloNumeros[i] = azar(100)
		si arregloNumeros[i] > numMayor Entonces
			numMayor = arregloNumeros[i]
		FinSi
	Fin Para
	
	Imprimir "El numero mayor del arreglo es: " numMayor
	
	
FinAlgoritmo
