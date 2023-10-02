Algoritmo Ej_4
	Definir notas, nota2 Como Entero
	Definir existe Como Logico
	
	Dimension notas[6]
	Para i = 0 Hasta 6 - 1 Con Paso 1 Hacer
		Imprimir "Ingrese una nota"
		leer notas[i]
	Fin Para
	
	Imprimir "Ingrese la nota que desea buscar"
	leer nota2
	
	existe = Falso
	
	Para i = 0 Hasta 6 - 1 Con Paso 1 Hacer
		Si nota2 = notas[i] Entonces
			existe = Verdadero
		Fin Si
	Fin Para
	
	Si existe = Verdadero Entonces
		Imprimir "La nota existe en el arreglo"
	SiNo
		Imprimir "La nota no existe"
	Fin Si
	
FinAlgoritmo
