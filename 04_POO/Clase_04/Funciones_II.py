
#TODO: LLAMADA SIN ARGUMENTO
# def resta(num1=None,num2=None):
#     return num1-num2

# resultado = resta()
# print(resultado)


#TODO: PASO POR VALOR
num = 10
def doblar_numero(num):
    num *= 2
    return num

resultado = doblar_numero(num)
# print(resultado) #20
# print(num) #10


#TODO: PASO POR REFERENCIA
def doblar_lista(lista):
    for i in range(len(lista)):
        lista[i] *= 2
    return lista

lista = [10,20,30]
copia_lista = lista[:]
resultado = doblar_lista(copia_lista)
# print(resultado) 
# print(lista)


#TODO: *ARGS ==> Son parametros especiales que permiten pasar a la funcion multiples datos en forma de tupla
def suma_numeros(num1,num2,num3,num4,num5,num6):
    return num1 + num2 + num3 + num4 + num5 + num6

resultado = suma_numeros(2,3,4,5,8,10)
#print(resultado)

def suma_args(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

resultado = suma_args(1,4,5,6,7,65,3,567,65,65,1,2,3,4,5,6,3)
#print(resultado)

#TODO: CREAR UNA FUNCION QUE CALCULE EL PERIMETRO
def calcular_perimetro(*args):
    total = 0
    for arg in args:
        total += arg
    return total

resultado = calcular_perimetro(10,30,23,42,53,3)
#print(resultado)

#TODO: EFICIENCIA DE EJECUCION
import  time

def suma_for(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


def suma_sum(lista):
    return sum(lista)

lista = [1,2,3,4,5,6,7,324,235,235,235,253,235,236,236,236,236,326,236,623,324325325326236236236236236236,236236236236236236236236236]

time_inicio = time.time()
resultado_for = suma_for(lista)
time_final = time.time()
time_for = time_final - time_inicio



resultado_sum = suma_sum(lista)


#RESULTADO
print(f"Resultado de la suma for: {resultado_for} en tiempo: {time_for}")
print(resultado_sum)
