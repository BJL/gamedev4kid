import pygame

from pygame.locals import *


""" Classe gerant le joueur """

class Joueur(pygame.sprite.Sprite):

    def __init__(self,x=480,y=300):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/mechant chevalier.png')

        coeff = 1
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*coeff,self.image.get_height()*coeff))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,x_move,y_move):
    	self.rect.move_ip(x_move,y_move)