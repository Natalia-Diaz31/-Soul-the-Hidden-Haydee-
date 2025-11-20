import pygame, sys

def mostrar_introduccion(pantalla):
    background = pygame.image.load("introduccion.png").convert() # Cargamos la imagen de fondo, "convert" sirve para optimizar el renderizado
    
    duracion = 5000  # duración en milisegundos (5 segundos)
    tiempo_inicio = pygame.time.get_ticks() # Guarda el tiempo actual al iniciar la introducción

    esperando = True # Variable para mantener el bucle activo
    while esperando:
        # Nos sirve para revisar los eventos del sistema (como cerrar la ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pantalla.blit(background, (0, 0))#Pone la imagen de fondo
        pygame.display.flip() # Actualiza la pantalla para mostrar los cambios

        # Sirve para calcular el tiempo actual y ve si ya paso el tiempo que queriamos que transcurriera
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_inicio >= duracion:
            esperando = False #sale del bucle despues de que transcurre el tiempo.