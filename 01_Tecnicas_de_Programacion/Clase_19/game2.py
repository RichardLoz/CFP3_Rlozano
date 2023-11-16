import pygame
import sys
#Inicializar Pygame
pygame.init()

width , height = 800, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mi primer juego")

#Color de fondo
bg_color = (235, 224 ,3 )

# Coordenadas del centro de la ventana:
center_x, center_y = width // 2 , height // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # LOGICA DEL JUEGO
    window.fill(bg_color)
    
    #Dibujar estrella
    pygame.draw.line(window, (6, 7, 3), (center_x, center_y -50), (center_x, center_y + 50),2)
    pygame.draw.line(window, (6, 7, 3), (center_x -50, center_y), (center_x +50, center_y),2)
    pygame.draw.line(window, (6, 7, 3), (center_x -40 , center_y -40), (center_x +40, center_y + 40),2)
    pygame.draw.line(window, (6, 7, 3), (center_x -40, center_y +40), (center_x +40, center_y -40),2)
    
    pygame.display.flip()
    #COntrol de velocidad del bucle
    pygame.time.Clock().tick(60)