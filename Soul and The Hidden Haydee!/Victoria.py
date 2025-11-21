import pygame, sys

def mostrar_victoria(pantalla):
    background = pygame.image.load("victoria.png").convert()
    volver_jugar= pygame.Rect(200, 470, 635, 200)

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if volver_jugar.collidepoint(event.pos):
                    esperando = False  # Solo salimos si se hace clic en el botón

        pantalla.blit(background, (0, 0))
        pygame.display.flip()