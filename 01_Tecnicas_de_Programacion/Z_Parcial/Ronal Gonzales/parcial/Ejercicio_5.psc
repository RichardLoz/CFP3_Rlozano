Algoritmo Ejercicio_5
	Definir edades, numBusca Como Entero
	Definir busca como logico
	Imprimir "¿Cuantas edades desea ingresar?"
	Leer numEdades
	Dimension edades[numEdades]
	Para i = 0 Hasta numEdades-1 Con Paso 1 Hacer
		Imprimir "Ingrese una edad: "
		leer edades[i]
	Fin Para
	Imprimir "Gracias por ingresar los datos"
	busca = Falso
	Imprimir "ingrese un numero para buscar"
	leer numBusca
	i = 0
	Mientras i <= numEdades-1 Hacer
		Si edades[i] = numBusca Entonces
			busca = Verdadero
		Fin Si
		i = i+1
	Fin Mientras
	Si busca Entonces
		Imprimir "Se encuentra en los datos"
	SiNo
		Imprimir "No se encuentra en los datos"
	Fin Si
FinAlgoritmo
