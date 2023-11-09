
#TODO: COMPREHENSION 

#TODO: Insertar en una lista los numeros pares del 1 al 10

# Solucion 1
lista = []
lista.append(0)
lista.append(2)
lista.append(4)
lista.append(6)
lista.append(8)
lista.append(10)
print(lista)

# Solucion 2
lista_2 = []
for i in range(0,11,2):
    lista_2.append(i)

print(lista_2)

# Solucion 3
lista_3 = []
for i in range(11):
    if (i % 2 == 0):
        lista_3.append(i)
print(lista_3)

# Solucion 4 ==> List Comprehension
#Sintaxis ==> [expresion for elemento in secuencia if condicion]
lista_4 = [i for i in range(11) if i % 2 == 0]
print(lista_4)


# Solucion 5 ==> Set comprehension
lista_5 = {i for i in range(11) if i % 2 == 0}
print(lista_5)


