import pygame, sys

# Esta función permitirá mostrar una pequeña introducción al juego.

def mostrar_introduccion(pantalla):
    background = pygame.image.load("introduccion.png").convert() # Carga de la imagen de fondo.

    # Esta sección de código permite dejar la imagen de la introducción unos segundos.
    duracion = 5000  # Duración en milisegundos (5 segundos)
    tiempo_inicio = pygame.time.get_ticks() # Guarda el tiempo actual al iniciar la introducción

    esperando = True # Variable para mantener el bucle activo
    while esperando:
        # Revisa los eventos del sistema (como cerrar la ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pantalla.blit(background, (0, 0)) # Pone la imagen de fondo
        pygame.display.flip() # Actualiza la pantalla para mostrar los cambios

        # Calcula el tiempo transcurrido y revisa si ya pasaron los 5 segundos.
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_inicio >= duracion:

            esperando = False # Finaliza el bucle una vez transcurrido el tiempo.
