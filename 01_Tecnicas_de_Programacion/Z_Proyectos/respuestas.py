
#TODO: 1-

# Solicitamos contraseña al usuario
# contraseña_ingresada = input("Ingrese su contraseña: ")
# # Pepito123
# #Verificar si la contraseña es mayor a 8 caracteres
# if len(contraseña_ingresada) < 8 :
#     print("La contraseña debe tener minimo 8 caracteres")
# else: 
#     #Verificar si tiene mayuscula
#     for caracter in contraseña_ingresada :
#         contiene_mayuscula   = False
#         if 'A' <= caracter <= 'Z':
#             contiene_mayuscula = True
#             break
#     #Verificar si tiene minuscula
#     for caracter in contraseña_ingresada:
#         contiene_minuscula = False
#         if 'a' <= caracter <= 'z':
#             contiene_minuscula = True
#             break
#     #Verificar si tiene numero
#     for caracter in contraseña_ingresada:
#         contiene_numero = False
#         if '0' <= caracter <= '9':
#             contiene_numero = True
#             break
#     if contiene_mayuscula and contiene_minuscula and contiene_numero:
#         print("La contraseña es valida")
#     else:
#         print("Contraseña no valida")


#TODO: 2- Ordenando lista alfabeticamente
lista = ["arbol", "javier", "fernando", "victor", "manuel", "bastian", "ana", "roberto"]

n = len(lista)

for i in range(n - 1):
    for j in range(n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)





#TODO: 3-
# palabra = input("Ingrese la palabra: ")
# if palabra == palabra_invertida:
#     print("Es palindromo")
# else:
#     print("No es palindromo")


#TODO: 4-
#Solicitamos codigo verificador
#codigo_verificador = input("Ingrese su codigo verificador: ").upper()
#Solicitamos el valor de la entrada
# precio = int(input("Ingrese el valor de su entrada: "))
# #Clasificamos el tipo de entrada
# # if codigo_verificador[-1] == "X" and precio > 50000:
# #TODO: La funcion endwith en Python se utiliza para verificar si una cadena de texto termina en una subcadena especifica. Retorna True o False si la cadena termina en la subcadena proporcionada.
# if codigo_verificador.endswith("X") and precio > 50000:
#     categoria = "Aventura"
# elif codigo_verificador[-1] == "Y" and 20000 <= precio <= 50000:
#     categoria = "Familiar"
# else: 
#     categoria = "General"
# #Mostramos la categoria de la entrada
# print(f"La entrada pertenece a la categoria {categoria}")


#TODO: 5-
# temperaturas = int(input("Ingrese los registros de temperatura:  ")) 
# baja = []
# media = []
# alta = []
# for i in range(temperaturas):
#     temperatura = int(input("Ingrese la temperatura: "))
#     if temperatura <= 10:
#         baja.append(temperatura)
#     elif 10 < temperatura <= 25:
#         media.append(temperatura)
#     else: 
#         alta.append(temperatura)

# print("Temperaturas bajas: ", baja)
# print("Temperaturas media: ", media)
# print("Temperaturas alta: ", alta)
        

