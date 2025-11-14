import random

def logica_sencilla(nivel_actual, puntaje_actual): 
    
    numero_puertas = 3 + (nivel_actual - 1)
    
    posicion_haydee = random.randint(1, numero_puertas)

    print(f" Nivel {nivel_actual} (lógica sencilla)")
    print(f"Hay {numero_puertas} puertas frente a ti...")
    print(f"Las puertas se abren un momento... Haydee esta {posicion_haydee} ")
    print("Las puertas se cierran nuevamente...")
    
    while True: 
        eleccion = input(f"Elige una puerta (1 a {numero_puertas}): ")
        try: 
            eleccion = int(eleccion)
            if 1 <= eleccion <= numero_puertas:

                break
            else:
                print("Numero fuera de rango. Intenta otra vez.")
        except ValueError:
            print("Debes escribir un numero valido.")
            
    gano = (eleccion == posicion_haydee)
    
    if gano:
        print("¡Encontraste a Haydee!")
        puntaje_actual += 10
    else:
        print("No encontraste a Haydee :( ")
        puntaje_actual -= 5
    return gano, puntaje_actual


def logica_con_odurn(nivel_actual, puntaje_actual):
    numero_puertas = 3 + (nivel_actual - 1)
    
    posicion_haydee = random.randint(1, numero_puertas)
    
    while True: 
        posicion_odurn = random.randint(1, numero_puertas)
        if posicion_odurn != posicion_haydee: 
            break
        
        
    print(f"Nivel {nivel_actual} (Modo Odurn)")
    print(f"Hay {numero_puertas} puertas frente a ti")
    
    if nivel_actual == 4:
        print("Odurn ha entrado al juego... se esconde detras de una puerta.")
    else:
        print("La presencia de Odurn es mucho mas fuerte en este nivel... ")
        print("Algo oscuro se mueve detras de varias puertas...")
        
        
    print(f"Haydee esta en la puerta {posicion_haydee}")
    print(f"Odurn esta en la puerta {posicion_odurn}")
    print("Las puertas se cierran... recuerda bien.")
    
    while True: 
        eleccion = input(f"Elige una puerta (1 a {numero_puertas}): ")
        try: 
            eleccion = int(eleccion)
            if 1 <= eleccion <= numero_puertas:
                break
            else: 
                print("Elige un numero dentro del rango.")
        except ValueError:
            print("Debes escribir un numero valido.")
            
    if eleccion == posicion_haydee:
        gano = True
        print("¡Lograste esquivar a Odurn y encontraste a Haydee!")
    else:
        gano = False
        if eleccion == posicion_odurn:
            print("¡Elegiste la puerta de Odurn!")
        else:
            print("Esa puerta esta vacia... ¡Odurn te alcanza!")
            
    if gano: 
        if nivel_actual == 4:
            puntaje_actual += 15
        else: 
            puntaje_actual+=30 
    else:
        if nivel_actual == 4:
            puntaje_actual -= 10
        else:
            puntaje_actual -= 20
            
    return gano, puntaje_actual

nivel = 1
puntaje = 0

while nivel <= 5:
    print(f"Nivel actual: {nivel} | Puntaje: {puntaje}")
    
    if nivel <= 3: 
        gano, puntaje = logica_sencilla(nivel, puntaje)
        
    if nivel >= 4:
        
        gano, puntaje = logica_con_odurn(nivel, puntaje)
        
    if gano:
        nivel += 1
    else:
        nivel = 1 
print("¡Felicidades, ganaste el juego! FIN")
