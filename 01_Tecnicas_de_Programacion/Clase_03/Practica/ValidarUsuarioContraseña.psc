Algoritmo ValidarUsuarioContraseña
	//Declaro usuario y contraseña almacedos
	nombreGuardado = "Franco"
	contraGuardada = 12345
	// Solicitar usuario y contraseña al usuario
	Imprimir "Ingrese su usuario: "
	leer nombreIngresado
	Imprimir "Ingrese su contraseña: "
	leer contraIngresada
	
	//Evaluar la condicion
	Si nombreGuardado == nombreIngresado & contraGuardada == contraIngresada Entonces
		Imprimir "Bienvenido " nombreIngresado
	SiNo
		Imprimir "Usuario no encontrado"
	Fin Si
FinAlgoritmo
