import pygame
from Inicio import mostrar_inicio
from Introduccion import mostrar_introduccion
from Juego import jugar_nivel

pygame.init()
pantalla = pygame.display.set_mode((1038, 802))
pygame.display.set_caption("Soul and The Hidden Haydee!")

# Primero mostramos la pantalla de inicio
mostrar_inicio(pantalla)

# Pantalla de introducción (con temporizador)
mostrar_introduccion(pantalla)

# Luego mostramos el juego
jugar_nivel(pantalla)
