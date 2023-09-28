Algoritmo ejercicios_2
	// 2- Crear un algoritmo para hallar el mayor de 3 numeros 
	//ingresados por teclado.
	imprimir " ingrese 3 numeros "
	LEER num1,num2,num3
	Si num1>num2 &num1>num3 Entonces
		imprimir " el numero mayor es " num1
	SiNo
		si	num2>num3 y num2>num1 Entonces
			imprimir" el numero mayor es " num2
		SiNo
			imprimir " el numero mayor es " num3
		FinSi
			
	Fin Si
FinAlgoritmo
