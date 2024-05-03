
#TODO: EJERCICIOS:

#TODO: 1- Escribir una funcion llamada "contar_vocales" que tome como argumento una cadena de texto y cuente el numero de veces que aparece cada vocal (a,e,i,o,u) en la cadena.
# def contar_vocales(cadena):
#     vocales = {
#         "a": 0,
#         "e": 0,
#         "i": 0,
#         "o": 0,
#         "u": 0,
#     }
#     for letra in cadena:
#         if letra.lower() in vocales:
#             vocales[letra.lower()] +=1
#     return vocales
# cadena = input("Ingrese un texto: ")
# resultado = contar_vocales(cadena)

# with open("resultado.txt", "w") as archivo:
#     for vocal, cantidad in resultado.items():
#         archivo.write(f"La vocal {vocal} aparece {cantidad} de veces \n")

# print("Resultado guardados con exito")
    

#TODO: 2- Escribir una funcion que acepte una cantidad variable de argumentos numericos y devuelva el valor maximo y minuto de todos los argumentos.
#Opcion 1
def valor_min_max(*args):
    if not args:
        return "Ingrese numeros...."
    else:
        minimo = None
        maximo = None
        for num in args:
            if num < minimo:
                minimo = num
            if num > maximo:
                maximo = num
        return minimo, maximo
valores = valor_min_max(-10,23325,12,4124,-2414,24,1)
print(f"Los valores minimos y maximos son: {valores}")

#Opcion_2
# def valor_min_max(*args):
#     if not args:
#         return "Ingrese numeros...."
#     else:
#         return min(args), max(args)
# valores = valor_min_max(-10,23325,12,4124,-2414,24,1)
# print(f"Los valores minimos y maximos son: {valores}")
