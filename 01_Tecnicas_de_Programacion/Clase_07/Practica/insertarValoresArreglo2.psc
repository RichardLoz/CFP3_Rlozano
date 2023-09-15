Algoritmo insertarValoresArreglo2
	//Definimos el tipo de dato del arreglo
	definir valorArreglo Como Entero
	
	// Definimos la Dimension del arreglo
	Dimension valorArreglo[5]
	
	//Utilizamos un ciclo Para solicitar valores para llenar el arreglo
	para i = 0 Hasta 5-1 con paso 1 Hacer
		Imprimir "Ingrese el valor para la posicion: " i, " del arreglo: "
		leer valorArreglo[i]
	FinPara
	
	Para i = 0 Hasta 5-1 Con Paso 1 Hacer
		Imprimir "El valor es la posicion ", i , " es: ", valorArreglo[i]
	Fin Para
	
FinAlgoritmo