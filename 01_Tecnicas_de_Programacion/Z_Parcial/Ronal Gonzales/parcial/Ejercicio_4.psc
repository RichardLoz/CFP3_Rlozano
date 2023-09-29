Algoritmo Ejercicio_4
	Definir arregloNombres Como caracter
	//pedir al usuario la cantidad de nombres que decea ingresar
	Escribir '¿Cuantos nombres va ingresar?: '
	Leer numeroArreglos
	
	Dimension arregloNombres[numeroArreglos]
	Para i <-0 Hasta numeroArreglos -1 Con Paso 1 Hacer
		Escribir 'Ingrese los nombres'
		Leer arregloNombres[i]
	FinPara
	Para i=numeroArreglos-1 Hasta 0 Con Paso -1 Hacer
		Imprimir Sin Saltar arregloNombres[i] ", "
	Fin Para
	Escribir "estos son los nombres de forma inversa. "
	
FinAlgoritmo

