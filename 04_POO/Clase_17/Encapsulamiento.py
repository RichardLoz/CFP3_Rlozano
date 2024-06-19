
#TODO: ENCAPSULAMIENTO: El encapsulamiento es uno de los pilares de la POO. Consiste en ocultar la implementacion interna de un objeto y proporcionar una interfaz con el. De este modo, se controla que información y comportamiento de un objeto son accesibles desde el exterior, protegiendo asi la integridad de los datos y facilitando el mantenimiento de codigo.


#1. Getter: Es un metodo que se utiliza para acceder al valor de un atributo privado desde fuera de la clase. Permite obtener el valor del atributo sin modificarlo, en Python los getters suelen nombrarse con el prefijo get_nombre.

#2. Setter: Son un metodo que se utiliza para modificar el valor de un atributo privado desde fuera de la clase. Permite controlar y validar los cambios que se realizan en el atributo. En Python, los setters suelen nombrarse con el prefijo set_nombre

# __(doble guion bajo): El uso del doble guion bajo indica que ese atributo es privado y no debe ser accedido directamente desde fuera de la clase.

class Usuario:
    def __init__(self,nombre, edad, email, contraseña):
        self.nombre = nombre #Atributo publico
        self.edad = edad    #Atributo publico
        self.email = email  #Atributo publico
        self.__contraseña = contraseña # #Atributo privado
        
        
    #Metodo get-set para obtener el nombre de usuario
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    # Método getter para obtener la edad del usuario
    def get_edad(self):
        return self.edad

    # Método setter para establecer la edad del usuario
    def set_edad(self, edad):
        self.edad = edad
        
    # Método getter para obtener el email del usuario
    def get_email(self):
        return self.email

    # Método setter para establecer el email del usuario
    def set_email(self, email):
        self.email = email
        
    # Método getter para obtener la contraseña del usuario
    def get_contraseña(self):
        return self.__contraseña

    # Método setter para establecer la contraseña del usuario
    def set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña
        
        
    def __str__(self):
        return f"Usuario: {self.nombre}, Edad : {self.edad}, Email: {self.email}"
        

# usuario1 = Usuario("Richard",33,"rlozano@gmail.com", 1234)
# print(usuario1)

# #Usando getter y setter para los atributos publicos
# usuario1.set_nombre("Tomas")
# usuario1.set_edad(19)
# usuario1.set_email("rlozano1@gmail.com")

# print(usuario1.get_nombre())
# print(usuario1.get_edad())
# print(usuario1.get_email())



#TODO: EJERCICIOS:

# Consigna 1: Clase Producto
# Crea una clase Producto que represente un producto en una tienda en línea. La clase debe tener los siguientes atributos privados:

# __nombre: El nombre del producto (cadena de texto).
# __precio: El precio del producto (número decimal).
# __stock: La cantidad de productos disponibles en inventario (número entero).
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre.
# Métodos getter y setter para precio, con una validación en el setter para asegurar que el precio sea positivo.
# Métodos getter y setter para stock, con una validación en el setter para asegurar que el stock sea un número entero no negativo.
# Finalmente, implementa el método __str__ para que al imprimir un objeto de la clase Producto, se muestre la siguiente información:
# Producto: <nombre>, Precio: <precio>, Stock: <stock>

# Consigna 2: Clase Empleado
# Crea una clase Empleado que represente a un empleado en una empresa. La clase debe tener los siguientes atributos privados:

# __nombre: El nombre del empleado (cadena de texto).
# __salario: El salario del empleado (número decimal).
# __departamento: El departamento al que pertenece el empleado (cadena de texto).
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre.
# Métodos getter y setter para salario, con una validación en el setter para asegurar que el salario sea positivo.
# Métodos getter y setter para departamento.
# Además, implementa un método aumentar_salario(porcentaje) que incremente el salario del empleado por un cierto porcentaje. Asegúrate de validar que el porcentaje sea un número positivo.

# Finalmente, implementa el método __str__ para que al imprimir un objeto de la clase Empleado, se muestre la siguiente información:
# Empleado: <nombre>, Salario: <salario>, Departamento: <departamento>


#TODO: Consigna 3: Clase Curso
# Crea una clase Curso que represente un curso en una plataforma educativa. La clase debe tener los siguientes atributos privados:

# __nombre_curso: El nombre del curso (cadena de texto).
# __instructor: El nombre del instructor del curso (cadena de texto).
# __estudiantes: Una lista que contenga los nombres de los estudiantes inscritos en el curso.
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre_curso.
# Métodos getter y setter para instructor.
# Un método getter para obtener la lista de estudiantes get_estudiantes().
# Un método agregar_estudiante(estudiante) que añada un estudiante a la lista de estudiantes.
# Un método remover_estudiante(estudiante) que elimine un estudiante de la lista de estudiantes si existe en la lista.
# Un método listar_estudiantes() que devuelva una cadena con todos los nombres de los estudiantes inscritos, separados por comas.
# Un método __str__ para representar el objeto como una cadena que muestre el nombre del curso y el nombre del instructor.

