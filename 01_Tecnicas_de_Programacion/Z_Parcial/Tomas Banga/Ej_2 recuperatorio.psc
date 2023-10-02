Algoritmo Ej_2
	Definir num Como Entero
	
	Imprimir "Ingrese un número positivo"
	leer num
	
	Para i = 1 Hasta num Con Paso 1 Hacer
		Si i % 2 = 0 Entonces
			suma = suma + i
		Fin Si
	Fin Para
	
	Imprimir "La suma de todos los números impares es " suma
	
FinAlgoritmo
