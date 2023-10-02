Algoritmo Ejercicio_4
	Definir arregloNombres Como Cadena
	Escribir '¿Cuantos nombres desea ingresar? '
	Leer numeroArreglos
	Dimension arregloNombres[numeroArreglos] // Solo modifique el "Dimensionar" por "Dimension"
	Para i<-0 Hasta numeroArreglos-1 Con Paso 1 Hacer
		Escribir 'Ingrese los nombres'
		Leer arregloNombres[i]
	FinPara
	Para i=numeroArreglos-1 Hasta 0 Con Paso -1 Hacer
		Imprimir Sin Saltar arregloNombres[i] ", "
	Fin Para
FinAlgoritmo
