# 4-	Un parque temático está organizando un evento especial y te ha pedido que desarrolles un programa que clasifique las entradas en tres categorías: "Aventura", "Familiar" y "General". La clasificación se realizará según los siguientes criterios:

# Aventura: Entradas con el código verificador terminado en "X" y un precio mayor a $50.000.  (ERTJHX)
# Familiar: Entradas con el código verificador terminado en "Y" y un precio entre $20.000 y $50.000, inclusive. (QUPHNY)
# General: Entradas que no cumplen ninguno de los criterios anteriores.

# Tu programa debe solicitar al usuario ingresar el código verificador y el precio de la entrada, y luego determinar a qué categoría pertenece.


""" codigo_ver = input("ingrese el codigo: ").lower()
precio_entrada = int(input("ingrese el precio: "))


if codigo_ver[-1] == "x" and precio_entrada >= 50000:
    print("La entrada ingresada es de categoría 'Aventura' ")
elif codigo_ver[-1] == "y" and precio_entrada > 20000:
    print("La entrada ingresada es de categoría: 'Familiar")
else:
    print("La entrada ingresada es de categoría: 'General' ") """


# 5-	El Ministerio de Salud les pide que realicen un algoritmo que pueda clasificar temperaturas en tres categorías: "Baja", "Media" y "Alta". Tu tarea es desarrollar un programa que solicite al usuario ingresar temperaturas y las clasifique según los siguientes criterios:

# Baja: Temperaturas menores o iguales a 10 grados Celsius.
# Media: Temperaturas mayores a 10 grados y menores o iguales a 25 grados Celsius.
# Alta: Temperaturas mayores a 25 grados Celsius.

# Además, se desea que el programa almacene las temperaturas en listas separadas para cada categoría.
# Al finalizar imprimir por pantalla las temperaturas correspondientes a cada categoría. 

temp_baja=[]
temp_media=[]
temp_alta=[]
temp=[]
temperatura= 1
while temperatura != 0:
    temperatura = int(input("ingrese temperatura actual, (0 para continuar)"))
    temp.append(temperatura)

print(temp)
for i in temp:
    if i <= 10:
        temp_baja.append(i)
    if i >= 10 and i <= 25:
        temp_media.append(i)
    if i > 25:
        temp_alta.append(i)
        
print(f"temperaturas bajas {temp_baja}")
print(f"temperaturas medias {temp_media}")
print(f"temperaturas altas {temp_alta}")