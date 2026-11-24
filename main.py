import pygame
import math
from tabla import Tabla
from bola import Bola

pygame.init()

ancho = 1000
alto = 600

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Pool Fisica")

blanco = (255, 255, 255)
reloj = pygame.time.Clock()
mesa = Tabla()

colores = [
    (255, 220, 0),
    (0, 80, 220),
    (220, 30, 30),
    (130, 40, 180),
    (255, 120, 0),
    (30, 150, 50),
    (130, 20, 20),
    (20, 20, 20),
    (255, 220, 0),
    (0, 80, 220),
    (220, 30, 30),
    (130, 40, 180),
    (255, 120, 0),
    (30, 150, 50),
    (130, 20, 20)
]


def crear_partida():

    bola_blanca = Bola(300, 300, blanco)
    bola_blanca.vx = 0
    bola_blanca.vy = 0

    bolas = []

    separacion = 31
    inicio_x = 600
    inicio_y = 300

    contador = 0

    for fila in range(5):
        for columna in range(fila + 1):

            x = inicio_x + fila * separacion
            y = inicio_y + (columna - fila / 2) * separacion

            bola = Bola(x, y, colores[contador])
            bola.vx = 0
            bola.vy = 0

            bolas.append(bola)
            contador += 1

    return bola_blanca, bolas


bola_blanca, bolas = crear_partida()

cargando = False
potencia = 0
potencia_maxima = 600
velocidad_carga = 300

ejecutando = True

while ejecutando:

    dt = min(reloj.tick(60) / 1000, 0.033)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                bola_blanca, bolas = crear_partida() #reinicia
                cargando = False
                potencia = 0

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                rapidez_blanca = math.hypot(
                    bola_blanca.vx,
                    bola_blanca.vy
                )
                bolas_quietas = all(
                    math.hypot(bola.vx, bola.vy) < 1
                    for bola in bolas
                )
                if rapidez_blanca < 1 and bolas_quietas:

                    cargando = True
                    potencia = 0

        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1 and cargando:
                mouse_x, mouse_y = evento.pos
                dx = mouse_x - bola_blanca.x
                dy = mouse_y - bola_blanca.y

                distancia = math.hypot(dx, dy)

                if distancia > 0:
                    direccion_x = dx / distancia
                    direccion_y = dy / distancia
                    bola_blanca.vx = direccion_x * potencia
                    bola_blanca.vy = direccion_y * potencia
                cargando = False
                potencia = 0

    if cargando:
        potencia += velocidad_carga * dt
        potencia = min(potencia, potencia_maxima)

    bola_blanca.frenar(dt)
    bola_blanca.mover(dt)

    if mesa.bola_embocada(bola_blanca):
        bola_blanca.x = 300
        bola_blanca.y = 300
        bola_blanca.vx = 0
        bola_blanca.vy = 0
        cargando = False
        potencia = 0

    else:
        bola_blanca.rebotar(
            ancho,
            alto,
            margen=60
        )

    for bola in bolas[:]:
        bola.frenar(dt)
        bola.mover(dt)
        if mesa.bola_embocada(bola):

            bolas.remove(bola)
        else:

            bola.rebotar(
                ancho,
                alto,
                margen=60
            )

    for bola in bolas:
        bola_blanca.chocar_con(
            bola,
            restitucion=1.0
        )

    for i in range(len(bolas)):
        for j in range(i + 1, len(bolas)):
            bolas[i].chocar_con(
                bolas[j],
                restitucion=1.0
            )

    mesa.dibujar(pantalla)

    pygame.draw.rect(
        pantalla,
        (50, 50, 50),
        (350, 15, 300, 20)
    )

    ancho_potencia = int(
        (potencia / potencia_maxima) * 300
    )

    pygame.draw.rect(
        pantalla,
        (255, 200, 0),
        (350, 15, ancho_potencia, 20)
    )

    rapidez_blanca = math.hypot(
        bola_blanca.vx,
        bola_blanca.vy
    )

    bolas_quietas = all(
        math.hypot(bola.vx, bola.vy) < 1
        for bola in bolas
    )

    if rapidez_blanca < 1 and bolas_quietas:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.line(
            pantalla,
            (255, 255, 255),
            (int(bola_blanca.x), int(bola_blanca.y)),
            (mouse_x, mouse_y),
            2
        )

    bola_blanca.dibujar(pantalla)

    for bola in bolas:
        bola.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()