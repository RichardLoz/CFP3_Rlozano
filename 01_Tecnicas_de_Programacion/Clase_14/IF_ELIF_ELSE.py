
#TODO: IF: Dentro de las sentencias condicionales es una de las mas utilizadas, al utilizar la palabra reservada "IF" le indicamos a nuestro programa que si se cumple una determinada condicion se deberá ejecutar cierta porción de codigo.

#Ejemplo
# edad = int(input("Ingrese su edad: ")) 
# if edad > 18:
#     print("Puede ingresar al Boliche de Ronal")
# else:
#     print("No puede ingresar al Boliche de Ronal")
    
#TODO: Ejemplo usando NOT
# if not  False: #TRUE
#     print("Esto es falso")
    
#TODO: MULTIPLES IF
# a = 5
# b = 10

# #IF ANIDADO
# if a == 5:
#     print(f"Verdadero, a vale {a}")
#     if b == 10:
#         print(f"Verdadero, b vale {b}")

# #IF Multiple condicion
# if (a == 5 and b == 10):
#     print(f"Verdadero a vale {a} y b vale {b}")

#TODO: EJERCICIO: CREAR UN LOGIN DE USUARIO QUE EVALUE USUARIO Y CONTRASEÑA
#lower() ==> Transforma a minuscula
#upper() ==> Transforma a mayuscula
# DB_usuario  = input("Ingrese su usuario: ").upper()
# DB_contraseña = input("Ingrese su contraseña: ").lower()

# if DB_usuario == "MILAGROS" or DB_contraseña == "pepito123":
#     print("Acceso concedido")
# else:
#     print("Acceso denegado")



#TODO: ELIF

# edad = 24
# if edad >= 36:
#     print("Es un adulto")
# elif edad == 26:
#     print("La edad es 24")
# elif edad == 26:
#     print("La edad es 24_bis")
# elif edad == 24:
#     print("La edad es 24_bis_3")
# elif edad == 24:
#     print("La edad es 24_bis_4")
# else:
#     print("No sabemos la edad")
    
    
# print("Se termino el programa")

#TODO: IF
# Se solicita crear un programa que admita una nota y muestre un mensaje:
# menor 4 : Reprobado
# menor 6: Aprobado
# menor 8: Sobresaliente
# menor 9 : Excelente
# 10 : GENIO


#nota=float(input("Ingrese la nota del alumno: ")) #7
#input ==> "7"
#int ==> 7
#float ==> 7.0

# if nota <= 4 and nota <=6:
#     print("Aprobado")
# elif nota <= 8:
#     print("Sobresaliente")
# elif nota <=9:
#     print("Excelente")
# elif nota == 10:
#     print("GENIO")
# else:
#     print("ES MUY INTELIGENTE; ROMPIO LA MATRIX")


#SOLUCION MARVEL- CAPCOM

#TODO: Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a una preferencia (Marvel o Capcom). El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
preferencia = input("Ingrese su preferencia (Marvel - Capcom)").lower()

if (preferencia == "marvel" and nombre <= "M") or (preferencia == "capcom" and nombre > "N"):
    print(f"{nombre} esta en el grupo A")
else:
    print(f"{nombre} esta en el grupo B")