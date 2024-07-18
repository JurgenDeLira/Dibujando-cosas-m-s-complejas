# pygame demo 2 - replicar la portada del álbum "90125" de Yes
# 1 - Importar paquetes
import pygame
from pygame.locals import *
import sys

# 2 - Definir constantes
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30

# 3 - Inicializar el mundo
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Bucle infinito
while True:
    # 5 - Comprobar y manejar eventos
    for event in pygame.event.get():
        # ¿Se hizo clic en el botón de cierre? Salir de pygame y terminar el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 6 - Limpiar la ventana
    window.fill(WHITE)

    # 7 - Dibujar todos los elementos de la ventana
    # Dibujar el fondo gris del círculo
    pygame.draw.circle(window, GRAY, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 200)

    # Dibujar los segmentos de color (ajustados a la forma de la portada original)
    pygame.draw.polygon(window, YELLOW, [(320, 140), (450, 320), (320, 320)])
    pygame.draw.polygon(window, RED, [(320, 140), (190, 320), (320, 320)])
    pygame.draw.polygon(window, BLUE, [(320, 500), (450, 320), (320, 320)])
    pygame.draw.polygon(window, GREEN, [(320, 500), (190, 320), (320, 320)])

    # Dibujar el contorno del círculo
    pygame.draw.circle(window, BLACK, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 200, 5)

    # 8 - Actualizar la ventana
    pygame.display.update()

    # 9 - Reducir la velocidad un poco
    clock.tick(FRAMES_PER_SECOND)

