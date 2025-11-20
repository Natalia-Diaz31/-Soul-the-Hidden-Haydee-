import pygame, random, sys

def jugar_nivel(pantalla):
# Para puntaje
    fuente = pygame.font.SysFont(None, 60) # declaramos la fuente y el tamaño
    puntaje = 0

# Configuramos la pantalla 
    pantalla = pygame.display.set_mode((1038, 802))
    pygame.display.set_caption("Soul and The Hidden Haydee!")

#Imagenes
    background = pygame.image.load("puertaspixel.png").convert()# Imagen de fondo
#cargamos las imagenes que se van a sobreponer en la imagen del fondo para simular una animación
    puerta_abierta = pygame.image.load("puerta_abierta.png").convert_alpha() 
    puerta_haydee = pygame.image.load("puerta_haydee.png").convert_alpha()

# Declaramos las medidas que tienen las puertas, para que el jugador pueda hacer clic sobre estas y generar una interacción.

    puerta1 = pygame.Rect(85, 212, 205, 380)
    puerta2 = pygame.Rect(416, 212, 205, 380)
    puerta3 = pygame.Rect(748, 212, 205, 380)

    puertas = [puerta1, puerta2, puerta3]

    """# Para establacer las medidas antereriores dibujamos rectagulos en la pantalla para verificar que las coordenas estaban correctas o irlas modificando.
    #pygame.draw.rect(pantalla, (255, 0, 0), puerta1, 3)
    #pygame.draw.rect(pantalla, (255, 0, 0), puerta2, 3)
    #pygame.draw.rect(pantalla, (255, 0, 0), puerta3, 3)
    """

# Elegimos de manera aleatoria que puerta sera en donde estara Haydee
    correcta = random.randint(0, 2)

#Estado: todas cerradas al inicio 
    abiertas = [False, False, False]

#Bucle principal 
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # estas tres lineas de codigo nos ayudan a poder cerrar la ventana
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, puerta in enumerate(puertas):
                    if puerta.collidepoint(event.pos):
                        abiertas[i] = True  # Se abre esta

                        #Aumentamos o disminuimos el puntaje 
                        if i == correcta:
                            puntaje += 1
                        else:
                            puntaje -= 1

        pantalla.blit(background, (0, 0))

        # ---- Dibujar puertas abiertas si corresponde ----
        for i, puerta in enumerate(puertas):
            if abiertas[i]:
                if i == correcta:
                    # Centrar imagen de Haydee y subirla un poco
                    rect_haydee = puerta_haydee.get_rect(center=puerta.center)
                    rect_haydee.y -= 22  # Ajuste vertical de la imagen
                    pantalla.blit(puerta_haydee, rect_haydee)
                else:
                    # Centrar imagen de puerta abierta
                    rect_abierta = puerta_abierta.get_rect(center=puerta.center)
                    rect_abierta.y -= 22  # Ajuste vertical de la imagen
                    pantalla.blit(puerta_abierta, rect_abierta)
        
        # Establecimos el texto del puntaje en la pantalla
        texto = fuente.render(str(puntaje), True, (255, 255, 0))
        pantalla.blit(texto, (950, 20))# coordenadas de donde estara el puntaje

        pygame.display.flip()