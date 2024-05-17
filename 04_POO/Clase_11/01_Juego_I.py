
#TODO:Creacion de clase Personaje
class Personaje:
    def __init__(self,nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print("Nombre: ", self.nombre)
        print("Fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defensa: " , self.defensa)
        print("Vida: ", self.vida)
        
    def subir_nivel(self,fuerza, inteligencia, defensa,vida):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        self.vida = self.vida + vida
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(f"{self.nombre} esta muerto")
        
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
        #return f"El daño causado por {self.nombre} es de {self.fuerza - enemigo.defensa} al rival {enemigo.nombre}"
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f"{self.nombre} ha realizado {daño} puntos al rival {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es de {enemigo.vida}")
        else:
            enemigo.morir()
        

# jesica = Personaje("Jesica", 70, 50, 45, 700)
# print("Personaje Nivel 1")
# jesica.atributos()
# jesica.subir_nivel(20,15,15,200)
# print("\n")
# print("Personaje Nivel 2")
# jesica.atributos()
# # print(jesica.esta_vivo())

# # #Crear enemigo
# print("\n")
# roberto = Personaje("Roberto",75,60,50,800)
# roberto.atributos()

# # #Metodo atacar
# print("\n")
# print(jesica.atacar(roberto))
# print(roberto.atributos())
# roberto.atacar(jesica)
# print(jesica.atributos())

class Guerrero(Personaje):
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,espada):
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.espada = espada
        
    # Metodo que nos permite seleccionar un arma
    def cambiar_arma(self):
        tipo_arma = int(input("""
                              Seleccione el tipo de arma:
                              1- Doran - daño 12
                              2- Filo Infinito - daño 70
                              3- Sanguinaria - daño 80
                              4- Espadon - daño 100
                              """
                              ))
        #Logica al elegir el arma.
        if tipo_arma == 1:
            self.espada = 12
        elif tipo_arma == 2:
            self.espada = 70
        elif tipo_arma == 3:
            self.espada = 80
        elif tipo_arma == 4:
            self.espada = 100
        else:
            print("Opción no valida")
        
    def atributos(self):
        super().atributos()
        print(f"Espada: {self.espada}")
        
    #Sobreescribir el metodo daño, ya que incorporamos una accesorio al guerrero
    def daño(self,enemigo):
        return self.fuerza + self.espada - enemigo.defensa
        
        
roberto = Guerrero("Roberto",100,80,60,600,2)
roberto.atributos()
roberto.cambiar_arma()
jesica = Personaje("Jesica", 100, 89, 100,800)
roberto.atacar(jesica)
print("\n")
jesica.atributos()

