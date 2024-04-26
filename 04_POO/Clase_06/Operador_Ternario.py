
#TODO: Cual seria la logica para evaluar un numero y si es este es mayor o igual a 6 mostrar el mensaje "Verde" y sino mostrar el mensaje "Rojo".

#Variables
#En Python tenemos la posibilidad de declarar variables vacias, es decir con valor "None"
nota = 5
color = None

# if nota >= 6:
#     print("Verde")
# else:
#     print("Rojo")
    
    
#Operador Ternario: Nos permite evaluar una condicion de manera abreviada.

# nota = 5
# color = "Verde" if nota >= 6 else "Rojo"

# print(nota,color)

#TODO: Dado un numero entero, imprimir "Es PAR" si el numero es PAR, y "Es IMPAR" si el numero es IMPAR.
#TRADICIONAL
# num = int(input("Ingrese un numero: "))
# if num % 2 == 0:
#     print("Es PAR")
# else:
#     print("Es IMPAR")

#TERNARIO
# num = int(input("Ingrese un numero: "))
# resultado = "ES PAR" if num % 2== 0 else "Es IMPAR"
# print(resultado)


#TODO: Dado dos numeros enteros A y B, Imprimir "A es MAYOR" si A es Mayor que B, "B es MAYOR", si B es MAYOR que A, si son IGUALES, mostrar el mensaje "AMBOS SON IGUALES".
#FORMA TRADICIONAL
a = 30
b = 28

if a > b:
    print(f"{a} es MAYOR")
elif b > a:
    print(f"{b} es MAYOR")
else:
    print("Ambos son iguales")


#FORMA OPERADOR TERNARIO
a = 30
b = 28

resultado = "A es mayor" if a > b else ("B es mayor" if b > a else "Son iguales")

print(resultado)
