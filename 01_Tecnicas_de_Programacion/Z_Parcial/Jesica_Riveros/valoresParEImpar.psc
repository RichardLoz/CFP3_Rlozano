Algoritmo valoresParEImpar
	//Crea un programa que solicite al usuario ingresar un número entero positivo. 
	//Utiliza un ciclo Para para sumar todos los números impares desde 1 hasta el número ingresado y muestra el resultado
	Definir num Como Entero
	Imprimir " ingrese un numero positivo: " 
	Leer num
	Para i=1 Hasta num-1 Con Paso 1 Hacer
		num=num+i
		Imprimir " la suma de los numeros ingresado es: " num
	Fin Para
	Para i=1 Hasta num-1 Con Paso 1 Hacer
		Imprimir i
	Fin Para
	Imprimir " el resultado es: " num
	
	
FinAlgoritmo
