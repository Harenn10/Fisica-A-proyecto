import pygame

class Tabla:

    def __init__(self):

        self.izquierda = 60
        self.derecha = 940
        self.arriba = 60
        self.abajo = 540

        self.verde = (20, 110, 60)
        self.madera = (100, 55, 25)
        self.negro = (0, 0, 0)

        self.troneras = [
            (60, 60),
            (500, 60),
            (940, 60),
            (60, 540),
            (500, 540),
            (940, 540)
        ]

    def dibujar(self, pantalla):

        pantalla.fill(self.madera)

        pygame.draw.rect(
            pantalla,
            self.verde,
            (
                self.izquierda,
                self.arriba,
                self.derecha - self.izquierda,
                self.abajo - self.arriba
            )
        )

        for x, y in self.troneras:
            pygame.draw.circle(
                pantalla,
                self.negro,
                (x, y),
                25
            )

    def bola_embocada(self, bola):
        for x, y in self.troneras:
            dx = bola.x - x
            dy = bola.y - y
            distancia = (dx**2 + dy**2)**0.5
            if distancia < 22:
                return True #si la distancia es menor que 22 pixeles entra
        return False