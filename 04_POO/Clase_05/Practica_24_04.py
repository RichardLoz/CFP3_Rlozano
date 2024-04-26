
#TODO: 1- Crear una funcion que sume dos numeros

def suma(num1 , num2):
    resultado = num1 + num2
    return resultado

resultado_suma = suma(78,2)
#print(resultado_suma)

#TODO: 2- A la funcion anterior modificarla para que los numeros los pueda introducir el usuarios.

#num1 =int(input("Ingrese el primer valor: "))
#num2 =int(input("Ingrese el segundo valor: "))

#resul_suma_teclado = suma(num1,num2)
#print(f"La suma entre {num1} y {num2} es {resul_suma_teclado}")

#TODO: Incorporar la logica para que solicite de manera indefinida la suma de dos numeros, hasta que una condición corte el ciclo.

def suma(num1,num2):
    resultado = num1 + num2
    return resultado

def suma_bucle():
    while True:
        num1 = int(input("Ingrese el primer valor (Ingrese un numero negativo para salir: )"))
        if num1 < 0:
            print("Usted esta saliendo el programa.....")
            break
        num2 = int(input("Ingrese el segundo valor: "))
        resultado_suma = suma(num1, num2)
        print(f"La suma entre {num1} y {num2} es {resultado_suma}")
        
#suma_bucle()


#TODO: ENUMERATE: Es una funcion en Python que se utiliza para enumerar elementos de una secuencia (lista, tuplas, etc), mientras los recorre en un bucle. Enumerate toma dos parametros: la secuencia que se quiere sumar y opcionalmente el indice inicial. Devuelve un objeto enumerado que produce tuplas que contienen un contador y un elemento de la secuencia.

# frutas = ["manzana", "banana", "pera", "anana", "naranja"]

# for indice,fruta in enumerate (frutas, start = 10):
#     print(f"Fruta {indice}: {fruta}")


#TODO: Lo que se solicita es que se guarden todos los resultados de las sumas y mostrarlos al salir del bucle

def suma(num1,num2):
    resultado = num1 + num2
    return resultado

def suma_bucle():
    resultados = []
    total = 0
    while True:
        num1 = int(input("Ingrese el primer valor (Ingrese un numero negativo para salir: )"))
        if num1 < 0:
            print("Usted esta saliendo el programa.....")
            break
        num2 = int(input("Ingrese el segundo valor: "))
        resultado_suma = suma(num1, num2)
        resultados.append(resultado_suma)
        print(f"La suma entre {num1} y {num2} es {resultado_suma}") 
    #Mostrar Resultados
    print(f"El resultado de las sumas es: {sum(resultados)} ")
    for indice, resultado in enumerate(resultados, start=1):
        print(f"Suma {indice}: {resultado}")
        
#Pendiente: PROMEDIO
        
    
        
#suma_bucle()




        