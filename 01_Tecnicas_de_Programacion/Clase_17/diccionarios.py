
#TODO: DICCIONARIOS

#TODO: DIccionario vacio
# dic_vacio = {}
# print(type(dic_vacio))

# alumno = {
#     "nombre": "Ronal",
#     "edad" : 15,
#     "sexo" : "Masculino",
#     "direccion" : "Humberto Primo 2252"
# }
# print(alumno)

#Modificar valores de alumno mediante su clave
# alumno["nombre"]="Daivis"
# alumno["edad"] = 20
# alumno["sexo"]  = "Binario"
# alumno["direccion"] = "San juan"
# print(alumno)

#Agregando clave y valor
# alumno["dni"] = 12345678
# print(alumno)



# Daivis aprovecha la OFERTA y compra una cafetera

# compra = {
#     "cliente": {
#         "nombre":"Daivis",
#         "apellido":"Gonzalez",
#         "documento":"123456789",
#         "email":"daivis@gmail.com"
#         },
#     "productos": [
#         {
#             "codigo":"cafetera",
#             "precio": 25000,
#             "cantidad": 2
#         },
#         {
#             "codigo":"taza",
#             "precio": 10000,
#             "cantidad": 1
#         }
#         ],
#     "total": 35000
#     }


#TODO: Practica Diccionario
# profesor = {
#     "nombre": "Richard",
#     "apellido": "Lozano",
#     "edad": 34,
#     "correo": "rlozano@buenosaires.com.ar"
# }
# print(profesor)

# #TODO: Mutabilidad del diccionario
# profesor["apellido"] = "Lozano2"
# print(profesor)

# #TODO: Agregando nueva clave
# profesor["telefono"] = "(+54) 9-11-1234-5678"
# print(profesor)

# #TODO: UPDATE()
# profesor.update({"direccion": "Humberto Primo 2252", "Localidad": "CABA"})
# print(profesor)
# profesor.update()
# print(profesor)

# #TODO: LEN
# print(len(profesor))

#TODO: Mas de valor
# profesor = {
#     "nombre": "Richard",
#     "apellido": "Lozano",
#     "edad": 34,
#     "correo": "rlozano@buenosaires.com.ar",
#     "hobbies": ["Futbol", "Tennis", "Programar"]
# }

# print(len(profesor["hobbies"][0]))
# print(type(profesor["hobbies"][0]))

#TODO: DEL  ==> Eliminar una clave de mi dicc
# del profesor["edad"]
# print(profesor)

#TODO: IN
# print("nombre" in profesor)

#TODO: CLEAR() ==> Borrar todos los valores de un dicc
# profesor.clear()
# print(profesor)
#Otra forma
#profesor = {}

#TODO: POP() Eliminar un elemento especifico de mi diccionario
# profesor = {
#     "nombre": "Richard",
#     "apellido": "Lozano",
#     "edad": 34,
#     "correo": "rlozano@buenosaires.com.ar",
#     "hobbies": ["Futbol", "Tennis", "Programar"]
# }
# print(profesor)
# item_eliminado = profesor.pop("apellido")
# print(item_eliminado)
# print(profesor.pop("apellido")) #Forma 2
# print(profesor)

#TODO: SOLUCION SET
#1-
# grupo = {"Miguel", "Blanca", "Mario", "Andres"}
# grupo.update({"Ana", "Ramon", "Marta", "Eric", "David"})
# print(grupo)

# #2- 
# for nombre in ["Mario", "Miguel", "Esteban"]:
#     grupo.discard(nombre)

# print(grupo)


#TODO: RECORRER DICCIONARIOS
profesor = {
    "nombre": "Richard",
    "apellido": "Lozano",
    "edad": 34,
    "correo": "rlozano@buenosaires.com.ar",
    "hobbies": ["Futbol", "Tennis", "Programar"]
}

#Recorriendo las claves
print("CLAVES")
for clave in profesor.keys():
    print(clave)

#Recorriendo los valores
print("")
print("VALORES")
for valor in profesor.values():
    print(valor)

#Recorriendo los items
print("")
print("ITEMS")
for items in profesor.items():
    print(items)
