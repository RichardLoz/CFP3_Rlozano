
#TODO: WHILE (No se sabe la cantidad de iteraciones)
#Sintaxis
# while condicion:
#     instrucciones

#Ejemplo_01

# num = 5

# while num > 0:
#     print(f"{num}")
#     num -= 1
    
# print("Termino el WHILE")


#Ejemplo_02
# n = 0
# while n <= 5:
#     n += 1
#     print(f"N vale {n}")


#Ejemplo_03: Bucle infinito
# while True:
#     print("Esto es un bucle infinito")


#TODO: While-Else
#Sintaxis
# while condicion:
#     instrucciones
# else:
#     intrucciones


#Ejemplo_04
# intento = 1
# while intento <=3:
#     msg = input("Escribe SI: ")
#     if msg == "SI":
#         print(f"Ok, lo conseguiste en el intento {intento}")
#         break
#     intento += 1
# else:
#     print("Usaste todos tus intentos disponibles")

#TODO: Ejercicio
#TODO: Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, cuando lo haga mostrar por pantalla la suma de todos los números ingresados.
# num = 1
# suma = 0
# while num !=0:
#     num = int(input("Ingrese un numero, (0 para terminar): "))
#     suma = suma + num
# else:
#     print(f"Usted finalizo el programa y la suma acumulada es {suma}")





# num = 1
# suma = 0
# while num != 0:
#     num = int(input("Ingrese un numero (0 para terminar): "))    
#     suma = suma + num
# else:
#     print(f"Usted finalizo el programa, la suma total es {suma}")

#TODO: BREAK: Sirve para salir del bucle inmediatamente se cumpla una condicion determinada.
# n = 5
# while n < 10:
#     n -= 1
#     if n == 2:
#         print(f"Ahora que N vale {n}, termino el programa")
#         break
#     else:
#         print(f"N vale {n}")

#TODO: CONTINUE: Sirve para omitir una iteracion y continuar con la siguiente si se cumple una condicion determinada.
# n = 0
# while n < 10:
#     n += 1
#     if n == 2:
#         print(f"Ahora que N vale {n}, voy a continuar iterando")
#         continue
#     else:
#         print(f"N vale {n}")


#TODO: PASS: Se utiliza comunmente en bloques de codigo que aún no se han implementado o en funciones que aun no tienen contenido.

# def alta_materia():
#     pass

#TODO: FOR: (Sabiendo la cantidad de iteraciones)

# alumnos = ["Nestor","Joaquin","Xavi","Delfina","Facu","Roberto"]

# for i in alumnos:
#     print(f"Soy un alumno de la clase y mi nombre es {i}")
    

# Ejemplo:
# lista = [0,1,2,3,4,5,6,7,8,9,10]

# for num in lista:
#     print(f"Soy un elemento de la lista y valgo {num}")
#     num *= 5
#     print(f"Soy un elemento de la lista y ahora valgo {num}")

#TODO: ENUMERATE
# alumnos = ["Nestor","Joaquin","Xavi","Delfina","Facu","Roberto"]

# for indice,i in enumerate(alumnos,start=1):
#     print(f"indice:{indice}")
#     print(f"nombre: {i}\n\n")
#     print(f"El alumno {i} tiene el indice {indice}")

#TODO: Recorrer un String
# texto = "Hola Xavi, como andas?"
# texto2= ""
# # for letra in texto:
# #     print(letra)

# for i in texto:
#     texto2 = i * 100
#     print(texto2)


#TODO: RANGE

# for num in range(0,11,2):
#     print(num)

# inicio = int(input("Ingrese el inicio: "))
# final = int(input("Ingrese el final: "))
# pasos = int(input("Ingrese los pasos: "))

# for i in range(inicio,final+1,pasos):
#     print(i)

#TODO: Recorrer de manera descendente
# for i in range(10,1,-1):
#     print(i)



