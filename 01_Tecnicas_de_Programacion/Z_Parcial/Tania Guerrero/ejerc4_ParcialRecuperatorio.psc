Algoritmo ejerc4_ParcialRecuperatorio
	// 4- Declara un arreglo llamado "notas" con capacidad para 6 elementos. 
	// Llena el arreglo con calificaciones (números enteros) ingresadas por el usuario. 
	//A continuación, solicita al usuario ingresar una calificación y verifica si esa calificación se encuentra en el arreglo. 
	//Muestra un mensaje apropiado
	
	Definir notas, notaAvalidar Como Entero
	Definir encontrado Como Logico
	
	Dimension notas[6]
	
	Para i = 0 Hasta 6 - 1 Con Paso 1 Hacer
		Imprimir "Ingrese las calificaciones del arreglo:"
		leer notas[i]
	Fin Para
	
	imprimir "Ingresar una calificacion para validar: "
	leer notaAvalidar
	
	encontrado = Falso
	i = 0
	
	Para i = 0 Hasta 6 - 1 Con Paso 1 Hacer
		Si notaAvalidar = notas[i] Entonces
			encontrado = Verdadero
		Fin Si
	Fin Para
	
	Imprimir encontrado
	Si encontrado = verdadero Entonces
		Imprimir " La nota se encuentra dentro del arreglo"
	SiNo
		Imprimir "La nota no se encuentra en el arreglo"
	Fin Si
	
FinAlgoritmo
