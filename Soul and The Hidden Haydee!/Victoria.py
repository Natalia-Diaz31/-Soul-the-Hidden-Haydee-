import pygame, sys

def mostrar_victoria(pantalla):
    background = pygame.image.load("victoria.png").convert()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                esperando = False

        pantalla.blit(background, (0, 0))
        pygame.display.flip()