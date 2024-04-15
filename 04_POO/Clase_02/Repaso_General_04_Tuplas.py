
#TODO: TUPLAS: Coleccion de datos parecida a las listas, con la diferencia de que las TUPLAS son INMUTABLES. Se utilizan para asegurarnos que una colección de datos no se pueda modificar. Se declaran entre PARENTESIS

# numeros = (2,5,6,1,True,2.6)
# print(numeros)
# print(type(numeros))

# Tupla con un unico valor
# pares = (2,)
# print(pares) 
# print(type(pares))

# tupla_vacia = ()
# print(tupla_vacia)
# print(type(tupla_vacia))
# nombre = "Nestor"
# tupla_mixta = (1,-4,2.5,False,"Leo",nombre)
# print(tupla_mixta)

# Al igual que las listas, en las tuplas funcionan exactamente igual los indices y slicing
# lenguajes = ("Python","C","Java","Go","C++")
# print(lenguajes[2])
# print(lenguajes[-2])
# print(lenguajes[2:])

# Al igual que las listas, las tuplas se pueden concatenar
# lenguajes = ("C","Visual","C","Python","C","Java","Go","C++")
# print(lenguajes +("Python",))
# numeros = (2,5,1)
# print(lenguajes + numeros)

# Las TUPLAS son INMUTABLES ==> Esto quiere decir que no puedo modificar sus valor por el indice
# provincias = ("San Juan", "Cordoba", "Salta")
# provincias[1] = "Tucuman"
# print(provincias)

# Borrar valores de una tupla
# letras = ("a", "b", "c", "d", "e", "f")
# letras = ()
# print(letras)

# Len en TUPLAS
# lenguajes = ("Python","C","Java","Go","C++","Carbon")
# print(len(lenguajes))


# COUNT en TUPLAS
# lenguajes = ("Python","C","Java","Go","C++","Python")
# print(lenguajes.count("Python"))


# Index en TUPLAS
# lenguajes = ("Python","C","Java","Go","C++","Python")
# print(lenguajes)
# print(lenguajes.index("Java"))


# En PYTHON podemos anidar una lista con una tupla
# tupla = ("Visual","C","Python",
#              "Java","Go",[1,2,4,"Hola"],
#              "C++")
# print(tupla)
# print(type(tupla))

# lista = [2,3,2.5,False,("Hola","Coraje",2),["Leona"]]
# print(lista)
# #print(type(lista))
# print(type(lista[2]))


# Como acceder a los datos anidados
# a = (1,2,3)
# b = (4,5,6)
# c = (8,19,11)

# total = (a,b,c)
# print(total)
# print(total[0])
# print(total[0][0])
# print(type(total[0][0]))


# Transformar colecciones

#Tuplas a listas
# numeros =  (1,2,3,4)
# print(type(numeros))
# list_num=list(numeros)
# print(type(list_num))

# # Listas a TUPLAS
# series= ["Superman","Evangelion","ALF"]
# print(type(series))
# tuple_series = tuple(series)
# print(type(tuple_series))

#TODO: EJERCICIOS: A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:
#1-El último ítem de tupla
#2-El número de ítems de tupla
#3-La posición donde se encuentra el ítem 87 de tupla
#4-Una lista con los últimos tres ítems de tupla
#5-Un ítem que haya en la posición 8 de tupla
#6-El número de veces que el ítem 7 aparece en tupla

#tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
