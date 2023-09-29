Algoritmo ejercicio3
	Definir numArrgelo Como Entero
	
	Imprimir "ingrese la dimension del arreglo: "
	leer dimArreglo
	
	Dimension numArrgelo[dimArreglo]
	
	Para i = 0 Hasta dimArreglo - 1 Con Paso 1 Hacer
		Imprimir "ingresar numeros para el arreglo: "
		leer numArrgelo[i]
	Fin Para
	

	Para i = 0 Hasta dimArreglo - 1 Con Paso 1 Hacer
		Si numArrgelo[i] % 2 = 0 Entonces
			 
			contador = contador + numArrgelo[i]
		Fin Si
	Fin Para
Imprimir contador
FinAlgoritmo
