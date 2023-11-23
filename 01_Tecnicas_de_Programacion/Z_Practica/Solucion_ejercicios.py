# 1-	Crea dos variables, num1 y num2, e imprime la suma, resta, multiplicación y división de ambas.
# num1= int(input("Ingrese un numero: "))
# num2= int(input("Ingrese un numero: "))
# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2
# print(suma)
# print(resta)
# print(multiplicacion)
# print(round(division,2))

# 2-	Solicita al usuario que ingrese un número. Luego, verifica si es positivo, negativo o cero e imprime un mensaje correspondiente.
# num = int(input("Ingrese un numero: "))
# if num > 0:
#     print("El numero es positivo")
# elif num < 0:
#     print("El numero es negativo")
# else:
#     print("El numero es igual a 0")

# 3-	Utiliza un bucle while para imprimir los números del 1 al 10.
# num = 1
# while num <= 10:
#     print(num)
#     num += 1
# 4-	Dada la siguiente lista lista_num = [1,3,4,2,1,5,8,7,9,2,3,4,3,6], Calcular la suma y el promedio de sus elementos.
# lista_num = [1,3,4,2,1,5,8,7,9,2,3,4,3,6]
# suma_lista = 0


# for i in lista_num:
#     suma_lista += i
# print(f"La suma total de los numeros en la lista es {suma_lista}")
# promedio_lista = suma_lista / len(lista_num)
# print(f"El promedio de los numeros en la lista es {promedio_lista}")

# 5-	Teniendo en cuenta la lista anterior eliminar los elementos duplicados y mostrar la lista final. (Para este ejercicio se pide no usar funciones propias de listas)
# lista_num = [1,3,4,2,1,5,8,7,9,2,3,4,3,6]
# lista_sin_duplicados = []
# for i in lista_num:
#     if i not in lista_sin_duplicados:
#         lista_sin_duplicados.append(i)
# print(f"La lista sin elementos duplicados es: {lista_sin_duplicados}")
# 6-	Crea una tupla de nombres y utiliza un bucle for para imprimir cada nombre.
# nombres = ("Tania", "Daivis", "Roberto", "Milagros", "Jesica", "Bryan")
# for i in nombres:
#     print(i)
# 7-	Crea dos conjuntos y encuentra la unión, la intersección y la diferencia simétrica entre ellos.
# Crear dos conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

# Encontrar la unión
union = conjunto1.union(conjunto2)
print("Unión:", union)

# Encontrar la intersección
interseccion = conjunto1.intersection(conjunto2)
print("Intersección:", interseccion)

# Encontrar la diferencia simétrica
dif_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica:", dif_simetrica)
# 8-	Crea un diccionario de productos y sus precios. Luego imprimir por pantalla la lista de productos, luego imprimir los precios y por ultimo imprimir producto y precio.

productos = {
    "Azucar": 10.99,
    "Manteca": 24.95,
    "Detergente": 5.49,
    "Fernet": 14.75
}

# Imprimir la lista de productos
print("Lista de productos:")
for producto in productos.keys():
    print(producto)

# Imprimir la lista de precios
print("\nLista de precios:")
for precio in productos.values():
    print(precio)

# Imprimir producto y precio
print("\nProducto y precio:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")

# 9-	Toma una lista y utilice un bucle while para invertir el orden de los elementos. (No utilices funciones como reverse)
# Lista original
mi_lista = [1, 2, 3, 4, 5]

# Longitud de la lista
longitud = len(mi_lista)

# Índices para recorrer la lista
inicio = 0
fin = longitud - 1


while inicio < fin:
    # Intercambiar elementos en los índices inicio y fin
    mi_lista[inicio], mi_lista[fin] = mi_lista[fin], mi_lista[inicio]

    # Mover los índices hacia el centro de la lista
    inicio += 1
    fin -= 1

# Imprimir la lista invertida
print("Lista invertida usando while:", mi_lista)

# 10-	Solicita al usuario ingresar una frase y utiliza un bucle for con una estructura if para contar cuántas vocales contiene.
# Solicitar al usuario ingresar una frase
frase = input("Ingrese una frase: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Bucle for para contar vocales en la frase
for caracter in frase:
    # Verificar si el caracter es una vocal
    if caracter.lower() in "aeiou":
        contador_vocales += 1

# Imprimir el resultado
print(f"La frase tiene {contador_vocales} vocal(es).")
