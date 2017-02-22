import pygame
import pytmx
import pyscroll

from pygame.locals import *
from pytmx.util_pygame import load_pygame
from decor import *


class Map():

    def loadTiledMap(self,screen_w=800,screen_h=600,path='maps/testmap2.tmx'):
        self.tiled_map = load_pygame(path)
        self.map_data = pyscroll.TiledMapData(self.tiled_map)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, (screen_w,screen_h),clamp_camera=True)

        return self.map_layer

    def loadObjects(self):
        for obj in self.tiled_map.objects:
            if obj.type == "PORTE":
                Door(obj.image, obj.x, obj.y,obj.properties['target'],int(obj.properties['target.x'])*64,int(obj.properties['target.y'])*64)
            else:
                Decor(obj.image, obj.x, obj.y)
