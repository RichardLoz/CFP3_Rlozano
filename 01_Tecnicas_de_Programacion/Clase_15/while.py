
#TODO: ESTRUCTURA WHILE
#SINTAXIS
# while (condicion): ==> TRUE
#     INTRUCCIONES

#Ejemplo_1
# num = 5
# while num > 0:  # 5 > 0 # 0 ==> FALSO
#     print(f"{num}") # ==> 1
#     num = num - 1   # 1 = 1 - 1
    
# print("Fin del bucle")

#TODO: LOGIN USANDO WHILE Y CONTADOR DE INTENTOS DE SESION
# Para salir del bucle el usuario debe ingresar correctamente las credenciales o llegar al maximo de intentos posibles.

#Acumulador
# intentos = 0

# while intentos < 3 :
#     DB_usuario  = input("Ingrese su usuario: ").upper()
#     DB_contraseña = input("Ingrese su contraseña: ").lower()
    
#     if DB_usuario == "MILAGROS" and DB_contraseña == "pepito123":
#         print("Acceso concedido")
#         break
#     else:
#         print(f"Acceso denegado, intentos restantes {2 - intentos}")
#         intentos += 1

# if intentos >= 3:
#     print("Se ha agotado el numero de intentos. Su cuenta fue bloqueada")
        
        
        
#TODO: BUCLE INFINITO
# while True:
#     print("Blucle infinito")
    
#TODO: WHILE-ELSE
#Sintaxis
# while condicion:
#    INTRUCCIONES
# else:
#    INTRUCCIONES
        
# intento = 1
# while intento <=3:
#     msg = input("Escribe SI: ").upper() #==> "si" ==> "SI"
#     if msg == "SI":
#         print(f"Ok, lo conseguiste en el intento {intento}")
#         break
#     intento += 1
# else:
#     print("Usaste todos tus intentos disponibles")

#TODO: EJERCICIO SUMA NUMEROS POR TECLADO
# acumulador = 0
# num = 1
# while num !=0:
#     num = int(input("Ingrese un numero, 0 para terminar: "))
#     acumulador = acumulador + num
# else:
#     print(f"La suma total es {acumulador}")
    
#TODO: Realizar un programa que me devuelva la suma de los primeros 100 numeros enteros. 5050

# num = 0
# acum = 0
# while num <= 100:
#     acum += num
#     #num += 1
#     print("Hola")
# print(f"La suma de los primeros 100 numeros enteros es {acum}")

#TODO: BREAK ==> Sirve para salir del bucle inmediatamente se cumpla una condicion determinada
# n = 5
# while n < 10:
#     n -= 1
#     if n == 2:
#         print(f"Ahora que N vale {n}, termino el programa")
#         break
#     else:
#         print(f"N vale {n}")

#TODO: CONTINUE ==> Sirve para omitir una iteración y continuar con la siguiente, si se cumple una condicion determinada:

# n = 0
# while n < 10:
#     n += 1
#     if n == 2:
#         print(f"Ahora que N vale {n}, voy a continuar iterando")
#         continue
#     else:
#         print(f"N vale {n}")

#TODO: PASS ==> Se utiliza comunmente en bloques de codigo que aun no se han implementado o en funciones que aun no tienen contenido
#Tania: Login Usuarios
#Ronal : Validacion de contraseña
def loginUsuario():
    pass