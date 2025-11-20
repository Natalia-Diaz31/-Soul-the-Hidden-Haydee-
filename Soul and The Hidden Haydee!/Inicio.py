import pygame, sys #<--ayuda a cerrar el juego 
def mostrar_inicio(pantalla):
    background = pygame.image.load("inicio.png").convert()
    boton_comenzar = pygame.Rect(300, 656, 430, 120)
# Esta sección de código genera un bucle que se reinicia cuando el jugador vuelve a acceder a la pantalla de inicio, 
    # ya sea saliendo del juego y volviendo a entrar, o dándole clic a la pantalla para empezar a jugar.
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_comenzar.collidepoint(event.pos):
                    esperando = False  # Solo salimos si se hace clic en el botón

        pantalla.blit(background, (0, 0))
        pygame.display.flip()

"""
#Esta sección de código establece las medidas de la ventana de inicio 
tamaño=(1038,802)
pantalla=pygame.display.set_mode(tamaño)

#Esta sección de código mostrará título en la ventana de inicio
pygame.display.set_caption("Soul and The Hidden Haydee!")
fuente = pygame.font.SysFont(None, 60) #Fuente del texto

# Esta sección de código carga la imagen de la pantalla en la memoria
background=pygame.image.load("inicio.png").convert()

boton_comenzar = pygame.Rect(300, 656, 430, 120)
"""

