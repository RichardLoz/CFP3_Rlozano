#5-	El Ministerio de Salud les pide que realicen un algoritmo que pueda clasificar temperaturas en tres categorías: "Baja", "Media" y "Alta". Tu tarea es desarrollar un programa que solicite al usuario ingresar temperaturas y las clasifique según los siguientes criterios:

#Baja: Temperaturas menores o iguales a 10 grados Celsius.
#Media: Temperaturas mayores a 10 grados y menores o iguales a 25 grados Celsius.
#Alta: Temperaturas mayores a 25 grados Celsius.

#Además, se desea que el programa almacene las temperaturas en listas separadas para cada categoría.
#Al finalizar imprimir por pantalla las temperaturas correspondientes a cada categoría. 

Baja = []
Media = []
Alta = []

temperate = float(input("Ingrese la temperatura: "))

for i in range(temperate):
    if i <= 10:
        Baja.append(i)

    if i > 10 and i <= 25:
        Media. append(i)

    if i > 25:
        Alta. append(i)



print(f("Segun lo evaluado, las temperaturas bajas son: {Baja}, las medias son: {Medias} y las altas son: {Alta}"))

    
    
    
    