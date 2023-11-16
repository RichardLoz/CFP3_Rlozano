
# #TODO: COPY()
# set_1 = {1,2,3,4,5}
# set_2 = set_1.copy()
# print(set_1)
# print(set_2)

# #TODO: isdisjoint
# set_3 = {2,3,4}
# set_4 = {1,5,6}
# print(set_3.isdisjoint(set_4))

# #TODO: ISSUBSET()
# set_5 = {5,6}
# set_6 = {4,5,6,7}
# print(set_5.issubset(set_6))

# #TODO: ISSUPERSET() ==>
# set_7 = {1,2,3,4}
# set_8 = {1,2,4}
# print(set_7.issuperset(set_8))

# #TODO: UNION
# set_9 = {1,2,3,1.2}
# set_10 = {2,3,4,5,6,1.2}
# print(set_9.union(set_10))

# #TODO: DIFFERENCE
# set_11 = {1,2,3,4,5}
# set_12 = {2,3,4,5,6,7}
# print(set_11.difference(set_12))

# #TODO: DIFFERENCE UPDATE
# set_13 = {1,2,3,4,5}  #{1}
# set_14 = {2,3,4,5,6,7}
# print(set_13)
# set_13.difference_update(set_14)
# print(set_13)

# #TODO:: INTERSECTION
# set_15 = {1,2,3,4,5}
# set_16 = {2,3,4,5,6,7}
# print(set_15.intersection(set_16))

# #TODO: INTERSECTION UPDATE
# set_17 = {1,2,3,4,5,7}
# set_18 = {2,3,4,5,6,7}
# print(set_17)
# set_17.intersection_update(set_18)
# print(set_17)

#TODO: EJERCICIO:
#Crea un conjunto 'numeros' con elementos de tipo entero. Luego recorrerlo con un ciclo FOR para imprimir cada elemento elevado al cuadrado

import random
numeros = set(random.randint(1,30) for _ in range(10))
print(numeros)
lista_cuadrada = []

for i in numeros:
    print(i**2)
    lista_cuadrada.append(i)
print("Lista cuadrados", lista_cuadrada)

