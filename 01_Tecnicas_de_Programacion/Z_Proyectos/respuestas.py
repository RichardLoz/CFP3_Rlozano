# # Solicitar la contraseña al usuario
# contrasena_ingresada = input("Ingrese su contraseña: ")

# # Verificar la longitud de la contraseña
# if len(contrasena_ingresada) < 8:
#     print("La contraseña debe tener al menos 8 caracteres.")
# else:
#     # Verificar si contiene al menos una letra mayúscula
#     tiene_mayuscula = False
#     for caracter in contrasena_ingresada:
#         if 'A' <= caracter <= 'Z':
#             tiene_mayuscula = True
#             break

#     # Verificar si contiene al menos una letra minúscula
#     tiene_minuscula = False
#     for caracter in contrasena_ingresada:
#         if 'a' <= caracter <= 'z':
#             tiene_minuscula = True
#             break

#     # Verificar si contiene al menos un número
#     tiene_numero = False
#     for caracter in contrasena_ingresada:
#         if '0' <= caracter <= '9':
#             tiene_numero = True
#             break

#     # Mostrar el resultado
#     if tiene_mayuscula and tiene_minuscula and tiene_numero:
#         print("La contraseña es válida.")
#     else:
#         print("La contraseña no cumple con los criterios especificados.")

#2 Ordenar la lista de palabras
lista = ["arbol", "vegetal", "dinosarusio", "zapato", "leon"]

n = len(lista)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
print(lista)


#3: Comprobar si una palabra es palindromo
# palabra = input("Ingrese una palabra: ")
# palabra_reves = palabra[::-1]
# if palabra == palabra_reves:
#     print("La palabra es palindromo.")
# else:
#     print("La palabra no es palindromo.")
































#TODO: 4

codigo = ("Ingrese su codigo verificado: ")
# FSDHJSJFSFBJX
#234235235235X
#HFGBFG35325X
precio = int(input("Ingres el valor de su entrada: "))


if codigo[-1] == "X" and precio > 50000:
    print("Aventura")
    
    
    
    
#5
baja = []
temperaturas = int(input("Ingrese la temperaturas: ")) ==> 10
for i in range(temperaturas):
    if i >= 10:
        baja.append(i)
    