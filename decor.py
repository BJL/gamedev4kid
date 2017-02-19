import pygame

from pygame.locals import *

class Decor(pygame.sprite.Sprite):
    def __init__(self,image,x,y,layer=0):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.layer = layer

class Background(pygame.sprite.Sprite):
    def __init__(self,image,x,y,layer=0):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.layer = layer
