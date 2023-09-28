Algoritmo Ejercicio_5
	// 5-	Crear un algoritmo que imprima por pantalla 
	//la multiplicación de los numeros pares e impares del rango del 1 al 10
	definir num, multiPares, multiImpares Como Entero
	multiPares = 1
	multiImpares = 1
	Para num = 1 Hasta 10 Con Paso 1 Hacer
		Si num % 2 == 0 Entonces
			//Imprimir "Multiplicacion de : ", multiPares " * " num
			multiPares = multiPares * num
			//Imprimir "Multiplicacion parcial de ", multiPares
		SiNo
			//Imprimir "Multiplicacion de : " multiImpares, " * " , num
			multiImpares = multiImpares * num
			//Imprimir "Multi parcial Impares: " , multiImpares
		Fin Si
	Fin Para
	Imprimir "La multiplicacion de los numeros pares es: " multiPares
	Imprimir "La multiplicacion de los numeros impares es: " multiImpares
FinAlgoritmo
