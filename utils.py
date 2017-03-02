__author__ = 'ben'

from pygame.math import Vector2
from math import cos,sin

def normalVector(vector):
    (r, phi) = vector.as_polar()
    x = r * cos(phi)
    y = r * sin(phi)