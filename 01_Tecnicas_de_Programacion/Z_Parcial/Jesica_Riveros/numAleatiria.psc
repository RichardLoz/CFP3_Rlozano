Algoritmo numAleatiria
	//Crea un programa que genere un n�mero aleatorio entre 1 y 30. 
	//Luego, solicita al usuario que adivine el n�mero. 
	//Utiliza una estructura de control Mientras para permitir al usuario hacer intentos hasta que adivine el n�mero correcto. 
	//Muestra el n�mero de intentos necesarios al final.
	Definir num,aletario,intentos Como Entero
	num=0
	aletario=0
	intentos=0
	num= azar(30) //numero al azar entre 1 y 30
	Imprimir " ingrese un numero: "
	Leer num
	Mientras num>aletario 
		Imprimir num=num+1
		Leer num
	Fin Mientras
	Escribir "necesitaste: " intentos , " intentos: " 
	
FinAlgoritmo
