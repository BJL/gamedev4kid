import pygame
import random

from pygame.locals import *

""" Classe gerant les enemiss """

class Poulpito(pygame.sprite.Sprite):

    def __init__(self,(x,y)=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/poulpito rose mechant.png')

        coeff = 0.5
        self.image = pygame.transform.scale(self.image,(int(self.image.get_rect().width * coeff)
            ,int(self.image.get_rect().height * coeff) ))
        self.rect = self.image.get_rect()
        if (x ==0 and y==0):
            self.rect.x = random.randint(20, 960 - self.rect.width)
            self.rect.y = random.randint(10, 600 - self.rect.height)
        else:
            self.rect.x = x
            self.rect.y = y
        self.rect.x = random.randint(20, 960 - self.rect.width)
        self.rect.y = random.randint(10, 600 - self.rect.height)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self,x_move,y_move):
    	self.rect.move_ip(x_move,y_move)