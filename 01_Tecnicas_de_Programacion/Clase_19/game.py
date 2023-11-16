import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Esquiva Obstáculos")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Jugador
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 8

# Obstáculos
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25

obstacles = []

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Función para dibujar al jugador
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_size, player_size])

# Función para dibujar obstáculos
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, white, obstacle)

# Función principal del juego
def game():
    global player_x, obstacles

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player_x -= (keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]) * player_speed

        # Generar obstáculos
        if random.randint(1, obstacle_frequency) == 1:
            obstacle_x = random.randint(0, width - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])

        # Mover obstáculos
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed

        # Eliminar obstáculos fuera de la pantalla
        obstacles = [obstacle for obstacle in obstacles if obstacle[1] < height]

        # Colisión con obstáculos
        for obstacle in obstacles:
            if (
                player_x < obstacle[0] + obstacle[2]
                and player_x + player_size > obstacle[0]
                and player_y < obstacle[1] + obstacle[3]
                and player_y + player_size > obstacle[1]
            ):
                print("¡Perdiste!")
                pygame.quit()
                sys.exit()

        # Limpiar la pantalla
        screen.fill(black)

        # Dibujar jugador y obstáculos
        draw_player(player_x, player_y)
        draw_obstacles(obstacles)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(30)

# Iniciar el juego
game()
