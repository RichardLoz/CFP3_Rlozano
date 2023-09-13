Algoritmo ValidaciónUsuario
	Definir userDB Como Caracter
	Definir passDB Como Entero
	userDB = "Richard"
	passDB = 12345
	Repetir
		Imprimir "Bienvenidos al sistema de login del CFP3"
		Imprimir "Ingrese su usuario: "
		leer user
		Imprimir "Ingrese su contraseña: "
		leer pass
	Hasta Que (user == userDB) & (pass == passDB)
		Imprimir "Bienvenido: " , user
	
FinAlgoritmo
