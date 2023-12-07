
#TODO: ESTRUCTURA DE UNA FUNCION
# def nombre_funcion():
#     SENTENCIAS
#     RETURN [EXPRESION]

#Sin RETURN
# def saludar():
#     print("Hola Daivis")

# resultado = saludar()
# print(resultado)

# #CON RETURN
# def saludar_return():
#     return "Hola Daivis"

# resultado2 = saludar_return()
# print(resultado2)


#TODO: FUNCIONES CON PARAMETROS
# nombre = "Jesica"
# print(f"Hola {nombre}")
                       # Roberto
# def mi_nombre_es(nombre="Roberto"): #Parametro
#     print(f"Hola {nombre}") #Roberto


# mi_nombre_es("Daivis")  #mi_nombre_es("Roberto")



#TODO: VARIABLES LOCALES
# def test():
#     variable_test = 10
#     print(variable_test)
    
# test()
# print(variable_test)

#TODO: VARIABLES GLOBALES
# variable_test = "Roberto"
# def test():
#     variable_test = "Daivis"
#     print(variable_test)
    
# test()
# print(variable_test)



#TODO: RETURN
# def saludo_con_nombre(nombre): 
#     saludo = print(f"Hola {nombre}") 
#     return saludo
# #LO IGNORA
#     print("El saludo fue correcto!!")
#     print("El saludo fue correcto!!")


# saludo_con_nombre("Milagros")


#TODO: RETURN MULTIPLEVALORES
# def test():
#     return "Daivis", False, 10, [1,2,3]

# print(test())

#TODO: CALCULAR EL MAYOR DE 3 NUMEROS:



    
# def num_mayor(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#          return f"El numero mayor es {num1}"
#     elif num2>num1 and num2>num3:
#         return f"El numero mayor es {num2}"
#     else:
#         return f"El numero mayor es {num3}"
    
# print(num_mayor(45,334,22))


#TODO: ES PALINDROMO
# palabra = input("Ingrese la palabra: ")
# palabra_invertida = palabra[::-1]
# if palabra == palabra_invertida:
#     print("Es palindromo")
# else:
#     print("No es palindromo")
    
    
# def es_palindromo(palabra): #neuquen
#     palabra_invertida = palabra[::-1] #neuquen
#     if palabra == palabra_invertida:
#         #"neuquen" == "neuquen"
#         return "Es palindromo"
#     else:
#         return "No es palindromo"

# palabra_usuario = input("Ingrese una palabra: ") #Neuquen
# resultado = es_palindromo(palabra_usuario) #neuquen
# print(resultado)

#TODO: VALORES POR DEFAULT
# AREA DE UN CIRCULO
# def area_circulo(radio, pi=3.14):
#     area =  pi * (radio ** 2)
#     return round(area,3)

# resultado = area_circulo(pi = 3.1416, radio = 8)
# print(resultado)
# resultado = area_circulo(pi=3.1416, radio=10)
# print(resultado)

# def area_circulo(radio=10, pi=3.14):
#     return pi * (radio ** 2)

# resultado = area_circulo(radio = 20)
# print(resultado)

# TODO: Define una función llamada invertir_lista que tome una lista como parámetro y devuelva la lista invertida.

#TODO: Dada una lista = [2,3,7,1,8,12,5], devolver los numeros pares e impares por separado.


# def separar_pares_impares(lista):
#     pares = []
#     impares = []
#     for i in lista:
#         if i % 2 == 0:
#             pares.append(i)
#         else:
#             impares.append(i)
#     return pares, impares
# #   positivo = return pares
# #   negativo = return impares
# numeros = [2,3,7,1,8,12,5]
# positivo , negativo = separar_pares_impares(numeros)
# print(f"Numeros pares: {positivo}")
# print(f"Numeros impares: {negativo}")

def separar_pares_impares(lista):
    pares = [i for i in lista if i % 2 == 0]
    impares = [i for i in lista if i % 2 != 0]
    return pares , impares

numeros = [2,3,7,1,8,12,5]
positivo , negativo = separar_pares_impares(numeros)
print(f"Numeros pares: {positivo}")
print(f"Numeros impares: {negativo}")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















































