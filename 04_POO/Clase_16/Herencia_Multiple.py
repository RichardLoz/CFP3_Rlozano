
#TODO: HERENCIA MULTIPLE

class ClaseA:
    def metodo_a(self):
        return "Metodo de ClaseA"
    
class ClaseB:
    def metodo_b(self):
        return "Metodo de ClaseB"
    
class ClaseDerivada(ClaseA, ClaseB):
    def metodo_derivada(self):
        return "Metodo de ClaseDerivada"

objetoDeri = ClaseDerivada()

#TODO: Llamar a los metodos de las clases padre
# print(objetoDeri.metodo_a()) # ==> Salida: Metodo Clase A
# print(objetoDeri.metodo_b()) # ==> Salida: Metodo Clase B
# print(objetoDeri.metodo_derivada()) # ==> Salida: Metodo Clase Derivada

#TODO: CONSIGNA: MEDIANTE EL USO DE HERENCIA MULTIPLE REPRESENTAR DISTINTOS TIPOS DE VEHICULOS, PARA COMBINAR LAS CARACTERISTICAS DE TIPOS DE VEHICULOS.
#Clase Padre
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Inicialización del objeto Vehiculo con marca, modelo y año
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False  # Estado inicial del vehículo (apagado)

    def encender(self):
        # Método para encender el vehículo
        self.encendido = True
        print("El vehículo está encendido.")

    def apagar(self):
        # Método para apagar el vehículo
        self.encendido = False
        print("El vehículo está apagado.")

    def descripcion(self):
        # Método para obtener la descripción del vehículo
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas, tipo_combustible):
        # Llama explícitamente al constructor de Vehiculo con marca, modelo y año
        super().__init__(marca, modelo, año)
        # Inicialización de atributos específicos de Auto
        self.puertas = puertas
        self.tipo_combustible = tipo_combustible

    def conducir(self):
        # Método específico de Auto para conducir
        print("Conduciendo el auto.")

    def descripcion(self):
        # Sobrescribe el método de Vehiculo para agregar más detalles de Auto
        return f"{super().descripcion()}, Puertas: {self.puertas}, Combustible: {self.tipo_combustible}"


class Avion(Vehiculo):
    def __init__(self, marca, modelo, año, alas, tipo_motor):
        # Llama explícitamente al constructor de Vehiculo con marca, modelo y año
        super().__init__(marca, modelo, año)
        # Inicialización de atributos específicos de Avion
        self.alas = alas
        self.tipo_motor = tipo_motor

    def volar(self):
        # Método específico de Avion para volar
        print("Volando el avión.")

    def descripcion(self):
        # Sobrescribe el método de Vehiculo para agregar más detalles de Avion
        return f"{super().descripcion()}, Alas: {self.alas}, Motor: {self.tipo_motor}"


class VehiculoAmfibio(Auto, Avion):
    def __init__(self, marca, modelo, año, puertas, tipo_combustible, alas, tipo_motor, capacidad_agua):
        # Llama explícitamente al constructor de Auto y Avion para inicializa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.puertas = puertas
        self.tipo_combustible = tipo_combustible
        self.alas = alas
        self.tipo_motor = tipo_motor
        self.capacidad_agua = capacidad_agua

    def navegar(self):
        # Método específico de VehiculoAmfibio para navegar
        print("Navegando el vehículo anfibio.")

    def descripcion(self):
        # Sobrescribe el método de Auto para incluir todos los detalles de VehiculoAmfibio
        return f"{Auto.descripcion(self)}, Capacidad de Agua: {self.capacidad_agua} litros"

# Crear una instancia de VehiculoAmfibio
vehiculo_anfibio = VehiculoAmfibio("Amphico", "Model X", 2023, 4, "Híbrido", 2, "Turbojet", 500)

# Llamar a métodos de las clases base y de la clase derivada
print(vehiculo_anfibio.descripcion())  # Imprime la descripción detallada del vehículo anfibio


