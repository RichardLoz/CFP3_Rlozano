Algoritmo ejercicio_1
	definir edad Como Entero
	EDAD_MAYORIA = 18
	Imprimir "ingrese su edad: "
	leer edad
	Si  edad = EDAD_MAYORIA Entonces
		Imprimir "usted tiene 18 a�os"
	SiNo
		Si edad > EDAD_MAYORIA Entonces
			Imprimir "usted es mayor de 18 a�os"
		SiNo
			Imprimir "usted es menor de edad"
		Fin Si
	Fin Si
FinAlgoritmo
