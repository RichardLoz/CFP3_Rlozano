Algoritmo Ej_5
	Definir num, num2 Como Entero
	
	num = azar(30)
	
	Mientras num2 <> num Hacer
		Imprimir "Ingrese un número del 1 al 30"
		leer num2
		intentos = intentos + 1
	Fin Mientras
	
	Imprimir "Adivinaste el número en " intentos " intentos"
	
FinAlgoritmo
