import sys
import pygame
import pyscroll

from pygame.locals import *
from pygame.gfxdraw import *
from pygame.math import *
from pylab import *

from decor import *
from joueur import *
from enemy import Enemy,Poulpito
from maps import *
from bullet import Bullet


class Jeu:

    # declaration

    def __init__(self):
        # initialisation de PyGame
        self.screenW = 800
        self.screenH = 600
        self.tileSize = 64
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 16)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))
        pygame.display.set_caption("Noa & Otis Production")

        # groupe de sprites
        self.decors = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.joueurs = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        Enemy.containers = self.enemies
        Joueur.containers = self.joueurs
        Bullet.containers = self.bullets


        # chargement de la map
        self.map = Map()
        self.joueur = Joueur()
        self.loadMap("debut cart.tmx")

    def loadMap(self, file,(x,y)=(-1,-1)):
        self.decors.empty()
        self.doors.empty()
        self.enemies.empty()
        self.bullets.empty()
        if (hasattr(self, 'group')):
            self.group.empty()
        self.map.loadTiledMap(self.screenW, self.screenH - 32 , "maps/" + file)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map.map_layer)
        self.group.add(self.joueur, layer=3)

        if (x>=0 and y>=0):
            self.joueur.rect.topleft = (x,y)


        self.group.center(self.joueur.rect.center)

        Decor.containers = self.decors, self.group
        Door.containers = self.doors, self.group
        Bullet.containers = self.bullets,self.group
        self.map.loadObjects()
        self.group.add(self.enemies.sprites(), layer=3)

    def enemiesMove(self, enemies, joueur):
        for enemy in enemies:
            self.enemyMove2(enemy, joueur)

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

    def enemyMove2(self, enemi, joueur):
        vJ = Vector2(joueur.rect.center)
        vE = Vector2(enemi.rect.center)
        vMove = vJ - vE
        xMove = 0
        yMove = 0

        if (vMove.length() > 250):
            return
        if vMove.length() > 3:
            vMove.scale_to_length(3)

        xMove = round(vMove[0])
        yMove = round(vMove[1])

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

    def bulletCollision(self,bullets,objects,doKill1=True,doKill2=True):
        pygame.sprite.groupcollide(bullets,objects,doKill1,doKill2,pygame.sprite.collide_mask)

    def drawLine(self,p,l=3):
        p2 = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()==(1,0,0):
            pygame.draw.line(self.screen,(124,124,124),p,p2,l)

    def drawMenu(self):
        self.screen.fill((0, 0, 0), Rect(0, 568, 800, 32))
        """
        self.screen.blit(self.font.render(
            "FPS : " + str(self.clock.get_fps()), 1,
            pygame.color.THECOLORS['red']), (5, self.screenH - 32))
        """
        self.screen.blit(self.font.render("Weapon : Silver Sword"
                                          , 1, pygame.color.THECOLORS['yellow']), (5, self.screenH - 32))
        self.screen.blit(self.font.render("Experience : 0"
                                          , 1, pygame.color.THECOLORS['yellow']), (5, self.screenH - 18))


    def OutOfBoundaries(self, objet,map, xMove, yMove):
        objet.rect.x += xMove
        objet.rect.y += yMove

        outBound =  not map.rect.contains(objet.rect)

        objet.rect.x -= xMove
        objet.rect.y -= yMove

        return outBound

    def destroyOutOfBoundaries(self,group,map):
        for sprite in group:
            if not map.rect.contains(sprite.rect):
                sprite.kill()

    def calculateVector(self,xTarget,yTarget,xOrigine,yOrigine,xView=0,yView=0):

        vTarget = Vector2(xTarget + xView,
                          yTarget + yView)
        vOrigine = Vector2(xOrigine,yOrigine)

        return vTarget - vOrigine

    def principale(self):
        game_over = False
        pygame.key.set_repeat(10, 10)

        elapsed = 0
        pressTime = 0
        isPressed = False
        while not game_over:
            elapsed = self.clock.tick(50)
            canPlayerMove = True
            y_mouvement = 0
            x_mouvement = 0
            if isPressed and pressTime < 1000:
                pressTime += elapsed

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or (keys[K_ESCAPE]):
                    game_over = True

                if event.type == pygame.KEYDOWN:
                    if keys[K_UP] or keys[K_z]:
                        y_mouvement = - 6
                    if keys[K_DOWN] or keys[K_s]:
                        y_mouvement = 6
                    if keys[K_LEFT] or keys[K_q]:
                        x_mouvement = -6
                    if keys[K_RIGHT] or keys[K_d]:
                        x_mouvement = 6
                    if keys[K_SPACE]:
                        self.enterDoor(self.joueur, self.doors)

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0):
                    isPressed = True
                if event.type == pygame.MOUSEBUTTONUP:
                    isPressed = False
                    v = self.calculateVector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                                         self.joueur.rect.centerx, self.joueur.rect.centery,
                                         self.group.view.x, self.group.view.y)
                    self.joueur.fire(elapsed,v,pressTime)
                    pressTime = 0

            # gestion des collisions et de la taille de l'ecran
            if (self.collisionMask(self.joueur, self.decors, x_mouvement, y_mouvement)
                or  self.OutOfBoundaries(self.joueur,self.map,x_mouvement, y_mouvement)):
                canPlayerMove = False

            self.joueur.update(keys, canPlayerMove, elapsed)
            self.enemiesMove(self.enemies, self.joueur)
            self.bullets.update(elapsed)

            self.bulletCollision(self.bullets,self.enemies)
            self.bulletCollision(self.bullets, self.decors,True,False)


            self.destroyOutOfBoundaries(self.bullets,self.map)
            # dessin des sprites

            self.group.center(self.joueur.rect.center)

            self.group.draw(self.screen)
            self.drawMenu()
            self.drawLine((self.joueur.rect.centerx-self.group.view.x, self.joueur.rect.centery - self.group.view.y),pressTime/100)

            pygame.display.update()

if __name__ == "__main__":
    MainWindow = Jeu()
    MainWindow.principale()
    pygame.quit()
    quit()
