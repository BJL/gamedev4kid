import pygame
import pytmx

from pygame.locals import *
from pytmx.util_pygame import load_pygame
from decor import *


class Map():

    def loadTiledMap(self, path='maps/testmap.tmx'):
        self.tiled_map = load_pygame(path)
        self.loadBackground()
        self.loadObjects()

    def loadBackground(self):
        idx = 0
        for layer in self.tiled_map.layers:
            idx += 1
            if (not layer.name.startswith("objets")):
                for x, y, image in layer.tiles():
                    Background(image, x * 64, y * 64,idx)
                    #surface.blit(image, (x * 64, y * 64))

    def loadObjects(self):
        for layer in self.tiled_map.layers:
            if (layer.name.startswith("objets")):
                for obj in layer:
                    Decor(obj.image, obj.x, obj.y,
                               layer.properties['layer'])
                    #if (obj.properties.get('animated') != None):
                    #    self.getAnimation(obj.gid)

    def getAnimation(self, gid):
        frames = self.tiled_map.get_tile_properties_by_gid(gid)
        for animation_frame in frames['frames']:
            image = self.tiled_map.get_tile_image_by_gid(gid)
            duration = animation_frame.duration
