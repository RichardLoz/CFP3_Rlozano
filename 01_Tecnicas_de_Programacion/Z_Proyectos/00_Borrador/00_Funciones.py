
#TODO: FUNCIONES
#Hasta ahora veniamos trabajando de esta forma
#print("Hola chicos")

#Con funciones
# def saludar():
#     print("Hola chicos")

# #Invocando
# saludar()

#TODO: Saludo con nombre
# nombre = "Jesica"
# print(f"Hola {nombre}")

# def saludar_con_nombre(nombre):
#     print(f"Hola {nombre}")

# saludar_con_nombre("Jesica")

# def despedida():
#     saludo = "Adios"

# def suma(a,b):
#     resultado = a + b
#     print(resultado)
    
# def suma2(a,b):
#     resultado = a + b
#     return resultado

# sumador = suma(5,2)
# print(sumador)    #==> #Me saldra NONE, ya que no estoy retornando un valor valido
# sumando = suma2(5,2)  #==> # Aca si funciona correctamente ya que estoy retonando un valor
# print(sumando)

# Al asignar el resultado de una función a una variable, puedes reutilizar ese valor en otras partes de tu código. Esto es particularmente útil si el resultado de la función se utiliza en varios lugares y no quieres llamar la función varias veces.

# python
# Copy code
# suma_resultado = suma2(3, 4)
# print(suma_resultado)  # Imprime 7

# Pasar funciones como argumentos:

# Al asignar una función a una variable, puedes pasar esa variable a otras funciones como un argumento. Esto es útil en situaciones donde deseas que una función realice una operación en otra función.

# python
# Copy code
# def operacion(func, a, b):
#     resultado = func(a, b)
#     return resultado

# suma_resultado = operacion(suma2, 3, 4)
# print(suma_resultado)  # Imprime 7
# Claridad y legibilidad del código:

# Asignar funciones a variables puede hacer que el código sea más claro y legible, especialmente si la función realiza una operación significativa y el nombre de la variable refleja esa operación.

# python
# Copy code
# calcular_suma = suma2
# resultado = calcular_suma(3, 4)
# Trabajo con funciones de orden superior:

# En Python, las funciones son objetos de primera clase, lo que significa que pueden pasarse como argumentos a otras funciones y asignarse a variables. Esto es esencial en el trabajo con funciones de orden superior y programación funcional.

# python
# Copy code
# operacion_binaria = suma2
# resultado = operacion_binaria(3, 4)