
#TODO: Listas:
# Insert
# lista_cursos = ["Go", "Java", "C#", "Ruby"]
# print(lista_cursos)
# lista_cursos.insert(2,"Javascript")
# print(lista_cursos)

#Extend
# nuevos_cursos = ["Visual Basic", "Cobol"]
# lista_cursos.extend(nuevos_cursos)
# print(lista_cursos)

# Remove
# lista_cursos = ["Go", "Java", "C#", "Ruby"]
# lista_cursos.remove("Go")
# print(lista_cursos)

#Del
#lista_cursos = ["Go", "Java", "C#", "Ruby"]
# del lista_cursos[-1]
# print(lista_cursos)

# Clear
# lista_cursos.clear()
# print(lista_cursos)


#TODO:=========================================
# Metodos
lista = [9,19,2,1,0,299,400,7]

#Sort()
# lista = sorted(lista)
# lista.sort()
# print(lista)

# Descendente
# lista.sort(reverse=True)
# print(lista)

# para pensar: Quiero saber el numero mayor y el numero menor de la lista
# Opcion_1
# lista = [9,19,2,1,0,299,400,7]
# lista.sort()
# print(lista)
# print(lista[0])
# print(lista[-1])

# Opcion_2
# lista = [9,19,2,1,0,299,400,7]
# print(min(lista))
# print(max(lista))

#TODO: DESEMPAQUETADO
numeros = (1,2,3,4,5,6,7)
# uno = numeros[0]
# dos = numeros[1]
# tres = numeros[2]
# cuatro = numeros[3]

# print(uno)
# print(dos)
# print(tres)
# print(cuatro)

numeros = (1,2,3,4,5,6,7)
# uno, dos, tres, *resto = numeros

# print(uno)
# print(dos)
# print(tres)
# print(resto)

# Que pasa si quiero omitir los valores que se encuentran despues del indice 4 pero si quiero tener en cuenta los ultimos elementos

# numeros = (1,2,3,4,5,6,7,8,9,10,"H")

# uno, dos, tres, cuatro, *_, nueve, diez, once = numeros
# print(uno)
# print(dos)
# print(tres)
# print(cuatro)
# print(nueve)
# print(diez)
# print(once)

# *_ ==>  Omitir valores