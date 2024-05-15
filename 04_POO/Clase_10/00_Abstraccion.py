
#TODO: Representar un objeto del mundo real en codigo Python

class Animal():
    def __init__(self,habitad,especie,alas):
        self.habitad = habitad
        self.especie = especie
        self.alas = alas
        
    def __str__(self):
        return f'El habitad del animal es {self.habitad}'
    
    
#TODO: STR : Es un metodo especial en Python que se utiliza para devolver una representación de cadena legible para humanos. Es una forma clara y legible de representar el estado interno de un objeto a los usuarios. Al utilizar __str__ podemos personalizar completamente la salida del objeto, mostrando solo la información relevante que queremos mostrar.

animal1 = Animal("terrestre", "canina", False)
print(animal1)