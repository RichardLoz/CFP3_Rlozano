
#TODO: ENCAPSULAMIENTO: El encapsulamiento es uno de los pilares de la Programación Orientada a Objetos (POO). Consiste en ocultar la implementación interna de un objeto y proporcionar una interfaz pública para interactuar con él. De este modo, se controla qué información y comportamiento de un objeto son accesibles desde el exterior, protegiendo así la integridad de los datos y facilitando el mantenimiento del código.

#TODO: EJEMPLOS:

#Ejemplo 1: Celular
# Cuando usas una aplicación en el teléfono, como la cámara, no necesitas saber cómo funciona internamente la cámara. Solo necesitas saber cómo usar la interfaz que te proporciona la aplicación: abrir la cámara, enfocar, y tomar una foto. Todo el procesamiento interno, como ajustar el enfoque y guardar la imagen, está encapsulado dentro del teléfono y la aplicación. Así, la complejidad interna está oculta, y tú interactúas con una interfaz sencilla.

# Ejemplo 2: Cajero Automático
# Cuando insertas tu tarjeta y seleccionas retirar dinero, no necesitas conocer los detalles internos de cómo el cajero verifica tu saldo, autoriza la transacción, y dispensa el dinero. Solo usas la interfaz del cajero: insertar la tarjeta, introducir tu PIN, seleccionar la cantidad a retirar, y recibir el dinero. Los detalles internos de la verificación y la dispensación del dinero están encapsulados dentro del sistema del cajero automático, proporcionándote una interfaz fácil de usar mientras mantiene la seguridad y la integridad del proceso.

# Getters (Métodos get)
# Los getters son métodos que se utilizan para acceder al valor de un atributo privado desde fuera de la clase. Permiten obtener el valor del atributo sin modificarlo. En Python, los getters suelen nombrarse con el prefijo get_ seguido del nombre del atributo.

# Setters (Métodos set)
# Los setters son métodos que se utilizan para modificar el valor de un atributo privado desde fuera de la clase. Permiten controlar y validar los cambios que se realizan en el atributo. En Python, los setters suelen nombrarse con el prefijo set_ seguido del nombre del atributo.

# __ (Doble Guión Bajo)
# El uso de doble guión bajo al inicio de un nombre de atributo o método en Python indica que este es privado y no debe ser accedido directamente desde fuera de la clase. Esta convención ayuda a encapsular y proteger los datos y métodos internos de la clase. Python implementa el "name mangling" (mangling de nombres) para estos atributos, lo que significa que renombra el atributo de forma interna para que sea difícil acceder a él desde fuera de la clase.


class Usuario:
    def __init__(self, nombre, edad, email, contraseña):
        self.nombre = nombre  # Atributo público
        self.edad = edad      # Atributo público
        self.email = email    # Atributo público
        self.__contraseña = contraseña  # Atributo privado

    # Método getter para obtener el nombre del usuario
    def get_nombre(self):
        return self.nombre

    # Método setter para establecer el nombre del usuario
    def set_nombre(self, nombre):
        self.nombre = nombre

    # Método getter para obtener la edad del usuario
    def get_edad(self):
        return self.edad

    # Método setter para establecer la edad del usuario
    def set_edad(self, edad):
        if edad > 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo.")

    # Método getter para obtener el email del usuario
    def get_email(self):
        return self.email

    # Método setter para establecer el email del usuario
    def set_email(self, email):
        if "@" in email:
            self.email = email
        else:
            print("Email no válido.")

    # Método getter para obtener la contraseña del usuario
    def get_contraseña(self):
        return self.__contraseña

    # Método setter para establecer la contraseña del usuario
    def set_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) >= 6:  # Ejemplo de validación
            self.__contraseña = nueva_contraseña
        else:
            print("La contraseña debe tener al menos 6 caracteres.")

    # Método para representar el objeto como una cadena
    def __str__(self):
        return f'Usuario: {self.nombre}, Edad: {self.edad}, Email: {self.email}'

# Uso de la clase Usuario
usuario1 = Usuario("Alice", 30, "alice@example.com", "secreta123")
print(usuario1)  # Salida: Usuario: Alice, Edad: 30, Email: alice@example.com

# # Usando getters y setters para los atributos públicos
# usuario1.set_nombre("Alicia")
# usuario1.set_edad(31)
# usuario1.set_email("alicia@example.com")

# print(usuario1.get_nombre())  # Salida: Alicia
# print(usuario1.get_edad())    # Salida: 31
# print(usuario1.get_email())   # Salida: alicia@example.com

# # Uso de métodos getter y setter para el atributo privado
# print(usuario1.get_contraseña())  # Salida: secreta123
# usuario1.set_contraseña("nueva123")
# print(usuario1.get_contraseña())  # Salida: nueva123

# # Intento de establecer una contraseña no válida
# usuario1.set_contraseña("abc")  # Salida: La contraseña debe tener al menos 6 caracteres.

#print(usuario1.__contraseña)


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