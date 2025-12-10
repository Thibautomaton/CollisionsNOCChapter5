# This is a sample Python script.
import sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import Box2D
from settings import *
from bordure import Bordure
from Particle import Particle
import random
from contactListener import MyContactListener

pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collisions handling")


clock = pygame.time.Clock()

world = Box2D.b2World(gravity = (0, -10), doSleep=False)

world.contactListener  = MyContactListener()

bordures = []

bordures.append(Bordure(WIDTH/2, HEIGHT*9/10, WIDTH*3/4, 50, world))

particles = []

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    world.Step(STEP, 6, 2)
    display_surface.fill((0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        particles.append(Particle(x, y, random.uniform(5, 25), world))

    for b in bordures:
        b.display()

    for p in particles:
        p.update()
        p.display()
        if p.isDead():
            world.DestroyBody(p.body)
    particles = [p for p in particles if not p.isDead()]

    clock.tick(TARGET_FPS)

    pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
