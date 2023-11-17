
#TODO: REDONDEO DE NUMEROS DECIMALES

#1- Clasico
numero_decimal = 49.23592865263
print("Numero decimal: %.3f" %numero_decimal)

#2- Usando Format()
numero_decimal2 = 124.2352365236
print(float('{0:.4f}'.format(numero_decimal2)))

#3- ROUND()
numero_decimal3 = 13.2352368236
print(round(numero_decimal3,6))