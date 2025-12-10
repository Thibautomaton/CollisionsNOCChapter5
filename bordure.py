import pygame.draw

from settings import *
from Box2D.b2 import polygonShape


class Bordure():
    def __init__(self, x, y, w, h, world):

        self.x = x
        self.y=y
        self.w = w
        self.h = h

        self.display_surface = pygame.display.get_surface()

        self.body = world.CreateStaticBody(
            position = pixelsToWorld((self.x, self.y)),
            userData=self
        )

        box2DW = scalarPixelsToWorld(self.w/2)
        box2DH = scalarPixelsToWorld(self.h/2)

        ps = polygonShape(
            box = (box2DW, box2DH)
        )

        self.body.CreateFixture(
            shape = ps,
            friction = 0.3,
            density = 0.5,
            restitution = 0.5
        )

    def display(self):
        color = (0, 255, 0)
        pygame.draw.polygon(self.display_surface, color, [(self.x - self.w/2, self.y-self.h/2), (self.x +self.w/2, self.y-self.h/2), (self.x+self.w/2, self.y+self.h/2), (self.x -self.w/2, self.y+self.h/2)])