# class Producto:
#     def __init__(self, nombre, precio, stock):
#         self.__nombre = nombre
#         self.__precio = precio
#         self.__stock = stock

#     # Getter y Setter para nombre
#     def get_nombre(self):
#         return self.__nombre

#     def set_nombre(self, nombre):
#         self.__nombre = nombre

#     # Getter y Setter para precio
#     def get_precio(self):
#         return self.__precio

#     def set_precio(self, precio):
#         if precio > 0:
#             self.__precio = precio
#         else:
#             print("El precio debe ser un número positivo.")

#     # Getter y Setter para stock
#     def get_stock(self):
#         return self.__stock

#     def set_stock(self, stock):
#         if isinstance(stock, int) and stock >= 0:
#             self.__stock = stock
#         else:
#             print("El stock debe ser un número entero no negativo.")

#     # Método __str__ para representación en cadena
#     def __str__(self):
#         return f'Producto: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}'

# # Uso de la clase Producto
# p1 = Producto("Laptop", 1500.0, 5)
# print(p1)  # Producto: Laptop, Precio: 1500.0, Stock: 5

# p1.set_precio(1400.0)
# print(p1.get_precio())  # 1400.0

# p1.set_stock(10)
# print(p1.get_stock())  # 10




# class Empleado:
#     def __init__(self, nombre, salario, departamento):
#         self.__nombre = nombre
#         self.__salario = salario
#         self.__departamento = departamento

#     # Getter y Setter para nombre
#     def get_nombre(self):
#         return self.__nombre

#     def set_nombre(self, nombre):
#         self.__nombre = nombre

#     # Getter y Setter para salario
#     def get_salario(self):
#         return self.__salario

#     def set_salario(self, salario):
#         if salario > 0:
#             self.__salario = salario
#         else:
#             print("El salario debe ser un número positivo.")

#     # Getter 
#     # y Setter para departamento
#     def get_departamento(self):
#         return self.__departamento

#     def set_departamento(self, departamento):
#         self.__departamento = departamento

#     # Método para aumentar el salario
#     def aumentar_salario(self, porcentaje):
#         if porcentaje > 0:
#             self.__salario += self.__salario * (porcentaje / 100)
#         else:
#             print("El porcentaje debe ser positivo.")

#     # Método __str__ para representación en cadena
#     def __str__(self):
#         return f'Empleado: {self.__nombre}, Salario: {self.__salario}, Departamento: {self.__departamento}'

# # Uso de la clase Empleado
# e1 = Empleado("Juan Perez", 3000.0, "IT")
# print(e1)  # Empleado: Juan Perez, Salario: 3000.0, Departamento: IT

# e1.aumentar_salario(10)
# print(e1.get_salario())  # 3300.0

# e1.set_departamento("HR")
# print(e1.get_departamento())  # HR




class Curso:
    def __init__(self, nombre_curso, instructor):
        self.__nombre_curso = nombre_curso
        self.__instructor = instructor
        self.__estudiantes = []

    # Getter y Setter para nombre_curso
    def get_nombre_curso(self):
        return self.__nombre_curso

    def set_nombre_curso(self, nombre_curso):
        self.__nombre_curso = nombre_curso

    # Getter y Setter para instructor
    def get_instructor(self):
        return self.__instructor

    def set_instructor(self, instructor):
        self.__instructor = instructor

    # Getter para la lista de estudiantes
    def get_estudiantes(self):
        return self.__estudiantes

    # Método para agregar un estudiante
    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    # Método para remover un estudiante
    def remover_estudiante(self, estudiante):
        if estudiante in self.__estudiantes:
            self.__estudiantes.remove(estudiante)
        else:
            print(f"El estudiante {estudiante} no está inscrito en el curso.")

    # Método para listar los estudiantes
    def listar_estudiantes(self):
        return ", ".join(self.__estudiantes)

    # Método __str__ para representación en cadena
    def __str__(self):
        return f'Curso: {self.__nombre_curso}, Instructor: {self.__instructor}'

# Uso de la clase Curso
curso = Curso("Base de Datos", "Prof. Lozano")
print(curso)  # Curso: Matemáticas, Instructor: Prof. Gomez

curso.agregar_estudiante("Milagros")
curso.agregar_estudiante("Jesica")
print(curso.get_estudiantes())  

curso.remover_estudiante("Bryan")
curso.agregar_estudiante("Richard")
curso.agregar_estudiante("Tomas")
print(curso.listar_estudiantes())  # Bob

curso.set_nombre_curso("Programacion Python")
print(curso.get_nombre_curso())  # Matemáticas Avanzadas