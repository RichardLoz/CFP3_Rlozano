
#TODO: FUNCIONES ANIDADAS: Las funciones pueden ser anidadas, es decir una funcion puede contener a otra funcion.

#TODO: EJEMPLO: OPERACIONES BANCARIAS: Deposito, Retiro
 
def operacion():
    
    def deposito(cantidad, balance):
        return balance + cantidad
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None, "No tiene saldo suficiente para esta operacion"
    print(deposito(800, 400))
    print(retiro(200, 500))
    
#operacion()


#TODO: Agregar a la funcion anterior la opcion de especificar el tipo de operacion que se desea realizar, en el caso de no especificar una, tomar el valor deposito como default.
def operacion(cantidad, balance, tipo='deposito' ):
    
    def deposito(cantidad, balance):
        return balance + cantidad
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None, "No tiene saldo suficiente para esta operacion"
        
    if tipo == 'deposito':
        return deposito(cantidad,balance)
    elif tipo == 'retiro':
        return retiro(cantidad,balance)
        
    
resultado = operacion(100,300,tipo='retiro')
#print(resultado)



#TODO: Escribir una funcion calculadora que reciba 2 numeros y un caracter que indique el tipo de operacion a realizar (+, - , *, /). La funcion debe devolver el resultado de la operacion aritmetica. Utilizar funciones anidadas para implementar las operaciones. La operacion por default sera suma.

def calculadora(num1, num2, operacion='+'):
    
    def suma(num1, num2):
        return num1+num2
    
    def resta(num1, num2):
        return num1-num2
    
    def multiplicacion(num1, num2):
        return num1*num2
    
    def division(num1, num2):
        return num1 / num2
    
    if operacion == '+':
        return suma(num1,num2)
    elif operacion == '-':
        return resta(num1,num2)
    elif operacion == '*':
        return multiplicacion(num1,num2)
    elif operacion == '/':
        return division(num1, num2)
    else:
        return "Signo invalido"

resultado_suma = calculadora(20,30) 
resultado_resta = calculadora(20,30,'-') 
resultado_multi = calculadora(20,30,'*')  
resultado_divi = calculadora(20,30,'/') 
resultado_signo = calculadora(20,30,'%')
print(resultado_suma)
print(resultado_resta)
print(resultado_multi)
print(resultado_divi)
print(resultado_signo)





