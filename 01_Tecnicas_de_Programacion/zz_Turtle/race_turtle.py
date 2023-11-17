from turtle import *
from random import randint

#Configuración inicial de la pantalla de Turtle
speed(0)  #Rapidez del movimiento
penup()   # Levanta el lapiz para moverse sin dibujar
goto(-140, 140)    # Mover la tortuga a las coordenadas (-140, 140)

#Dibujar la pista de carrera y colocar las tortugas en el eje X

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
    

#CREAR LOS CORREDORES
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

#POSIBLES SHAPE: 
# arrow (default), circle, square, triangle, classic, dot, oval, image

#Posicionar las tortugas en el punto de partida
red.penup()
red.goto(-160,100)
red.pendown()

blue.penup()
blue.goto(-160, 70)
blue.pendown()

green.penup()
green.goto(-160,40)
green.pendown()

purple.penup()
purple.goto(-160, 10)
purple.pendown()
#Configurar que las tortugas se muevan de forma aleatoria

for turn in range(100):
    red.forward(randint(1,5))
    blue.forward(randint(1,5))
    green.forward(randint(1,7))
    purple.forward(randint(1,5))
    
done()
