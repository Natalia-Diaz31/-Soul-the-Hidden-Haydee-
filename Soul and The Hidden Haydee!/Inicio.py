import pygame, sys#<--ayuda a cerrar el juego 

def mostrar_inicio(pantalla):
    background = pygame.image.load("inicio.png").convert() #Cargamos la imagen que tendra de fondo
    boton_comenzar = pygame.Rect(300, 656, 430, 120)#Recuadro que interactua con el clic del jugador (x,y,largo,ancho).

    #Esta sección es para que comience el juego si el jugador da clic, o se cierre si el jugador cierra la ventana.
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit() # Sale del juego
            elif event.type == pygame.MOUSEBUTTONDOWN: # Detecta los movimientos e interacciones que estan sucediendo en la pantalla.
                if boton_comenzar.collidepoint(event.pos):
                    esperando = False  

        pantalla.blit(background, (0, 0)) # Establece las coordenadas desde donde se pondra la imagen.

        pygame.display.flip() #Funcion que actualiza constantemente el juego.
