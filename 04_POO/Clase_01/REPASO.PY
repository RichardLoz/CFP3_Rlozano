numeros_pares = []
numeros_impares = []

while True:
    numero = int(input("Por favor ingrese un número (o ingrese 0 para terminar): "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Números pares ingresados:", numeros_pares)
print(f"Suma de numeros pares: {sum(numeros_pares)}")
print(f"Promedio de numeros pares: {sum(numeros_pares)/len(numeros_pares)}")
print("Números impares ingresados:", numeros_impares)
print(f"Suma de numeros impares: {sum(numeros_impares)}")
