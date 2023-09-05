Algoritmo OperacionesNumeros
	// Solicito el 1er numero
	Imprimir "Ingrese el 1er numero: "
	Leer num1
	// Solicito el 2do numero
	Imprimir "Ingrese el 2do numero: "
	Leer num2
	// Calculos
	suma = num1 + num2
	resta = num1 - num2
	multi = num1 * num2
	
	// Muestro los resultado de las operaciones
	Imprimir "La suma de los numeros es: " suma
	Imprimir "La resta de los numeros es: " resta
	Imprimir "La multiplicación de los numeros es: " multi
	Si num2 <> 0 Entonces
		division = num1 / num2
		Imprimir "La división de los numeros es: " division
	SiNo
		Imprimir "No se puede dividir por 0"
	Fin Si
	
	
FinAlgoritmo
