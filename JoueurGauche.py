#CREATION 18/01/2022
#PAR DURAISAMY LP RAVI2
import random
import pygame
from pygame.math import Vector2

import core

class JoueurGAUCHE :
    def __init__(self):
        self.couleur = (255, 255, 255)
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))
        self.nom = "JoueurGAUCHE"
        self.vitesse = 5
        self.direction = Vector2()
        self.vitesseMax = 3

        self.L = Vector2(0, 0)
        self.l = 0
        self.lo = 10
        self.Ux = 0
        self.Fx = 0



    def deplacer (self,clique):
        core.WINDOW_SIZE = [1200, 800]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            self.position = Vector2(600,0)
        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            self.position = Vector2(0,400)

        if clique is not None:
            self.Ux = Vector2(clique) - self.position
            self.l= self.Ux.length()
            self.Ux= self.Ux.normalize()
            self.L= abs(self.l - self.lo)
            self.Fx= 0.00004 * self.L * self.Ux
            self.direction= self.direction + self.Fx


    def limit (self):
        core.WINDOW_SIZE = [1200, 800]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            self.direction, Vector2(self.direction.x, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            self.direction, Vector2(self.direction.x * -1, self.direction.y)

    def draw (self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
