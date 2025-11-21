import pygame, sys

def mostrar_victoria(pantalla):
    background = pygame.image.load("victoria.png").convert()
    volver_jugar= pygame.Rect(200, 470, 635, 200)

    # Esta sección permite que el jugador pueda seguir jugando después de acertar, o que pueda cerrar el juego.
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if volver_jugar.collidepoint(event.pos):
                    esperando = False  

        pantalla.blit(background, (0, 0))

        pygame.display.flip()

