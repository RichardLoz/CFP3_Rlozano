
#TODO: QUE SON LOS OPERADORES?
# Los operadores son calculos que se llevan a cabo sobre dos argumentos conocidos como "OPERANDOS"
# OPERADORES: - + * /
# ARITMETICAS: Si ambos operandos son valores literales
# print(8 + 5)
# print(6 - 5)
# print(10 * 5)
# print(20 / 5)

# #ALGEBRAICAS: Si al menos un operando es una variable
# peso = 10
# print(peso + 2)
# print(peso * 5)

# # TIPO LOGICO: Booleano (True (1) - False (0))
# print(True > False)
# print(False > True)
# print(True == False)

# # OPERADORES RELACIONALES: Simbolos que se usan para comparar dos valores
# print(2 > 3)
# print(5 >= 5)
# print(15 > 9)
# print("hola" == "Hola")
# print(2 == "2")
# print("Paula" == "Paula")

# # NEGACION: Si negamos una cosa es que es verdad, se convierte en mentira y si negamos una cosa que es mentira, esta se convierte en verdad
# print("2" != 2)
# print(7 != 7)


#TODO: EJERCICIOS: Calcular Mentalmente
# expresiones = [
#     False == True,
#     10 >= 2 * 4 
#     33/3 == 11,
#     True > False,
#     20 / 2 != 10, 
#     True * 5 == 2.5 * 2
#     True - 1 == False, 
#     12 / 2 <= 10,
#     True == "True", 
#     False + 1 == True,
#     1 + 4 != True + 3,
#     False + 4 == 4 / True
# ]


#TODO: OPERADORES LOGICOS: 
# NOT: Negacion, solo afecta a los de tipo logico (True - False) 
#print(not True)
# print(not 2 + 2 == 5)
# print(not 2 + 2 == 4)

# AND: (Conjuncion) Agrupa a través de la union (Y) y si ambas afirmaciones son verdaderas, el resultado es verdadero
# print( 2 == 2 and 2 > 5 ) 
    
# print( 2 == 4 and 2 < 5 )
 
# # OR: Operador de disyuncion (Separa), si al menos una de las dos afirmaciones es verdadera, el resultado final es verdadero
# print( 2 == 2 or 2 > 5 ) 
# print( 2 == 4 or 2 < 5 )
# print ( 3 != 3 or 4 > 5)


#TODO: EJERCICIOS:

# expresiones = [
#     not False,
#    not 3 == 5,
#     33/3 == 11 and 5 > 2,
#     True or False,
#    True*5 == 2.5*2 or 123 >= 23,
#     12 > 7 and True < False
# ]


#TODO: EXPRESIONES ANIDADAS: Combinaciones de diferentes expresiones (REGLA DE PROCEDENCIA) (),**, */, +-

#TODO: EJERCICIOS
# A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se cumplen TODAS las siguientes condiciones, encadenando operadores lógicos en una sola línea:

# NOMBRE sea diferente de cuatro asteriscos “****”
# EDAD sea mayor que 10 y a su vez menor que 18
# Que la longitud de NOMBRE sea mayor o igual a 3 pero a la vez menor que 10
# EDAD multiplicada por 4 sea mayor que 40

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad :"))

# condicion =[nombre != '****', edad >10 and edad < 18,len(nombre) >= 3]
# print(condicion)





# print(expresiones)

#TODO: OPERADOR DE ASIGNACION: Este operador asigna un valor a una variable
#mi_variable = "Budin"

#TODO: Operadores de asignacion compuestos: Se debe tener una variable previamente declarada, sino devolverá un error
#Suma
a = 1
# a +=1
#Equivalente a decir a = a + 1
# print(a)

# #Resta
# a -= 1
# print(a)

# # #Multiplicación
# a *= 10
# print(a)

# # #Division
# a /= 2
# print(a)

# #Potencia
# a **= 2
# print(a)

