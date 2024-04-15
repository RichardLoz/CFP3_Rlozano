# TODO: DICCIONARIOS
# dic_vacio= {}
# print(dic_vacio)
# print(type(dic_vacio))

# profesor = {
#     "nombre":"Richard",
#     "apellido":"Lozano",
#     "edad":18
# }
# print(profesor)

# alumno = {
#     "nombre":"Xavier",
#     "apellido":"Saez",
#     "edad":21,
# }
# alumno["nombre"]="Frutilla"
# print(alumno)
# alumno["nombre"]="Sandia Seca"
# print(alumno)
# # print(alumno["nombre"])
# alumno["nombre"]="Naza"
# print(alumno)
# alumno["edad"] *=3
# print(alumno)
# alumno["sexo"]="M"
# print(alumno)

# TODO: UPDATE
# numeros = {
#     "numero1":1,
#     "numero2":2
#     }
# numeros.update({"numero3":3,"numero4":4})
# print(numeros)
# numeros.update()
# print(len(numeros))

# alumno = {
#     "nombre":"Xavier",
#     "apellido":"Saez",
#     "edad":21,
#     "hobbies":["Cantar","Bailar","Comer"]
# }
# print(alumno)
# print(len(alumno))
# print(len(alumno["hobbies"][0]))
# print(type(alumno["hobbies"][0]))

# del alumno["edad"]
# print(alumno)



# TODO: IN
# numeros = {
#     "numero1":1,
#     "numero2":2,
#     "pares":[2,4,5]
#     }
# print("numero1" in numeros)
# numeros.clear()
# numeros = {}
# print(numeros)

# TODO: POP
# numeros = {
#     "numero1":1,
#     "numero2":2,
#     "pares":[2,4,5]
#     }

# numeros_borrados = numeros.pop("numero1")
# print(numeros)
# print(numeros_borrados)

# # TODO: DESAFIO SET
# grupo = {"Miguel","Blanca","Mario","Andres"}
# print(grupo)
# grupo.update({"Ana","Ramon","Marta","Eric","David"})
# print(grupo)

# for nombre in ["Mario","Miguel","Esteban"]:
#     grupo.discard(nombre)
# print(grupo)

# TODO: RECORRER DICCIONARIOS

# club= {
#     "nombre":"River Plate",
#     "barrio":"Nuñez",
#     "dt":"Gallardo",
#     "arquero":"Armani"
# }
# print(club)

# for clave in club.keys():
#     print(clave)

# for valor in club.values():
#     print(valor)
# for todoJunto in club.items():
#     print(todoJunto)
