
#TODO: Tipos de datos
#Entero
x = 10
#Decimal
y = 2.5
#Boolean
z = True
#String
w = "Hola"

#Imprimir mensajes por pantalla
# print("La variable x es igual a",x)
# print(f"La variable x es igual a {x}")

#Imprimimos el tipo de dato de las variables
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(w))

#Operaciones aritmeticas
# num1 = 7
# num2 = 3
# suma = num1 + num2
# resta = num1 - num2
# multi = num1 * num2
# divi = num1 / num2
# potencia = num1 **num2
# divi_entera = num1 // num2 # 2
# divi_resto = num1 % num2 # 
# print(f"El resultado de las operaciones de los numeros {num1} y {num2}: suma: {suma}, resta: {resta}") 

#TODO: Reglas de PROCEDENCIA
#El orden de las operaciones es de izquierda a derecha y el orden es el siguiente:
#1- Parentesis
#2- Potencia y raices
#3- Multiplicación y División
#4- Suma y resta

#TODO: Formas de imprimir mensajes por pantalla
# print("Esto es un 'texto' entre comillas ")
# print("Esto es una cadena\tcon tabulacion")
# print("Esto es una cadena\ncon salto de linea")
# print("""
#     Menu de operaciones
#     1- Suma
#     2- Resta
#     3- Multiplicacion
#     4- Division
#       """)

#TODO: Capturar valores por teclado
# nombre=input("Ingrese su nombre: ")
# print(nombre)
# print(f"El nombre ingresado fue {nombre}")

#TODO: INT ==> Parsear un variable a INT
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese un numero: "))
# suma = num1 + num2
# print(f"El resultado es {suma}")



#TODO: Indexacion de las cadenas(str)
# animal = "Perro"
# print(animal)
# print(animal[0])
# print(animal[4])
# print(animal[2])

# #TODO: LEN() ==> Me devuelve la longitud de una variable
# print(f"La longitud de mi animal es {len(animal)}")

#TODO: SLICING
#Sintaxis ==> [inicio:fin:paso]
# fruta = "Durasno"
# # fruta[4] = "z"
# # print(fruta)
# fruta = fruta[0:4] + 'z' + fruta[5:]
# print(fruta)

# cadena_1 = "moderno"
# cadena_2 = "Python"
# cadena_3 = "es un lenguaje"
# cadena_4 = "de programacion"
# cadena_5 = cadena_2 + " " + cadena_3 + " " + cadena_4 + " "+ cadena_1
# print(cadena_5)
# # Python es un lenguaje de programacion moderno

# #TODO: Ejercicios SLICING ==> dar vuelta una cadena
# frase = " Hola Roberto, como estas?"
# print(frase)
# print(len(frase))
# print(frase[25:0:-1])


#TODO: Modificar un elemento de una cadena
materia = "Programacyon"

#SOlucion:
materia = materia[0:9:1] + "i" + materia[10::]
print(materia)
print(f"{materia[0:9:1]}i{materia[10::]}")
