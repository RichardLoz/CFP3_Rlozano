Algoritmo ejercicio4
	
	Definir notas, numNota Como Entero
	Definir notaEncontrada como logico
	notaEncontrada = Falso
	Dimension notas[6]
	
	Para i = 0 Hasta 6 - 1 Con Paso 1 Hacer
		Imprimir "ingrese las notas: "
		leer notas[i]
		
	Fin Para
	
	
	Para i = 0 Hasta 6 - 1 Con Paso 1 Hacer
		Imprimir notas[i]
	Fin Para
	
	
	Imprimir "ingrese una nota: "
	leer numNota
	
	Para i = 0 Hasta 6 - 1 Con Paso 1 Hacer
		Si notas[i] == numNota Entonces
			notaEncontrada = verdadero
		Fin Si
	Fin Para
	
	Si notaEncontrada == Verdadero Entonces
		Imprimir "su nota esta "
	SiNo
		Imprimir "su nota no esta "
	Fin Si

FinAlgoritmo
