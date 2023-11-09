
#TODO: FOR (SABIENDO LA CANTIDAD DE ITERACIONES)
# meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre","Diciembre"]

#meses = [mes[0], mes[1],mes[2].......,mes[11]]

#PSEINT ==> ARREGLO ==> un tipo de dato
#PYTHON ==> LISTAS ==> Heterogenas ==> Multiple tipos de datos
# ARRAY
# print("Usando Print")
# print(meses)
# # 
# print("Usando FOR")
# for mes in meses:
#     print(f"Soy un mes del año y mi nombre es {mes}")

# lista = [0,1,2,3,4,5,6,7,8,9,10]

# for num in lista:
#     print(f"Soy un elemento de la lista y valgo {num}")
#     num *=5
#     print(f"Soy el mismo elemento, pero ahora valgo {num}")

#Recorriendo un string
# nombre = "TOMAS"
# for i in nombre:
#     print(i)

# RANGE
# for i in range(1,11,1):
#     print(i)

#Los numeros pares de 1 al 20 incluido
# for i in range(0,21,2):
#     print(i)

#El usuario defina el inicio, fin y los pasos.
# inicio = int(input("Ingrese el inicio: "))
# fin = int(input("Ingrese el fin: "))
# pasos = int(input("Ingrese el pasos: "))

# for i in range(inicio, fin, pasos):
#     print(i)

#RECORRER DE MANERA INVERSA
# for i in range(11,1,-1):
#     print(i)

#TODO: EJECICIO:
# Escribir un programa que genere una lista de numeros pares del 0 al 10 (ambos inclusive), para esto debemos utilizar un ciclo FOR y el metodo append. Finalmente imprimir la lista de numeros por pantalla.
# lista = []
# for i in range (0,12,2):
#     print(i)
#     lista.append(i)
# print(lista)

#TODO: Lista de numeros Pares - Impares
# lista_pares = []
# lista_impares = []
# for i in range(11):
#     if i % 2 == 0:
#         lista_pares.append(i)
#     else:
#         lista_impares.append(i)
# print(f"Lista de numeros pares: {lista_pares}")
# print(lista_impares)

#TODO: Dada una lista numeros=[1,2,3,4,5] hacer un programa que recorra la lista y vaya eliminando los elementos de la lista uno a uno y los muestre por pantalla hasta que la liste quede vacia
#TODO: DESCENDENTE
# numeros = [1,2,3,4,5]
# for i in range(len(numeros)-1, -1, -1):
#     numero_eliminado = numeros.pop(i)
#     print(f"Se elimino el numero {numero_eliminado}")
# print(f"La lista quedo vacia {numeros}")

# #TODO: ASCENDENTE
# numeros = [1,2,3,4,5]
# for _ in range(len(numeros)):
#     print(numeros)
#     numero_eliminado = numeros.pop(0)
#     print(numeros)
#     print(f"Se elimino el numero {numero_eliminado}")
# print(f"La lista quedo vacia {numeros}")

#TODO: Crear un programa que almacene dos listas: usuarios y contraseñas y solicite al ingresante los datos de login (usuario y contraseña) solo se admiten 3 intentos de inicio de sesión.
# usuarios = ["Bryan", "Tomas", "Jesica", "Santiago", "Milagros","Tania"]
# contraseñas = ["pepito", "123", "25", "contraseña","1425","milo"]
# intentos = 3
# while intentos > 0 :
#     usuario_ingresado = input("Ingrese su usuario: ").capitalize()
#     contraseña_ingresada = input("Ingrese su contraseña: ").lower()
#     if usuario_ingresado in usuarios and contraseña_ingresada == contraseñas[usuarios.index(usuario_ingresado)]:
#         print(f"Inicio de sesión correcto. Bienvenido {usuario_ingresado}")
#         break
#     else:
#         print("Credenciales incorrectas, intente nuevamente")
#         intentos -= 1
# if intentos == 0:
#     print("Su cuenta fue bloqueada, comunicarse con el departamento de Sistemas")