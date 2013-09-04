

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
ACC = 30


#images 
CHERRY_PIC = pygame.image.load("cherry.png")
CHERRY = pygame.transform.scale(CHERRY_PIC,(ACC,ACC))

HEAD_PIC = pygame.image.load("snake.png")
IMAGE = pygame.transform.scale(HEAD_PIC, (32,32))
HEAD_S = pygame.transform.scale(HEAD_PIC, (ACC,ACC))

BODY_PIC = pygame.image.load("body.png")
BODY = pygame.transform.scale(BODY_PIC,(ACC,ACC))


#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LTBLUE = (0,255,255)
ORANGE = (255,150,0)
YELLOW = (255,255,0)
