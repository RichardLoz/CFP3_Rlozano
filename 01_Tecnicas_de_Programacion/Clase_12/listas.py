
#TODO: Listas: Se describe como una lista de items separados por coma "," y contenido entre corchete "[]". Es una lista heterogenea es decir puede contener: numeros, variables, string o incluso otras listas. Las listas son mutables

#Lista
# nombre = "Roberto"
# datos = [1, -4, 124.2, "Marvel", "Nuñez", True, nombre] 
# print(datos)
# print(type(datos))

# lenguajes = ["Python", "Java", "C++", "JavaScript", 3, -4, [1,2,3], False]
# print(lenguajes)
# print(lenguajes[1])
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
juegos = ["Mario Bross", "COD", "NBA2K", "Ramon"]
juegos.pop()
print(juegos)


