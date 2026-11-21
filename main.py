import pygame
import math
from tabla import Tabla
from bola import Bola

pygame.init()

ancho = 1000
alto = 600

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Pool Fisica")

verde = (20, 100, 50)
blanco = (255, 255, 255)

reloj = pygame.time.Clock()

mesa = Tabla()

bola_blanca = Bola(300, 300, blanco)
bola_blanca.vx = 200
bola_blanca.vy = 0

amarillo = (255, 220, 0)
bola_amarilla = Bola(450, 320, amarillo)
bola_amarilla.vx = 0
bola_amarilla.vy = 0

ejecutando = True

while ejecutando:

    dt = reloj.tick(60) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
    ##FISICAS
    bola_blanca.frenar(dt)
    bola_blanca.mover(dt)
    bola_blanca.rebotar(ancho, alto, margen=60)
    bola_amarilla.frenar(dt) ##FISICAS
    bola_amarilla.mover(dt)
    bola_amarilla.rebotar(ancho, alto, margen=60)
    bola_blanca.chocar_con(bola_amarilla, restitucion=1.0)
    ##FISICAS
    
    mesa.dibujar(pantalla)
    bola_blanca.dibujar(pantalla)
    bola_amarilla.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()