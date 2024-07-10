
#TODO: POO
# 1. Abstracción: Proceso de ocultar los detalles complejos de un objeto del mundo exterior. Representar en codigo los objetos del mundo real.
# 2. Herencia: Mecanismo por el cual una clase padre hereda sus propiedades y metodos a una clase hija.
# 3. Encapsulamiento: Restricción del acceso directo a los datos de objeto y su manipulación a través de métodos. (get - set)
# 4. Polimorfismo: Capacidad de diferentes clases de ser tratadas cmo instancias de una misma clase mediante una interfaz comun.

# ========================================================

#TODO: POLIMORFISMO: Se refiere a la capacidad de los objetos de diferentes clases para ser tratados como objetos de una clase comun. Es decir, diferentes clases pueden definir métodos que se llaman igual, pero que tienen comportamientos diferentes. En Python el Polimorfismo se logra principalmente a través de la Herencia.



class Animal:
    def hacer_sonido(self):
        return "Este metodo debe ser implentado por las clases hijas"
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu"
    
perro = Perro()
gato = Gato()
vaca = Vaca()

# print(perro.hacer_sonido())
# print(gato.hacer_sonido())
# print(vaca.hacer_sonido())
    
# def imprimir_sonido(animal):
#     print(animal.hacer_sonido())

# imprimir_sonido(perro)
# imprimir_sonido(gato)
# imprimir_sonido(vaca) 
  


#TODO: EJERCICIOS FIGURAS GEOMETRICAS
# Apartir de una clase padre "Figura" definir un metodo "calcular_area" que debe ser implementado por todas las clases hijas (Rectangulo, Circulo, Triangulo). Cada subclase que implementa el metodo "calcular_area" debe devolver el resultado de la formula aplicada para cada caso.
#TODO: FORMULAS 
#Rectangulo = B * A
#Circulo = PI * (radio ** 2)
#Triangulo = (B * A) / 2

import math
class Figura:
    def calcular_area(self):
        return "Este metodo debe ser implementado por las clases hijas"
    
class Rectangulo(Figura):
    def __init__(self,base,alto):
        self.base = base
        self.alto = alto
        
    def calcular_area(self):
        return self.base * self.alto

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
class Triangulo(Figura):
    def __init__(self,base,alto):
        self.base = base
        self.alto = alto
    
    def calcular_area(self):
        return (self.base * self.alto) / 2
    
def imprimir_area(figura):
    print(f"El area de la figura es: {figura.calcular_area()}")
    
# rectangulo = Rectangulo(10,20)
# circulo = Circulo(10)
# triangulo = Triangulo(10,20)

# figuras = [rectangulo, circulo, triangulo]

# for figura in figuras:
#     imprimir_area(figura)

# imprimir_area(rectangulo)
# imprimir_area(circulo)
# imprimir_area(triangulo)
# print(rectangulo.calcular_area())
# print(circulo.calcular_area())
# print(triangulo.calcular_area())

#TODO: Una empresa nos solicita un programa que les permita gestionar los empleados. 
# Tipos de empleados: Tiempo Completo, Medio Tiempo, Freelance
# Debemos poder calcular sus salarios y gestionar una lista de todos sus empleados

#1- Clases y Herencia
    # - Crear una clase base "Empleado" con los siguientes atributos y metodos:
    # ATRIBUTOS: nombre(privado) , id_empleado(privado)
    # Metodos: __init__ , calcular_salario, get y set, __str__

#2- Subclases:
    # - EmpleadoTiempoCompleto(Empleado)
        #- Atributo: salario_mensual(privado)
        #- Metodo: calcular_salario()
    # - EmpleadoMedioTiempo(Empleado)
        #- Atributo: salario_por_hora(privado), horas_trabajadas(privado)
        #- Metodo: calcular_salario()
    # - EmpleadoFreelance(Empleado)
        #- Atributo: tarifa_proyecto(privado)
        #- Metodo: calcular_salario()

#3- Gestion de Empleados
    # - class GestionEmpleados
        # - Atributo: lista_empleados
    # - Metodos:
        # - agregar_empleado()
        # - agregar_varios_empleados()
        # - eliminar_empleado_por_id()
        # - mostrar_empleados()
        #- calcular_salarios() : Calcular y devolver la suma de todos los salarios de todos los empleados de la lista
        # - __str__ : Una representación en cadena de la lista de nombres de empleados





class Empleado:
    def __init__(self,nombre,id_empleado):
        self.__nombre = nombre
        self.__id_empleado = id_empleado
    
    def calcular_salario(self):
        pass
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self):
        return self.__nombre
    
    def get_id_empleado(self):
        return self.__id_empleado
    
    def set_id_empleado(self):
        return self.__id_empleado
    
    def __str__(self):
        return f"ID:{self.__id_empleado} - Nombre: {self.__nombre}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self,nombre,id_empleado,salario_mensual):
        super().__init__(nombre,id_empleado)
        self.__salario_mensual = salario_mensual
    
    def calcular_salario(self):
        return self.__salario_mensual

class EmpleadoMedioTiempo(Empleado):
    def __init__(self,nombre,id_empleado,salario_por_hora,horas_trabajadas):
        super().__init__(nombre,id_empleado)
        self.__salario_por_hora = salario_por_hora
        self.__horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        return self.__salario_por_hora * self.__horas_trabajadas
    

class EmpleadoFreelance(Empleado):
    def __init__(self,nombre,id_empleado,tarifa_proyecto):
        super().__init__(nombre, id_empleado)
        self.__tarifa_proyecto = tarifa_proyecto
        
    def calcular_salario(self):
        return self.__tarifa_proyecto
    
class GestionEmpleados:
    def __init__(self):
        self.lista_empleados = []
        
    def agregar_empleado(self, empleado):
        self.lista_empleados.append(empleado)
    
    def agregar_varios_empleados(self, *empleados):
        for empleado in empleados:
            self.agregar_empleado(empleado)

    def eliminar_empleado_por_id(self,id_empleado):
        self.lista_empleados = [emp for emp in self.lista_empleados if emp.get_id_empleado() != id_empleado]
        
    def mostrar_empleados(self):
        for emp in self.lista_empleados:
            print(emp)
            
    def calcular_salarios_totales(self):
        return sum(emp.calcular_salario() for emp in self.lista_empleados)
    
tomas = EmpleadoTiempoCompleto("Tomas",1,1800000)
mila = EmpleadoMedioTiempo("Milagros",2,1000,90)
jesi = EmpleadoFreelance("Jesica",3,280000)
bryan = EmpleadoFreelance("Bryan",4,280000)

gestion = GestionEmpleados()


gestion.agregar_varios_empleados(tomas,mila,jesi,bryan)
print("Lista de empleados")
gestion.mostrar_empleados()

print("Salarios Totales")
print(gestion.calcular_salarios_totales())