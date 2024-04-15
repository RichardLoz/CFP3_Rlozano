
#TODO: IF: Dentro de las sentencias condicionales es una de las mas utilizadas, al utilizar la pabra reservada "IF" le indicamos a nuestro programa que si se cumple una determinara condicion deberá ejecutar cierta porción de código.

# Ejemplo

# if (edad >= 18) and (genero == 'F'):
#     print("Puede pasar")
# else:
#     print("No puede pasar")
    
# Ejemplo usando el NOT
# Si pasamos como valor "False" no me ejecutara ningun mensaje, pero si utilizo el operador de negacion "NOT", me convertira el False en True
# if not False:
#     print("Esto es Falso")


# Ejemplo solicitando datos por teclado
# age = int(input("Ingrese su edad: "))
# if age >= 18:
#     print("Puede pasar")



# Multiples IF
# a = 5
# b = 10

# if a == 5:
#     print(f"Verdadero, a vale {a}")
#     if b == 10:
#         print(f"Verdadero, b vale {b}")
        
# Utilizando el operador AND
# a = 5
# b = 10
# if(a == 5 and b == 10):
#     print(f"a vale {a} y b vale {b}")


#TODO: ELSE: (SINO) Se puede utilizar junto con los "IF" para comprobar los casos que son "FALSE", de este modo se ejecutara la porcion de codigo contenida en el "ELSE" solo si no se cumple ninguna condición antes planteada.

# Ejemplo:

# edad = 11

# if edad >= 18:
#     print("Puede pasar")
# else:
#     print("No puede ingresar")
    

# # Ejemplo_02

# num1 = 5
# num2 = 10
# if(num1 > num2):
#     print(f"{num1} es mayor a {num2}")
# else:
#     print(f"{num2} es mayor que {num1}")


# ELIF
edad =  24
if edad >= 36:
    print("Es un adulto")
elif edad == 24:
	print("la edad es 24")
elif edad == 24:
    print("La edad es 24_bis")
else:
	print("No sabemos la edad")



# edad = int(input("Ingrese su edad: "))

# if edad > 18:
#     print("Usted puede pasar")
# elif edad == 18:
#     print("No puede pasar, vuelva el prox año")
# elif edad == 17:
#     print("No puede ingresar, vuelva en 2 años")
# elif edad == 18:
#     print("No puede ingresar, vuelva en 3 años")
# else:
#     print("No ingreso un valor valido")



#TODO: SOLUCION

# nombre = input("Ingrese su nombre: ")
# preferencia = input("Ingrese su preferencia")

# # Fan Marvel y nombre > M
# if (preferencia == "Marvel" and nombre <= "M") or (preferencia == "Capcom" and nombre >= "N"):
#     print(f"{nombre} pertenece al grupo A")
# else:
#     print(f"{nombre} pertenece al grupo B")