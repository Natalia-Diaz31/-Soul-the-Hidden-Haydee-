import pygame, random, sys
import Perdiste # Importamos el archivo de Perdiste.py
import Victoria

def jugar_nivel(pantalla):
# Esta sección de código establece el puntaje y la forma en que aparece en pantalla.
    fuente = pygame.font.SysFont(None, 60) 
    puntaje = 0

# Configuración de la pantalla.
    pantalla = pygame.display.set_mode((1038, 802))
    pygame.display.set_caption("Soul and The Hidden Haydee!")

# Esta sección de código es para todo lo relacionado a las imágenes del juego.
    
    background = pygame.image.load("puertaspixel.png").convert() # Esta es la imagen de fondo
    
# Estas líneas son las imágenes del juego en sí, que se sobrepondrán a la imagen del fondo
# para simular una animación.
    puerta_abierta = pygame.image.load("puerta_abierta.png").convert_alpha() 
    puerta_haydee = pygame.image.load("puerta_haydee.png").convert_alpha()

# Aquí se declaran las medidas que tienen las puertas, 
# para que el jugador pueda hacer clic sobre estas y generar una interacción.

    puerta1 = pygame.Rect(85, 212, 205, 380)
    puerta2 = pygame.Rect(416, 212, 205, 380)
    puerta3 = pygame.Rect(748, 212, 205, 380)

    puertas = [puerta1, puerta2, puerta3]

    """
    
    Para establacer las medidas anteriores, se dibujaron rectángulos en la pantalla 
    para verificar que las coordenadas estuvieran correctas o modificarlas de ser necesario.
    
    pygame.draw.rect(pantalla, (255, 0, 0), puerta1, 3)
    pygame.draw.rect(pantalla, (255, 0, 0), puerta2, 3)
    pygame.draw.rect(pantalla, (255, 0, 0), puerta3, 3)
    
    """

# Esta línea de código randomiza la ubicación de Haydee.
    correcta = random.randint(0, 2)

# Esta línea de código hace que todas las puertas estén cerradas al inicio.
    abiertas = [False, False, False]

#Funcion para abrir las puertas al inicio
    def mostrar_puertas_abiertas_inicio():
        pantalla.blit(background, (0, 0))

        for i, puerta in enumerate(puertas):

        # Si es la puerta correcta mostrar a Haydee
            if i == correcta:
                rect_haydee = puerta_haydee.get_rect(center=puerta.center)
                rect_haydee.y -= 22  # Ajuste de posición de Haydee
                pantalla.blit(puerta_haydee, rect_haydee)

        # Si no es la correcta mostrar puerta abierta vacía
            else:
                rect_abierta = puerta_abierta.get_rect(center=puerta.center)
                rect_abierta.y -= 22  # Ajuste de posición de puerta abierta
                pantalla.blit(puerta_abierta, rect_abierta)

        pygame.display.flip()  # Actualizar pantalla
        pygame.time.delay(1000)  # Esperar un segundo antes de continuar


# Llamar a la animación inicial de puertas abiertas
    mostrar_puertas_abiertas_inicio()
    abiertas = [False, False, False]  # Estado de puertas cerradas después de la animación
    
# Bucle principal 
    running = True
    while running:
        
        # Esta sección es específica por si el jugador cierra la ventana del juego.
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            # Esta sección es para abrir las puertas si el jugador da clic en ellas.
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, puerta in enumerate(puertas):
                    if puerta.collidepoint(event.pos):
                        abiertas[i] = True  

                        # Aquí aumenta o disminuye el puntaje dependiendo si el jugador acierta o falla.
                        if i == correcta:
                            puntaje += 1

                            # Esta pate muestra a Haydee en la puerta correcta antes de reiniciar
                            rect_haydee = puerta_haydee.get_rect(center=puertas[i].center)
                            rect_haydee.y -= 22
                            pantalla.blit(background, (0, 0))
                            for j, p in enumerate(puertas):
                                if abiertas[j]:
                                    if j == correcta:
                                        pantalla.blit(puerta_haydee, rect_haydee)
                                    else:
                                        rect_abierta = puerta_abierta.get_rect(center=p.center)
                                        rect_abierta.y -= 22
                                        pantalla.blit(puerta_abierta, rect_abierta)
                            texto = fuente.render(str(puntaje), True, (255, 255, 0))
                            pantalla.blit(texto, (950, 20))
                            pygame.display.flip()

                            pygame.time.delay(800)  # Hace una pausa para que se vea Haydee
                        
                        # Al sumar un punto, se reinician las puertas y se podrá elegir una nueva.
                            abiertas = [False, False, False]
                            correcta = random.randint(0, 2)
                            #Vuelve a mostrar las puertas abiertas al reiniciar el juego
                            mostrar_puertas_abiertas_inicio()
                            abiertas = [False, False, False]

                            # Si llega a 5 puntos saldrá la pantalla de Victoria.
                            if puntaje >= 5:
                                Victoria.mostrar_victoria(pantalla)

                                # Reinicia el juego para volver a jugar
                                puntaje = 0
                                abiertas = [False, False, False]
                                correcta = random.randint(0, 2)
                                mostrar_puertas_abiertas_inicio()  # animación inicial de puertas

                        else:
                            Perdiste.mostrar_perdiste(pantalla) # Aquí se llama a la pantalla de perdiste.
                            puntaje=0 # reiniciamos el puntaje
                            abiertas = [False, False, False]  # cerramos puertas
                            correcta = random.randint(0, 2)   # nueva puerta correcta
                            
                            mostrar_puertas_abiertas_inicio()
                            abiertas = [False, False, False]


        pantalla.blit(background, (0, 0))

        # Dibuja puertas abiertas si corresponde
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
        
        # Aquí se estableció el texto del puntaje obtenido y sus coordenadas.
        texto = fuente.render(str(puntaje), True, (255, 255, 0))
        pantalla.blit(texto, (950, 20))

        pygame.display.flip()


