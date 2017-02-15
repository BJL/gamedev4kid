import pygame
import random

from pygame.locals import *


class Sapin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/sapin.png')

        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() * 4, self.image.get_height() * 4))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 960 - self.rect.width)
        self.rect.y = random.randint(10, 600 - self.rect.height)
        self.mask = pygame.mask.from_surface(self.image)


class Rocher(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/rocher.png')

        coefficient = random.randint(2, 7)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * coefficient, self.image.get_height() * coefficient))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 960 - self.rect.width)
        self.rect.y = random.randint(10, 600 - self.rect.height)
        self.mask = pygame.mask.from_surface(self.image)


class Feu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/feu.png')

        coefficient = random.randint(2, 3)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * coefficient
            , self.image.get_height() * coefficient))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 960 - self.rect.width)
        self.rect.y = random.randint(10, 600 - self.rect.height)
        self.mask = pygame.mask.from_surface(self.image)


class Tombe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/tombe.png')


        coefficient = random.randint(2, 3)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * coefficient
            , self.image.get_height() * coefficient))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 960 - self.rect.width)
        self.rect.y = random.randint(10, 600 - self.rect.height)
        self.mask = pygame.mask.from_surface(self.image)


class Buisson(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/buisson.png')
        #self.image = pygame.Surface(self.image2.get_size())
        #self.image.fill((113, 177, 227))

        coefficient = random.randint(2, 3)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * coefficient, self.image.get_height() * coefficient))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 960 - self.rect.width)
        self.rect.y = random.randint(10, 600 - self.rect.height)
        self.mask = pygame.mask.from_surface(self.image)
