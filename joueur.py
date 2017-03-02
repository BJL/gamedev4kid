import pygame

from pygame.locals import *
from bullet import Bullet



""" Classe gerant le joueur """


class Joueur(pygame.sprite.Sprite):
    SPEED = 6

    def __init__(self, (x, y)=(512, 384)):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = []

        for i in range(0, 13):
            if i in [1, 4, 7, 10]:
                self.images.append(pygame.image.load(
                    'images/player_' + str(i + 1) + '.png').convert_alpha())
            self.images.append(pygame.image.load(
                'images/player_' + str(i) + '.png').convert_alpha())

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.AI = 0
        self.animationDuration = 200
        self.rotating = False

    def update(self, keys, moving, elapsed):
        self.animation(keys,elapsed)
        if moving:
            self.move(keys)

    def fire(self,elapsed,v2d):
        Bullet(self.rect.x,self.rect.y,v2d)

    def animation(self,keys,elapsed):
        self.animationDuration -= elapsed
        if (keys[K_RIGHT]):
            self.image = self.images[9 + self.AI]
        elif (keys[K_LEFT]):
            self.image = self.images[13 + self.AI]
        elif (keys[K_DOWN]):
            self.image = self.images[1 + self.AI]
        elif (keys[K_UP]):
            self.image = self.images[5 + self.AI]
        elif (keys[K_SPACE]):
            self.rotating = True
        else:
            if (self.animationDuration < 0):
                self.animationDuration = 200
                self.image = self.images[0]
                self.rotating = False
        if (self.rotating):
            self.image = pygame.transform.rotate(self.image, 90)

        if (self.animationDuration < 0):
            self.animationDuration = 200
            self.AI += 1

        if self.AI > 3: self.AI = 0


    def move(self, keys):
        (x_move, y_move) = (0,0)
        if keys[K_UP]:
            y_move = - Joueur.SPEED
        if keys[K_DOWN]:
            y_move = Joueur.SPEED
        if keys[K_LEFT]:
            x_move = - Joueur.SPEED
        if keys[K_RIGHT]:
            x_move = Joueur.SPEED
        self.rect.move_ip(x_move, y_move)
