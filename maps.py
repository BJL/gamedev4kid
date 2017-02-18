import pygame
import pytmx

from pygame.locals import *
from pytmx.util_pygame import load_pygame
from decor import TiledDecor


class Map():

    def __init__(self):
        self.tiled_map = 0
        print("init")

    def loadTiledMap(self,path='maps/testmap.tmx'):
        self.tiled_map = load_pygame(path)


    def drawMap(self,surface):
        for layer in self.tiled_map.layers:
            if (layer.name == "background"):
                for x, y, image in layer.tiles():
                    surface.blit(image, (x * 64, y * 64))
    def drawObject(self,surface):
        for layer in self.tiled_map.layers:
            if (layer.name == "objets"):
                for obj in layer:
                    TiledDecor(obj.image, obj.x , obj.y)