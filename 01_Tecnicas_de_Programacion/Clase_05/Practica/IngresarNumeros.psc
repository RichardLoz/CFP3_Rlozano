Algoritmo IngresarNumeros
	definir totalAcumulado Como Entero
	Repetir
		Imprimir "Ingresar un numero: "
		leer num
		Imprimir "Desea agregar otro numero?: si/no"
		leer respuesta
		totalAcumulado = totalAcumulado + num
		
	Hasta Que respuesta <> "si"
		Imprimir "El valor acumulado es: ", totalAcumulado
	
FinAlgoritmo
