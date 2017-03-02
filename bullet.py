__author__ = 'ben'

import pygame
from math import cos,sin

from pygame.locals import *

""" Classe gerant les projectils """

class Bullet(pygame.sprite.Sprite):

    SPEED = 50

    def __init__(self,x,y,v2d, image_file='images/swordSilver.png'):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = pygame.image.load(image_file).convert_alpha()
        (r,phi) = v2d.as_polar()
        if v2d.length() > Bullet.SPEED:
            v2d.scale_to_length(Bullet.SPEED)
        self.image = pygame.transform.rotate(self.image, -phi)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.v2d = v2d


    def update(self,elapsed):
        self.rect.move_ip(self.v2d[0],self.v2d[1])
