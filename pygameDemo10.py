# pygame demo 2 - una imagen, clic y movimiento
# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys
import random

# 2 - Definir constantes
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
TEAL = (0, 128, 128)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 200
N_PIXELS_PER_FRAME = 3

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 4 - Cargar activos: imagen(es), sonido(s), etc.
ballImage = pygame.image.load('POO_pygame_Assets-main/images/ball.png')
bounceSound = pygame.mixer.Sound('POO_pygame_Assets-main/sounds/boing.wav')
pygame.mixer.music.load('POO_pygame_Assets-main/sounds/background.mp3')
pygame.mixer.music.set_volume(0.09) # Le bajamos el volumen
pygame.mixer.music.play(-1, 0.0)

# 5 - Inicializamos variables
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH) 
ballY = random.randrange(MAX_HEIGHT) 
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Bucle infinito
while True:
    # 7 - Comprobar y manejar eventos
    for event in pygame.event.get():
        # ¿Se hizo clic en el botón de cierre? Salir de pygame y terminar el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Realizar acciones "por cuadro"
    if (ballX < 0) or (ballX >= MAX_WIDTH): 
        xSpeed = -xSpeed  # dirección contraria X
        bounceSound.play()  # reproducir sonido de rebote
    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed  # dirección contraria Y
        bounceSound.play()  # reproducir sonido de rebote

    # Actualiza la localización de la pelota, usando la velocidad en dos direcciones
    ballX = ballX + xSpeed 
    ballY = ballY + ySpeed

    # 9 - Limpiar la ventana
    window.fill(GRAY)

    # 10 - Dibujar todos los elementos de la ventana
    # Dibujar un cuadrado
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)  # arriba
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)  # izquierda
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)  # derecha
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)  # abajo
    # Dibujar una X en el cuadrado
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)
    # Dibujar un círculo y una circunferencia
    pygame.draw.circle(window, GREEN, (250, 50), 30, 0)  # relleno
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2)  # orilla de 2 pixeles
    # Dibujar un rectángulo relleno y un rectángulo vacío
    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0)  # relleno
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1)  # orilla de 1 pixel
    # Dibujar una elipse rellena y una elipse vacía
    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0)  # relleno
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2)  # orilla de 2 pixeles
    # Dibujar un hexágono
    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350), (410, 410), (350, 470), (240, 470), (170, 410)))

    # Dibujar la imagen de la bola
    window.blit(ballImage, (ballX, ballY))

    # 11 - Actualizar la ventana
    pygame.display.update()

    # 12 - Reducir la velocidad un poco
    clock.tick(FRAMES_PER_SECOND)
