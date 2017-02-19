import sys
import pygame

from pygame.locals import *
from pygame.gfxdraw import *
from pygame.math import *
from pylab import *

from decor import *
from joueur import *
from enemy import *
from maps import *


# declaration
surfaceW = 1024
surfaceH = 768
tileSize = 64

# initialisation de PyGame
pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Noa & Otis Production")

# groupe de sprites
backgrounds = pygame.sprite.Group()
decors = pygame.sprite.Group()
enemies = pygame.sprite.Group()
joueurs = pygame.sprite.Group()
all = pygame.sprite.LayeredUpdates()

Background.containers = backgrounds,all
Decor.containers = decors,all
Poulpito.containers =  enemies,all
Joueur.containers = joueurs,all

# chargement de la map
map = Map()
map.loadTiledMap()

# chargement des sprites
joueur = Joueur()
Poulpito()
Poulpito()

def enemiesMove(enemies, joueur):
    for enemy in enemies:
        enemyMove(enemy, joueur)


def enemyMove(enemi, joueur):
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

    if (collisionMask(enemi, decors,xMove,0)
        or collisionMask(enemi,joueurs,xMove,0)):
        xMove = 0

    if (collisionMask(enemi, decors,0,yMove)
        or collisionMask(enemi,joueurs,0,yMove)):
        yMove = 0

    enemi.update(xMove, yMove)

def collision(objet, sprites,xMove,yMove):
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


def collisionMask(objet, sprites,xMove,yMove):
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


def principale():
    game_over = False
    pygame.key.set_repeat(10, 10)

    elapsed = 0
    while not game_over:
        elapsed = clock.tick(50)
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

        # gestion des collisions
        if (collisionMask(joueur, decors,x_mouvement,y_mouvement)):
            x_mouvement = 0
            y_mouvement = 0


        joueur.update(keys,x_mouvement, y_mouvement,elapsed)

        enemiesMove(enemies, joueur)

        # dessin du background
        #map.drawMap(surface)
        # dessin des objets avec collision
        #decors.draw(surface)

        #drawSprite(joueur)  # dessin du joueur
        #enemies.draw(surface)  # dessin des enemis
        all.draw(surface)

        pygame.display.update()


principale()
pygame.quit()
quit()
