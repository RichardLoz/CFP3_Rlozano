Algoritmo ValidarUsuarioContrase�a
	//Declaro usuario y contrase�a almacedos
	nombreGuardado = "Franco"
	contraGuardada = 12345
	// Solicitar usuario y contrase�a al usuario
	Imprimir "Ingrese su usuario: "
	leer nombreIngresado
	Imprimir "Ingrese su contrase�a: "
	leer contraIngresada
	
	//Evaluar la condicion
	Si nombreGuardado == nombreIngresado & contraGuardada == contraIngresada Entonces
		Imprimir "Bienvenido " nombreIngresado
	SiNo
		Imprimir "Usuario no encontrado"
	Fin Si
FinAlgoritmo
