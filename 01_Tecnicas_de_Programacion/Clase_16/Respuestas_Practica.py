
# TODO: 1- Escribir un programa que almacene los meses del año (por ejemplo Enero, Feberero, Marzo......Diciembre) en una lista y luego mostrar el resultado por pantalla.
# meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre","Diciembre"]
# #Mostrando el resultado
# print(meses)

# TODO: 2- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# palabra = input("Ingrese una palabra: ")
# print(palabra * 10) 
# #Salto de linea
# print("Hola\n Pedro")

#TODO: 3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
# numero = int(input("Ingrese un numero: "))

# if numero % 2 == 0:
#     print(f"{numero} es par.")
# else:
#     print(f"{numero} es impar.")
    
#TODO: 4- Para pagar un determinado impuesto se debe ser mayoro igual de 18 años y tener un ingreso mensual igual o mayor a $200.000. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario debe pagar el impuesto o no.
# edad = int(input("Ingrese su edad: "))
# sueldo = int(input("Ingrese su sueldo: "))

# if edad >= 18 and sueldo >= 200000:
#     print("El usuario debe abonar el impuesto")
# else:
#     print("El usuario NO debe abonar el impuesto")

#TODO: 5- Escribir un programa para una empresa de juegos para todas las edades que quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

# Pedir al usuario la edad del cliente
# edad = int(input("Por favor, ingrese la edad del cliente: "))

# # Calcular el precio de la entrada según la edad
# if edad < 4:
#     precio_entrada = 0
# elif 4 <= edad <= 18:
#     precio_entrada = 500
# else:
#     precio_entrada = 1000

# # Mostrar el precio de la entrada
# print(f"El precio de la entrada es: ${precio_entrada}")


#TODO: 6- Escribir un programa que solicite una contrasena y esta se deba volver a confirmar, el programa terminara cuando ambas contrasenas coincidan.

contraseña = input("Ingrese su contraseña: ")
#pepito
confirmacion = input("Confirme su contraseña: ")
#Pepito

while contraseña != confirmacion:
    print("Las contraseñas no coinciden. Vuelva a intentarlo")
    confirmacion = input("Confirme su contraseña: ")

print("Contraseña creada correctamente")
    