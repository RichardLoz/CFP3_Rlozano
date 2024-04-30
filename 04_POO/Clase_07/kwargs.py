
#TODO: Kwargs: Es una sintaxis que se utiliza en Python para aceptar un numero indefinido de argumentos de palabras claves en una funcion. La palabra clave **kwargs significa "Keyword arguments" (Argumento de palabras claves). Estos argumentos se pasan en la funcion como un diccionario, donde las claves son los nombres de los argumentos y los valores son los valores asociados a esos argumentos.

#Estructura ejemplo
def datos_alumnos(**kwargs):
    pass

datos_alumnos(nombre= 'Richard', apellido = 'Lopez', edad = 18, direcc = 'Cabildo 3000')

#Ejemplo
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"La clave es {clave} y su valor es {valor}")
        
#imprimir_info(nombre = "Richard", apellido = "Lozano", edad = 18, direcc = "Aristobulo del valle 2344",cp = 1602)


#TODO: EJERCICIO : Escribir una funcion llamada "Combinar diccionarios", que tome varios diccionarios como argumentos de palara clave y devuelva un unico diccionario que contenga la combinacion de todos los diccionarios proporcionados.
def combinar_dicc(**kwargs):
    resultado = {}
    for diccionario in kwargs.values():
        resultado.update(diccionario)
    return resultado

dicc_1 = {"a":1,"b":2,"c":3}

dicc_2 = {"d":4,"f":5,"g":6}

resultado = combinar_dicc(dic1 = dicc_1, dic2 = dicc_2 )
print(resultado)# {"a":1,"b":2,"c":3, "d":4,"f":5, "g":6}
