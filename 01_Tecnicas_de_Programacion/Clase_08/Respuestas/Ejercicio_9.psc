Algoritmo Ejercicio_9
	Definir numeroBuscado Como Entero
	Definir encontrado Como Logico

	encontrado = Falso
	Dimension arreglo[10]
	
	Para i = 0 Hasta 10-1 con Paso 1 hacer
		arreglo[i] = Azar(100)
		Imprimir arreglo[i]
	FinPara
	
	Escribir "Ingrese un número para buscar en el arreglo: "
	Leer numeroBuscado
	
	i = 0
	Mientras i <= 9 Hacer
		Si arreglo[i] = numeroBuscado Entonces
			encontrado = Verdadero
		FinSi
		i = i +1
	FinMientras
	
	Si encontrado Entonces
		Escribir "El número ", numeroBuscado, " existe en el arreglo."
	Sino
		Escribir "El número ", numeroBuscado, " no existe en el arreglo."
	FinSi
FinAlgoritmo
