# Importar el módulo Turtle y la función randint desde el módulo random
from turtle import *
from random import randint

# Configuración inicial de la pantalla de Turtle
speed(0)  # Configura la velocidad de dibujo a la máxima (0), sin animación
penup()   # Levanta el lápiz para moverse sin dibujar
goto(-140, 140)  # Mueve la tortuga a las coordenadas (-140, 140)

# Dibuja la pista y coloca los números en el eje X
for step in range(15):
    write(step, align="center")  # Escribe el número actual en el centro
    right(90)  # Gira la tortuga 90 grados a la derecha
    forward(10)  # Mueve la tortuga hacia adelante 10 unidades
    pendown()   # Baja el lápiz para comenzar a dibujar
    forward(150)  # Dibuja la línea de la pista
    penup()     # Levanta el lápiz para moverse sin dibujar
    backward(160)  # Retrocede para prepararse para el próximo número
    left(90)    # Gira la tortuga 90 grados a la izquierda
    forward(20)  # Mueve la tortuga hacia adelante 20 unidades
# Crear cuatro tortugas de colores diferentes
red = Turtle()
red.color("red")
red.shape("turtle")

blue = Turtle()
blue.color("blue")
blue.shape("turtle")

green = Turtle()
green.color("green")
green.shape("turtle")

purple = Turtle()
purple.color("purple")
purple.shape("turtle")

# Configurar la posición inicial de la tortuga roja
red.penup()  # Levanta el lápiz para no dibujar al moverse
red.goto(-160, 100)  # Mueve la tortuga roja a las coordenadas (-160, 100)
red.pendown()  # Baja el lápiz para prepararse para dibujar (aunque no dibuja en este caso)

# Configurar la posición inicial de la tortuga azul
blue.penup()  # Levanta el lápiz para no dibujar al moverse
blue.goto(-160, 70)  # Mueve la tortuga azul a las coordenadas (-160, 70)
blue.pendown()  # Baja el lápiz para prepararse para dibujar (aunque no dibuja en este caso)

# Configurar la posición inicial de la tortuga verde
green.penup()  # Levanta el lápiz para no dibujar al moverse
green.goto(-160, 40)  # Mueve la tortuga verde a las coordenadas (-160, 40)
green.pendown()  # Baja el lápiz para prepararse para dibujar (aunque no dibuja en este caso)

# Configurar la posición inicial de la tortuga morada
purple.penup()  # Levanta el lápiz para no dibujar al moverse
purple.goto(-160, 10)  # Mueve la tortuga morada a las coordenadas (-160, 10)
purple.pendown()  # Baja el lápiz para prepararse para dibujar (aunque no dibuja en este caso)

# Hacer que las tortugas se muevan de forma aleatoria durante 100 turnos
for turn in range(100):
    red.forward(randint(1, 5))   # Mueve la tortuga roja hacia adelante de forma aleatoria
    blue.forward(randint(1, 5))  # Mueve la tortuga azul hacia adelante de forma aleatoria
    green.forward(randint(1, 5)) # Mueve la tortuga verde hacia adelante de forma aleatoria
    purple.forward(randint(1, 5))# Mueve la tortuga morada hacia adelante de forma aleatoria

# Finalizar la ventana de Turtle
done()