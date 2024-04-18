
#TODO: FUNCIONES

def saludar():
    print("Hola todos")
    
#saludar()

def saludar_nombre(nombre): #Parametro
    print(f"Hola {nombre} como estas?")
    
#saludar_nombre("Roberto") #Argumento

#TODO: Crear una funcion que imprima por pantalla el nombre, apellido y edad del alumno.

def saludo_alumno(nombre,apellido,edad):
    print(f"Mi nombre es {nombre}, mi apellido es {apellido} y tengo {edad} años.")

#saludo_alumno("Milagros","Gomez",18)


#TODO: SCOPE DE VARIABLES
#Variable local
# def var_local():
#     edad = 18
#     print(edad)

# var_local()
# print(edad)

#Variable Global
edad = 20
def var_local():
    edad = 18
    print(edad)

# var_local() #==> 18 
# print(edad) #==> 20

#TODO: RETURN
def saludo_nombres(nombre1, nombre2):
    saludando = (f"Somos las alumnes {nombre1} y {nombre2}")
    return saludando

resultado = saludo_nombres("Milagros","Jesica")
#print(resultado)

def numero():
    return 6

resultado = numero() + 10
# print(resultado)
# print(type(numero()))

#TYPE() ==> Devuelve el tipo de dato
nombre = "Milagros"
edad = 24
sexo = True
# print(type(nombre))
# print(type(edad))
# print(type(sexo))


#TODO: Crear una funcion que me devuelva el mayor de 3 numeros dados
num1 = 1502
num2 = 280
num3 = 700
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)
    
def num_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
# resultado = num_max(150,28,7)
# print(resultado)

#TODO: MAX()
def num_max(num1, num2, num3):
    return max(num1, num2, num3)

valor_maximo = num_max(10,40,9)
#print(valor_maximo)

#TODO: CREAR FUNCION QUE CALCULE EL AREA DE UN CIRCULO
#PI por radio al cuadrado ==> PI * (radio **2)
# def area_circulo(radio, pi):
#     return pi * (radio ** 2)

# resultado_area = area_circulo(10, 3.14)
# print(resultado_area)

# PARAMETRO POR DEFAULT
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado_area = area_circulo(10)
#print(resultado_area)

resultado_area = area_circulo(pi=3.15, radio=10)
#print(resultado_area)

#TODO: Crear una funcion que sume dos numeros, Si no se proporciona el segundo numero, el valor por default es 20
def suma_numeros(num1, num2=20):
    return num1 + num2

resultado = suma_numeros(40)
#print(resultado)

#TODO: Escribir una funcion que calcule el promedio de una lista de numeros. Si no se proporciona una lista, el valor por defecto sera una lista vacia. Se permite usar SUM

def promedio(lista=[]):
    if len(lista) == 0:
        return "La lista esta vacia"
    else:
        return sum(lista) / len(lista)

resultado = promedio([4,2,23,5,9])
#print(resultado)

resultado_2 = promedio()
#print(resultado_2)

#TODO: Crear una funcion que valide las credenciales del usuario, las cuales tiene las siguientes reglas:
#TODO: Usuario debe tener minimo 6 letras
#TODO: Contraseña: mayor a 8 caracteres
#Si no se cumple con estas condiciones, informar al usuario
#TODO: OPCION_1
# def validar_usuario(user,password):
#     if len(user)>=6 and len(password)>8:
#         return "Bienvenido"
#     else:
#         return "Usuario o Contraseña incorrectos"
    
# validar = validar_usuario("Richard","123456789")
# print(validar)


# #TODO: OPCION_2
# def validar_usuario_2(usuario, password):
#     if len(usuario) >= 6 and len(password) > 8:
#         return True
#     else:
#         return False

# usuario = "Richard"
# password = "123456"

# if validar_usuario_2(usuario, password):
#     print(f"Bienvenido {usuario}")
# else:
#     print("Usuario o contraseña invalidos")


# #TODO: OPCION_3
def validar_usuario_3(usuario, password):
    if len(usuario) < 6:
        print("El nombre de usuario debe tener al menos 6 caracteres.")
        return False
    elif len(password) <= 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    else:
        print("Usuario y contraseña válidos.")
        return True

usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

validar_usuario = validar_usuario_3(usuario, contrasena)
if validar_usuario:
    print("¡Bienvenido!")
else:
    print("Inténtelo nuevamente.")
    
    

