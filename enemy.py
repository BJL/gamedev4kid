import pygame
import random

from pygame.locals import *

""" Classe gerant les enemiss """

class Poulpito(pygame.sprite.Sprite):

    def __init__(self,x=600,y=200):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/poulpito vert.png')

        coefficient = 1
        self.image = pygame.transform.scale(self.image,(self.image.get_rect().width*coefficient,self.image.get_rect().height*coefficient))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 960 - self.rect.width)
        self.rect.y = random.randint(10, 600 - self.rect.height)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self,x_move,y_move):
    	self.rect.move_ip(x_move,y_move)