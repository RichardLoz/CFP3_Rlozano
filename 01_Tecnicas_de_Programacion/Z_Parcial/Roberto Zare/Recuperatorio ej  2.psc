Algoritmo ejercicio2	
	Definir numAleatorio , numAcertijo , intentos como Entero
	numAleatorio = Aleatorio(1,20)
	intentos = 0
	Imprimir numAleatorio
	Mientras numAcertijo <> numAleatorio Hacer
		Imprimir " Adivine un número del 1 al 20: "
		Leer numAcertijo
		intentos = intentos + 1
	Fin Mientras
	Imprimir "Felicidades, usted adivino el numero " numAleatorio " en " intentos " intentos "
FinAlgoritmo
