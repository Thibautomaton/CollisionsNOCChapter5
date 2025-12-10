import pygame.display
from settings import *
from Box2D.b2 import circleShape


class Particle():
    def __init__(self, x, y, r, world):
        self.x = x
        self.y = y
        self.radius = r

        self.lifespan = 1000

        self.color = (175, 175, 175)
        self.border = (255, 0, 0)

        self.markedFD  = False

        self.display_surface = pygame.display.get_surface()

        self.body = world.CreateDynamicBody(
            position = pixelsToWorld((self.x, self.y)),
            userData = self
        )

        cs = circleShape(
            radius = scalarPixelsToWorld(self.radius)
        )

        self.body.CreateFixture(
            shape = cs,
            friction = 0.3,
            density = 0.3,
            restitution = 0.7
        )

    def display(self):



        pygame.draw.circle(self.display_surface, self.color, worldToPixels(self.body.transform.position), self.radius)
        pygame.draw.circle(self.display_surface, self.border, worldToPixels(self.body.transform.position), self.radius, 2)


    def isDead(self):
        return self.lifespan<0 or self.markedFD

    def update(self):
        self.lifespan-=1









