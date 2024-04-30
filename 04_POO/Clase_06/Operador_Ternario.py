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
