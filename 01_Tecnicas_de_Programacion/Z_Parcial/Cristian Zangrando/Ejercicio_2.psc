Algoritmo Ejercicio_2
	Definir num Como Entero
    Imprimir "intente adivinar un numero entre 1-20: "
	num=azar(20)
	contar=0
	Mientras num <> number Hacer
		Imprimir "ingrese un numero: "
		Leer number
		contar = contar + 1
	 FinMientras
	 Imprimir "correcto,usted adivino el numero " num // sume esta linea para poder mostrar al usuario el numero que adivino
	 Imprimir "usted intento " contar " veces "
	FinAlgoritmo