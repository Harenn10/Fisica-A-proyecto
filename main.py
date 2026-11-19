import pygame
from bola import Bola

pygame.init()

ancho = 1000
alto = 600

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Pool Fisica")

verde = (20, 100, 50)
blanco = (255, 255, 255)

reloj = pygame.time.Clock()

bola_blanca = Bola(300, 500, blanco)

ejecutando = True

while ejecutando:

    dt = reloj.tick(60) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    bola_blanca.mover(dt)
    bola_blanca.rebotar(ancho, alto)
    pantalla.fill(verde)
    bola_blanca.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()