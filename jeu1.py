import sys
import random
import pygame

from pygame.locals import *
from pygame.gfxdraw import *
from pygame.math import *
from decor import *
from joueur import *
from enemy import *
from pylab import *


# declaration
blue = (113, 177, 227)
white = (255, 255, 255)  # valeur max = 255

surfaceW = 1024
surfaceH = 768
tileSize = 64
tileMap = zeros((16, 12))
tileArray = range(1, 16 * 12)


def getEmptyTile():
    idx = randint(0, size(tileArray) - 1)
    y = tileArray[idx] / 16 * tileSize
    x = tileArray[idx] % 16 * tileSize
    tileArray.pop(idx)

    return x, y

# initialisation de PyGame
pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Noa & Otis Production")

# chargement des images
joueur = Joueur(getEmptyTile())
enemies = [Poulpito(getEmptyTile()), Poulpito(getEmptyTile())]

bckgnd = pygame.image.load("images/plaineW.png")

decors = [Sapin(getEmptyTile()), Sapin(getEmptyTile()), Sapin(getEmptyTile()), Sapin(getEmptyTile()), Sapin(getEmptyTile()), Sapin(getEmptyTile()), Rocher(getEmptyTile()), Rocher(getEmptyTile()), Rocher(getEmptyTile()), Rocher(getEmptyTile()), Rocher(getEmptyTile()),
          Buisson(getEmptyTile()), Buisson(getEmptyTile()), Buisson(getEmptyTile()), Buisson(getEmptyTile()), Buisson(getEmptyTile()), Buisson(getEmptyTile())]

tombes = [Tombe(getEmptyTile()), Tombe(getEmptyTile()), Tombe(getEmptyTile(
)), Tombe(getEmptyTile()), Tombe(getEmptyTile()), Tombe(getEmptyTile())]
feux = [Feu(getEmptyTile())]


def drawImage(x, y, image):
    surface.blit(image, (x, y))


def drawSprites(sprites):
    for sprite in sprites:
        surface.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
        pygame.gfxdraw.rectangle(surface, sprite.rect, (123, 123, 123))


def drawSprite(sprite):
    surface.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
    pygame.gfxdraw.rectangle(surface, sprite.rect, (123, 123, 123))


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
        xMove = 1
    if (jy - ey > 0):
        yMove = 1
    if (jx - ex < 0):
        xMove = -1
    if (jy - ey < 0):
        yMove = -1

    collX = False
    collY = False
    enemi.update(xMove, 0)
    if (collisionMask(enemi, decors)):
        enemi.update(-xMove, 0)
        collX = True

    enemi.update(0, yMove)
    if (collisionMask(enemi, decors)):
        enemi.update(0, -yMove)
        collY = True


def collision(objet, sprites):
    collision = False
    for sprite in sprites:
        collision = pygame.sprite.collide_rect(objet, sprite)
        if (collision):
            break
    return collision


def collisionMask(objet, sprites):
    collision = False
    for sprite in sprites:
        point = pygame.sprite.collide_mask(objet, sprite)
        if (point != None):
            collision = True
            break

    return collision


def principale():
    game_over = False
    pygame.key.set_repeat(150, 30)

    while not game_over:
        clock.tick(50)
        y_mouvement = 0
        x_mouvement = 0
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or (keys[K_ESCAPE]):
                game_over = True

            if event.type == pygame.KEYDOWN:
                if keys[K_UP]:
                    y_mouvement = - 3
                if keys[K_DOWN]:
                    y_mouvement = 3
                if keys[K_LEFT]:
                    x_mouvement = -3
                if keys[K_RIGHT]:
                    x_mouvement = 3

        # gestion des collisions

        joueur.update(x_mouvement, y_mouvement)
        if (collisionMask(joueur, decors)):
            joueur.update(-x_mouvement, -y_mouvement)

        enemiesMove(enemies, joueur)

        # dessin decors
        drawImage(0, 0, bckgnd)  # dessin background

        drawSprites(decors)
        drawSprites(feux)
        drawSprites(tombes)

        drawSprite(joueur)  # dessin du joueur
        drawSprites(enemies)  # dessin des enemis

        pygame.display.update()

principale()
pygame.quit()
quit()
