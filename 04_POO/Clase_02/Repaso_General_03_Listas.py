
# TODO: LISTAS
# Se describe como una lista de items separados por coma y contenido entre corchetes. Es una lista HETEROGENEA es decir puede contener: Numeros, variables, string o incluso otras listas. Las listan son mutables

# nombre = "Xavier"
# datos = [1,-4,124.2,"Pokemos", "Floresta", nombre, True]
# print(datos)
# print(type(datos))

# lenguajes = ["Python","Java", "C++", "JavaScript", 3, -4,[1,2,3]]
# # # Imprimir mi lista
# print(lenguajes)
# print(len(lenguajes))
# print(lenguajes[6])
# print(lenguajes[-2])

# # Concatenar Listas
# pares = [2,4,6,8,10]
# impares = [1,3,5,7,9]
# # # Muestro por pantalla
# print(pares + impares)
# print(F"{pares}{impares}")

# # Otra manera de concatenar

#juegos = ["lol", "valorant", "fifa"]
# print(juegos)
# print(juegos + ["pes", "mario bross"])

# # A diferencia de los string las listas son mutables
# print(juegos[0])
# print(juegos)
# juegos[0] = "NFS"
# print(juegos)

# # Asignacion por slicing
# numeros = [1,2,3,"cuatro","cinco","seis"]
# print(numeros)
# numeros[3:6] = [4,5,6]
# print(numeros)

# letras = ["a","b","c","d","e","f"]
# letras[:3] = ["A","B","C"]
# print(letras)

#  Borrar valores por Slicing
#letras = ["a","b","c","d","e","f"]
# letras[:3] = []
# print(letras)

# # Borrar toda la lista
# letras = []
# print(letras)

# FUNCIONES: En las listas hay funciones integradas: 

# # APPEND: Permite agregar un nuevo item al final de una lista, tambien podemos realizar operaciones aritmeticas dentro del item.
#juegos = ["lol", "valorant", "fifa"]
# juegos.append("cs")
# print(juegos)

# # Operaciones aritmeticas en APPEND
# juegos.append(4*2)
# print(juegos)

# # Longitud Lista
#print(len(juegos))

# # POP: Elimina el ultimo item de una lista
#juegos.pop()
# juegos = ["lol", "valorant", "fifa"]
# #Especificando un indice
# juegos.pop(0)
# juegos.pop(1)
# print(juegos)

# # Otro ejemplo (lo que va en parentesis el indice)
# numeros = [1,2,1,3,4,1,1]
# numeros.pop(1)
# print(numeros)

# numeros =  [1,2,1,3,4,1]
# numeros.pop(2)
# print(numeros)


# COUNT: Cuenta el numero de veces que un item se repite en una lista
# numeros =  [1,2,1,3,4,1]
# print(numeros.count(1))

# # Index: Busca el item que le indicamos y nos devuelve en que indice se encuentra
# numeros = [1,2,1,3,1,4,1,5]
# print(numeros.index(2))


#TODO: DESAFIO
# Dadas dos listas: Lista1 y Lista2 debes realizar las siguientes tareas:
#1- Añade a la Lista1 el int:1234 y luego el str:"Hola"
#2- Añade a la LISTA2 el string “Adios” y luego el int 1234
#3- Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
#4- Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
#5- Genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

#1-
lista1.append(1234)
lista1.append("Hola")
print(lista1)

#2-
lista2.append("Hola")
lista2.append(1234)
print(lista2)

#3-
lista1.pop()
lista3 = lista1
print(lista3)

#4-
lista2.pop(0)
lista2.pop(-1)
lista4 = lista2
print(lista4)

#5-
lista5 = lista3 + lista4
print(lista5)





#TODO: RESPUESTAS:
#1-
# lista1.append(1234)
# lista1.append("Hola")
# print(lista1)
# #2-
# lista2.append("Adios")
# lista2.append(1234)
# print(lista2)
# #3-
# lista1.pop()
# lista3 = lista1
# print(lista3)
# #4-
# lista2.pop(0)
# lista2.pop(-1)
# lista4 = lista2
# print(lista4)
# #5-
# lista5 = lista4 + lista3
# print(lista5)




