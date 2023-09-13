Algoritmo ContadorNumerosPares
	definir num, contador Como Entero
	
	Imprimir "Ingrese un numero entero positivo: "
	leer num
	contador = 1
	
	Imprimir "Numeros pares del 1 hasta ", num, " : "
	
	Mientras contador <= num Hacer
		si contador % 2 = 0 Entonces
			Imprimir contador
		FinSi
		contador = contador + 1
	Fin Mientras
	
FinAlgoritmo
