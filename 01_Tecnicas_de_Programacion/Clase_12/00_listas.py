
#TODO: Listas: Se describe como una lista de items separados por coma "," y contenido entre corchete "[]". Es una lista heterogenea es decir puede contener: numeros, variables, string o incluso otras listas. Las listas son mutables

#Lista
# nombre = "Roberto"
# datos = [1, -4, 124.2, "Marvel", "Nuñez", True, nombre] 
# print(datos)
# print(type(datos))

# lenguajes = ["Python", "Java", "C++", "JavaScript", 3, -4, [1,2,3], False]
# print(lenguajes)
# print(lenguajes[6])
# print(lenguajes[6][2]) #accediento al subindice de la sublista

# pares = [2,4,6,8]
# impares = [1,3,5,7,9]
# #Imprimo por pantalla
# print(pares + impares)
# print(f"{pares} {impares}")

#TODO: A diferencia de los STRING, las listas son MUTABLES
# juegos = ["Lol", "Fifa", "Valorant"]
# print(juegos)
# print(juegos[0])
# juegos[0] = "Mario Bross"
# print(juegos)

#TODO: Asignacion por SLICING
# numeros = [1, 2, 3, "cuatro", "cinco", "seis"]
# print(numeros)
# # ["uno", "dos", "tres", "cuatro", "cinco", "seis"]
# numeros[3:6:1] = [4, 5, 6]
# print(numeros)

# letras = ["a", "b" , "c", "D", "E", "F"]
# # ["A", "B", "C", "D", "E", "F"]

#TODO: Borrar por slicing
# letras = ["a", "b", "c", "d", "e", "f"]
# #["d", "e", "f"]
# print(letras)
# # letras[0:3:1] = []
# letras[0:3:1] = []
# print(letras)


#TODO: Funcion APPEND() ==> Agregar un elemento al final de una lista
# juegos = ["Mario Bross", "COD", "NBA2K"]
# print(juegos)
# print(type(juegos))
# juegos.append("Batlefield")
# print(juegos)
# juegos.append(3*2)
# print(juegos)

#TODO: POP() ==> Eliminar el ultimo elemento de una lista
# juegos = ["Mario Bross", "COD", "NBA2K", "Ramon"]
# print(juegos)
# juegos.pop(1)
# print(juegos)


#TODO: COUNT() ==> Cuenta el numero de veces que un item se repite en la lista
# numeros = [1,2,1,4,2,1,4,7,12,11,1,2,1,1]
# print(f"La cantidad de veces que se repite el numero 1 es : {numeros.count(1)}")
# print(numeros.count(2))

#TODO: INDEX() ==> Buscar un elemento que le indiquemos y nos devuelve en que posición se encuentra
# numeros = [1,22,42,4,21,12,42,7,12,11,11,2]
# print(f"La posición donde se encuentra el numero 42 es: {numeros.index(42)} ")

#TODO: SOlucion DESAFIO LISTAS
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]


#1- Añade a la LISTA1 el int 1234 y luego el string “Hola”
#2- Añade a la LISTA2 el string “Adios” y luego el int 1234
#3- Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
#4- Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
#5- Genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

#1- 
# lista1.append(1234)
# lista1.append("Hola")
# print(f"El valor actualizado de Lista1 es {lista1}")

# #2- 
# lista2.append("Adios")
# lista2.append(1234)
# print(f"El valor actualizado de Lista2 es  {lista2}")

# #3-
# lista1.pop()
# lista3 = lista1
# print(lista3)

# #4- 
# lista2.pop(0)
# lista2.pop(-1) #Pongo -1 ya que me asegura que siempre es el ultimo elemento
# lista4 = lista2
# print(lista4)

# #5- 
# lista5 = lista3 + lista4
# print(lista5)
