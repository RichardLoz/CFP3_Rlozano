
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
        
suma_bucle()
        