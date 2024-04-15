
# TODO: INDIXACION DE LAS CADENAS
#animal = "Perro"
# print(animal)
# print(animal[0])
# print(animal[-1])

# TODO: LONGITUD DE STRING
#print(f"La longitud de animal es {len(animal)} ")

# # TODO: SLICING
# # SINTAXIS ==> [inicio:fin:paso]
# fruta = "Durasno"
# print(fruta[0:2:1])
# print(fruta[2:7:1])

# # Puedo cambiarle el valor de un indice a un string?
# #fruta[3] = "z"
# # en Python los string son inmutables, significa que no pueden sustituir sus elementos individualmente
# # Solucion
# fruta = fruta[0:4] + 'z' + fruta[5:]
# print(fruta)

#materia = "Programacyon"
# print(materia)
# print("Programacion")

# # TODO: SOLUCION
# print(f"{materia[0:9:1]}i{materia[10::]}")

# TODO: OPERACIONES CON STR
# name = "L"
# print(name * 4000)

# # TODO: DAR VUELTA UNA CADENA
# frase = "HHola Facundo, como estas?"
# print(len(frase))
# print(frase[25:0:-1])

# # #TODO: SLICING
# # cadena = "Python"
# # print(cadena[2:6:2])

# # #TODO: MODIFICAR VALORES DE UN STRING MEDIANTE SLICING
# # name = "Facuno"
# # name = name[0:5] + "d" + name[5:]  # O -1
# # print(name)

# # #TODO: REORDENACION
# # cadena_1 = "moderno"
# # cadena_2 = "Python"
# # cadena_3 = "es un lenguaje"
# # cadena_4 = "de programacion"

# print("Resultado esperado")
# print("Python es un lenguaje de programacion moderno")
# print(cadena_2 + " " + cadena_3 + " " + cadena_4 + " " + cadena_1)
# print(f"{cadena_2} {cadena_3} {cadena_4} {cadena_1}")

# #TODO: FORMATEAR
# # Tenemos la cadena en el sentido invertido
cadena = "noicamargorP ,5.9 ,otinaluF emsoC"
# # # Damos vuelta la cadena, con el comando que nos indica iterar en el sentido invertido
print(cadena)
cadena_invertida = (cadena[::-1])
print(cadena_invertida) # Vemos que efectivamente se dio vuelta la cadena
frase = "Cosme Fulanito, 9.5, Programacion"
nombre = (frase[0:5:1])
nota = 9.5
materia = "Programacion"
print(nombre)
# print(nota)
# print(materia)
print(f"Mi nombre es {nombre} y me saque un {nota} en la materia {materia}")
# # # TODO: Dividimos los datos en variables
# # # TODO: NOMBRE : De la posicion 0 a las 14 esta Cosme Fulanito
# # nombre = cadena_invertida[0:14] 
# # print(nombre)

# # # TODO: NOTA :
# # nota = cadena_invertida[16:19] 
# # # Lo dejamos como cadena, pero si quieren como float, harian lo siguiente
# # # nota = float(cadena_invertida[15:18]) # Antes casteabamos con el int, ahora es un dato decimal por eso usamos Float
# # print(nota)

# # # TODO: MATERIA
# # cantidad_de_letras = len(cadena_invertida)
# # # Para saber la cantidad de letras ==> print(cantidad_de_letras)
# # materia = cadena_invertida[21:cantidad_de_letras] # Se hizo la magia
# # print(materia)

# # # TODO: Text Final
# # texto_final = "El estudiante " + nombre + " ha sacado un " + nota + " en " + materia
# # print(texto_final)

# # # TODO: OTRA FORMA DE MOSTRAR
# # print(f"El estudiante {nombre} ha sacado un {nota} en {materia}")