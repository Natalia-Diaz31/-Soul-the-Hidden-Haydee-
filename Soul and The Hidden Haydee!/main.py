import pygame
from Inicio import mostrar_inicio
from Juego import jugar_nivel
from Victoria import mostrar_victoria

pygame.init()
pantalla = pygame.display.set_mode((1038, 802))
pygame.display.set_caption("Soul and The Hidden Haydee!")

# Primero mostramos la pantalla de inicio
mostrar_inicio(pantalla)

# Luego mostramos el juego
jugar_nivel(pantalla)

# Finalmente mostramos la pantalla de victoria
mostrar_victoria(pantalla)