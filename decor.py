import pygame
import random

from pygame.locals import *


decorGroup = pygame.sprite.Group()

class TiledDecor(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.add(decorGroup)

class Decor(pygame.sprite.Sprite):
    def __init__(self,path,x=0,y=0,minCoeff=1,maxCoeff=3):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        coeff = random.randint(minCoeff, maxCoeff)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * coeff, self.image.get_height() * coeff))
        self.rect = self.image.get_rect()
        if (x ==0 and y==0):
            self.rect.x = random.randint(20, 960 - self.rect.width)
            self.rect.y = random.randint(10, 600 - self.rect.height)
        else:
            self.rect.x = x
            self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)


class Sapin(Decor):
    def __init__(self,(x,y)=(0,0)):
        Decor.__init__(self,'images/sapin.png',x,y)

class Rocher(Decor):
    def __init__(self,(x,y)=(0,0)):
        Decor.__init__(self,'images/rocher.png',x,y)

class Feu(Decor):
    def __init__(self,(x,y)=(0,0)):
        Decor.__init__(self,'images/feu.png',x,y)

class Tombe(Decor):
    def __init__(self,(x,y)=(0,0)):
        Decor.__init__(self,'images/tombe.png',x,y)

class Buisson(Decor):
    def __init__(self,(x,y)=(0,0)):
        Decor.__init__(self,'images/buisson.png',x,y,2,3)
