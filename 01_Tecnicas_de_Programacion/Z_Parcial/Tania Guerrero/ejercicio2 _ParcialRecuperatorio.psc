Algoritmo ejercicio2
	// 2-	Crea un programa que solicite al usuario ingresar un número entero positivo. 
	// Utiliza un ciclo Para para sumar todos los números impares desde 1 hasta el número ingresado y muestra el resultado
	Definir num, suma , contador Como Entero
	imprimir "Ingrese un numero entero positivo:"
	Leer num
	
	Para i = 1 Hasta num - 1 Con Paso 1 Hacer
		Si i % 2 <> 0 Entonces
			suma = suma + i
			
		Fin Si
	Fin Para
	Imprimir " La suma de todos los numeros impares hasta el numero asignado es: " suma
	
FinAlgoritmo
