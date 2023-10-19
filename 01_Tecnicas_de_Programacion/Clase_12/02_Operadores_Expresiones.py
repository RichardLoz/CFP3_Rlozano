
#TODO: QUe son los operadores:
# Los operadores son calculos que se llevan a cabo sobre dos argumentos conocidos como "Operandos"
# Operadores: - + * /
# print(8 + 5)
# print(6 - 5)
# print(10 * 5)
# print(20 / 5)

# #TODO: Algebraicas: Si al menos un operando es una variable
# peso = 10
# print(peso + 2)
# print(peso * 5)

#TODO: Tipo Logico: Booleanos (True(1) y False(0))
# print(True > False) #True
# print(False > True) #False
# print(True == False) #False

#TODO: Operadores Relacionales: Simbolos que se usan para comparar valores
# print(2 > 3)  #False
# print(5 >= 5) # True
# print(15 > 9) # True
# print("hola" == "Hola") # False
# print(2 == "2") # False
# print("Paula" == "Paula") # True

#TODO: NEGACION: Si negamos una cosa que es verdad, se convierte en falso y si negamos una cosa que falsa, se convierte en verdad
# print("2" != 2) # False
# print(7 != 7) # False


#TODO: EJERCICIOS: Calcular Mentalmente
# expresiones = [
#     False == True,  #False
#     10 >= 2 * 4, #True
#     33/3 == 11, # False - TRUE
#     True > False, # True
#     20 / 2 != 10,  # False (TRUE)
#     True * 5 == 2.5 * 2, # True 
#     True - 1 == False,  # False
#     12 / 2 <= 10, # True
#     True == "True",  # False
#     False + 1 == True, # False
#     1 + 4 != True + 3, # False
#     False + 4 == 4 / True # True
# ]

# print(expresiones)


#TODO: Operador AND (Y): Agrupa a traves de la union (Y) y si ambas afirmaciones son verdaderas, el resultado final es verdadero
# print(2 == 2 and 2 > 5) #False
# print(2 == 2 and 2 < 5) #True

# #TODO: Operador OR (Separa): Si al menos una de las dos afirmaciones es verdadera, el resultado final es verdadero
# print(2 == 2 or 2 > 5) #False
# print(2 != 2 or 2 > 5) #True

#TODO: TABLA VERDAD


#TODO: OPERADORES LOGICOS: 
# NOT: Negacion, solo afecta a los de tipo logico (True - False) 
# print(not True)
# print(not 2 + 2 == 5)
# print(not 2 + 2 == 4)


#TODO: EJERCICIOS:
# expresiones = [
#     not False, #True
#    not 3 == 5, # True
#     33/3 == 11 and 5 > 2, # True
#     True or False, #True
#    True*5 == 2.5*2 or 123 >= 23, #False
#     12 > 7 and True < False # False
# ]

# print(expresiones)


#TODO: EXPRESIONES ANIDADAS: Combinaciones de diferentes expresiones (REGLA DE PROCEDENCIA) (),**, */, +-

#TODO: EJERCICIOS
# A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se cumplen TODAS las siguientes condiciones, encadenando operadores lógicos en una sola línea:

# NOMBRE sea diferente de cuatro asteriscos “****”
# EDAD sea mayor que 10 y a su vez menor que 18
# Que la longitud de NOMBRE sea mayor o igual a 3 pero a la vez menor que 10
# EDAD multiplicada por 4 sea mayor que 40

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# condicion = [nombre != "****",edad > 10 and edad < 18, len(nombre) >= 3 and len(nombre) < 10, edad * 4 > 40 ]
# print(condicion) 
