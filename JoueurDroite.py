#CREATION 18/01/2022
#PAR DURAISAMY LP RAVI2
import random
import pygame
from pygame.math import Vector2

import core

class JoueurDroite :
    def __init__(self):
        self.rayon = 50
        self.couleur = (255, 255, 255)
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))
        self.nom = "JoueurDroite"
        self.vitesse = 5
        self.direction = Vector2()
        self.vitesseMax = 3


    def deplacer (self,clique):
        core.WINDOW_SIZE = [1200, 800]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            break
        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            break

        def keydown (event):
            global paddle1_vel, paddle2_vel

            if event.key == K_UP:
                paddle2_vel = -8
            elif event.key == K_DOWN:
                paddle2_vel = 8
            elif event.key == K_w:
                paddle1_vel = -8
            elif event.key == K_s:
                paddle1_vel = 8

        # keyup handler
        def keyup (event):
            global paddle1_vel, paddle2_vel

            if event.key in (K_w, K_s):
                paddle1_vel = 0
            elif event.key in (K_UP, K_DOWN):
                paddle2_vel = 0

        init()

    def limit (self):
        core.WINDOW_SIZE = [1200, 800]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            self.direction, Vector2(self.direction.x, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            self.direction, Vector2(self.direction.x * -1, self.direction.y)



    def draw (self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)