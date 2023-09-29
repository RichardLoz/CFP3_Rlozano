Algoritmo ejercicio_2
	//declarfion de variables
	definir numeroAdivinar,intento, numeroUsuario Como Entero
	numeroAdivinar <- Aleatorio(1,20)
	Mientras numeroUsuario <> numeroAdivinar Hacer
		//solicita al usuario que ingrese su intento
		Escribir "intenta adivinar el numero (entre 1 y 20): "
		leer numeroUsuario
		intento <- intento + 1
		si numeroUsuario < numeroAdivinar Entonces
			escribir "el numero es mayor: "
		SiNo
			si numeroUsuario > numeroAdivinar Entonces
				Escribir "el numero es menor: "
			FinSi
		FinSi
		
	Fin Mientras
	// mostrar el numero de intentos necesarios 
	Escribir "felicidades adivinastes el numero en ", intentos, "intentos."

FinAlgoritmo
