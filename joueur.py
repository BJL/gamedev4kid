import pygame
import sys

from pygame.locals import *


""" Classe gerant le joueur """


class Joueur(pygame.sprite.Sprite):

    def __init__(self, (x, y)=(512, 384)):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images = []

        for i in range(0, 13):
            if i in [1,4,7,10]:
                self.images.append(pygame.image.load('images/player_' + str(i +1) + '.png'))
            self.images.append(pygame.image.load('images/player_' + str(i) + '.png'))


        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.AI = 0
        self.animationDuration = 200
        self.rotating = False

    def update(self,keys, x_move, y_move, elapsed):
        self.animationDuration -= elapsed
        if (keys[K_RIGHT]):
            self.image = self.images[9+ self.AI]
        elif (keys[K_LEFT]):
            self.image = self.images[13 + self.AI]
        elif (keys[K_DOWN]):
            self.image = self.images[1+ self.AI]
        elif (keys[K_UP]):
            self.image = self.images[5+ self.AI]
        elif (keys[K_SPACE]):
            self.rotating = True
        else:
            if (self.animationDuration < 0):
                self.animationDuration = 200
                self.image = self.images[0]
                self.rotating = False
        if (self.rotating):
            self.image = pygame.transform.rotate(self.image,90)

        if (self.animationDuration < 0):
            self.animationDuration = 200
            self.AI += 1

        if self.AI > 3:self.AI = 0
        self.rect.move_ip(x_move, y_move)
