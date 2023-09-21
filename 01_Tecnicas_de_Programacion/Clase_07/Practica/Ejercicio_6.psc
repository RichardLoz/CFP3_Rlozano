Algoritmo Ejercicio_6
	//Dimension del arreglo 4
	Dimension arreglo1[4]
	Dimension arreglo2[4]
	Dimension arreglo3[4]
	
	Para i = 0 Hasta 4-1 Con Paso 1 Hacer
		Imprimir "Ingrese el valor para el arreglo1: "
		leer arreglo1[i]
		Imprimir "Ingrese el valor para el arreglo2: "
		leer arreglo2[i]
		arreglo3[i] = arreglo1[i] + arreglo2[i]
	Fin Para
	Para i = 0 Hasta 4-1 Con Paso 1 Hacer
		Imprimir arreglo1[i] " + " arreglo2[i] " = " arreglo3[i]
	Fin Para
FinAlgoritmo
