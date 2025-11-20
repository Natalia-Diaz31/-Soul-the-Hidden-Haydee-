import pygame, sys#<--ayuda a cerrar el juego 
def mostrar_inicio(pantalla):
    background = pygame.image.load("inicio.png").convert()
    boton_comenzar = pygame.Rect(300, 656, 430, 120)

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