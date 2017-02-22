import sys
import pygame
import pyscroll

from pygame.locals import *
from pygame.gfxdraw import *
from pygame.math import *
from pylab import *

from decor import *
from joueur import *
from enemy import *
from maps import *


class Jeu:

    # declaration

    def __init__(self):
        # initialisation de PyGame
        self.screenW = 800
        self.screenH = 600
        self.tileSize = 64
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption("Noa & Otis Production")

        # groupe de sprites
        self.decors = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.joueurs = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()

        Poulpito.containers = self.enemies
        Joueur.containers = self.joueurs


        # chargement de la map
        self.map = Map()
        self.joueur = Joueur()
        Poulpito()
        Poulpito()
        self.loadMap("testmap2.tmx")

    def loadMap(self, file,(x,y)=(-1,-1)):
        self.decors.empty()
        self.doors.empty()
        if (hasattr(self, 'group')):
            self.group.empty()
        self.map.loadTiledMap(self.screenW, self.screenH, "maps/" + file)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map.map_layer)
        self.group.add(self.joueur, layer=3)

        if (x>=0 and y>=0):
            self.joueur.rect.topleft = (x,y)


        self.group.center(self.joueur.rect.center)
        self.group.add(self.enemies.sprites(), layer=3)
        Decor.containers = self.decors, self.group
        Door.containers = self.doors, self.group
        self.map.loadObjects()

    def enemiesMove(self, enemies, joueur):
        for enemy in enemies:
            self.enemyMove(enemy, joueur)

    def enemyMove(self, enemi, joueur):
        (jx, jy) = joueur.rect.center
        (ex, ey) = enemi.rect.center
        vJ = Vector2(joueur.rect.center)
        vE = Vector2(enemi.rect.center)
        d = vJ.distance_to(vE)
        if (d > 250):
            return
        xMove = 0
        yMove = 0

        if (jx - ex > 0):
            xMove = 3
        if (jy - ey > 0):
            yMove = 3
        if (jx - ex < 0):
            xMove = -3
        if (jy - ey < 0):
            yMove = -3

        if (self.collisionMask(enemi, self.decors, xMove, 0)
                or self.collisionMask(enemi, self.joueurs, xMove, 0)):
            xMove = 0

        if (self.collisionMask(enemi, self.decors, 0, yMove)
                or self.collisionMask(enemi, self.joueurs, 0, yMove)):
            yMove = 0

        enemi.update(xMove, yMove)

    def enterDoor(self, objet, sprites):
        door = pygame.sprite.spritecollideany(objet, sprites)
        if (door != None):
            self.loadMap(door.target,(door.targetX,door.targetY))


    def collision(self, objet, sprites, xMove, yMove):
        collision = False

        objet.rect.x += xMove
        objet.rect.y += yMove
        for sprite in sprites:
            collision = pygame.sprite.collide_rect(objet, sprite)
            if (collision):
                break

        objet.rect.x -= xMove
        objet.rect.y -= yMove
        return collision

    def collisionMask(self, objet, sprites, xMove, yMove):
        collision = False

        objet.rect.x += xMove
        objet.rect.y += yMove
        for sprite in sprites:
            point = pygame.sprite.collide_mask(objet, sprite)
            if (point != None):
                collision = True
                break

        objet.rect.x -= xMove
        objet.rect.y -= yMove
        return collision

    def principale(self):
        game_over = False
        pygame.key.set_repeat(10, 10)

        elapsed = 0
        while not game_over:
            elapsed = self.clock.tick(50)
            y_mouvement = 0
            x_mouvement = 0
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or (keys[K_ESCAPE]):
                    game_over = True

                if event.type == pygame.KEYDOWN:
                    if keys[K_UP]:
                        y_mouvement = - 6
                    if keys[K_DOWN]:
                        y_mouvement = 6
                    if keys[K_LEFT]:
                        x_mouvement = -6
                    if keys[K_RIGHT]:
                        x_mouvement = 6
                    if keys[K_SPACE]:
                        self.enterDoor(self.joueur, self.doors)

            # gestion des collisions
            if (self.collisionMask(self.joueur, self.decors, x_mouvement, y_mouvement)):
                x_mouvement = 0
                y_mouvement = 0

            self.joueur.update(keys, x_mouvement, y_mouvement, elapsed)
            self.enemiesMove(self.enemies, self.joueur)

            # dessin des sprites
            self.group.center(self.joueur.rect.center)
            self.group.draw(self.screen)

            pygame.display.update()

if __name__ == "__main__":
    MainWindow = Jeu()
    MainWindow.principale()
    pygame.quit()
    quit()
