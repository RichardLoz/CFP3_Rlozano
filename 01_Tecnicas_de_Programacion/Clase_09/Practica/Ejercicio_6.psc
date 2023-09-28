Algoritmo Ejercicio_6
	definir i , f, ff, vector, temp Como Entero
	Dimension  vector[10]
	temp = 0
	f = 0
	ff = 0
	Para i = 0 Hasta 10 - 1 con paso 1 Hacer
		Imprimir "Ingrese el numero ", i + 1, " : "
		leer vector[i]
		Para f = 0 hasta i con paso 1 Hacer
			Para ff = f Hasta i Con Paso 1 Hacer
				Si vector[f]  > vector[ff] Entonces
					temp = vector[f]
					vector[f] = vector[ff]
					vector[ff] = temp				
				Fin Si
			Fin Para
		Fin Para
	Fin Para
	// Imprimo mi lista ordenada
	Para i = 0 Hasta 10 -1 Con Paso 1 Hacer
		Imprimir Sin Saltar " " vector[i]
	Fin Para
FinAlgoritmo
