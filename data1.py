

import pygame

from pygame.locals import *

from sys import exit


ZERO = 0
WIDTH = 640
HEIGHT = 480
N = 5


HALF_W = WIDTH/2
HALF_H = HEIGHT/2
SCREEN_SIZE = (WIDTH, HEIGHT)

SPEED = 250
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_SIZE),0,32)
VEL = [5,0]
ACC = 24


#images 
CHERRY = pygame.image.load("cherry.png")
CHERRY = pygame.transform.scale(CHERRY,(ACC,ACC))
REDBALL = pygame.image.load("redball.png")
IMAGE = pygame.transform.scale(REDBALL, (32,32))
IMAGE1 = pygame.transform.scale(REDBALL, (20,20))


#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LTBLUE = (0,255,255)
ORANGE = (255,150,0)
YELLOW = (255,255,0)
