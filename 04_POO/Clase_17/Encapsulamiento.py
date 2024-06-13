
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

