Algoritmo calificacionesAlumno
	definir calificaciones Como Entero
	
	Imprimir "Cuantas notas desea ingresar: "
	leer valor
	
	Dimension calificaciones[valor]
	
	Para i = 0 Hasta valor - 1 Con Paso 1 Hacer
		Imprimir "Ingrese las notas del alumno: "
		leer calificaciones[i]
		sumaNotas = sumanotas + calificaciones[i]
		promedio = sumanotas / valor
	Fin Para
	Imprimir "El promedio del alumno es: " promedio
	
FinAlgoritmo
