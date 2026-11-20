import pygame
from fisicas import actualizar_posicion, rebotar_paredes, aplicar_fricciones

class Bola:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.vx = 200
        self.vy = -150

        self.radio = 15
        self.color = color

    def mover(self, dt):
        self.x, self.y = actualizar_posicion(
            self.x,
            self.y,
            self.vx,
            self.vy,
            dt
        )

    def dibujar(self, pantalla):
        pygame.draw.circle(
            pantalla,
            self.color,
            (int(self.x), int(self.y)),
            self.radio
        )
    def rebotar(self, ancho, alto):

        self.x, self.y, self.vx, self.vy = rebotar_paredes(
            self.x,
            self.y,
            self.vx,
            self.vy,
            self.radio,
            ancho,
            alto
        )
        
    def frenar(self, dt):
        self.vx, self.vy = aplicar_fricciones(
            self.vx,
            self.vy,
            dt
        )