Algoritmo ejerc5_ParcialRecuperatorio
	// 5-	Crea un programa que genere un n�mero aleatorio entre 1 y 30. 
	// Luego, solicita al usuario que adivine el n�mero. 
	// Utiliza una estructura de control Mientras para permitir al usuario hacer intentos hasta que adivine el n�mero correcto. 
	//Muestra el n�mero de intentos necesarios al final.
	
	Definir num  Como Entero
	num = azar(30)
	Imprimir num
	Imprimir " Adivine el numero del rango del 1 al 30:"
	leer numUser
	Mientras num <> numUser Hacer
		Imprimir " Casi, volve a intentar:"
		leer numUser
		intentos = intentos + 1
	Fin Mientras
	
	Imprimir "Adivinaste el numero secreto " num, " en " intentos " intentos "
	

FinAlgoritmo
