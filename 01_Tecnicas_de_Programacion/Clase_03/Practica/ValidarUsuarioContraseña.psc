Algoritmo ValidarUsuarioContraseņa
	//Declaro usuario y contraseņa almacedos
	nombreGuardado = "Franco"
	contraGuardada = 12345
	// Solicitar usuario y contraseņa al usuario
	Imprimir "Ingrese su usuario: "
	leer nombreIngresado
	Imprimir "Ingrese su contraseņa: "
	leer contraIngresada
	
	//Evaluar la condicion
	Si nombreGuardado == nombreIngresado & contraGuardada == contraIngresada Entonces
		Imprimir "Bienvenido " nombreIngresado
	SiNo
		Imprimir "Usuario no encontrado"
	Fin Si
FinAlgoritmo
