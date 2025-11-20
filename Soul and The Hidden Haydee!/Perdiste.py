import pygame, sys#<--ayuda a cerrar el juego 
def mostrar_perdiste(pantalla):
    background = pygame.image.load("perdiste.png").convert()
    volver_jugar = pygame.Rect(200, 470, 635, 200)#Rectángulo del botón donde se dara clic  x, y, alto, ancho

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