

import pygame

from pygame.locals import *
import os 
from sys import exit


ZERO = 0
WIDTH = 640
HEIGHT = 480
N = 5

pygame.mixer.init()
HALF_W = WIDTH/2
HALF_H = HEIGHT/2
SCREEN_SIZE = (WIDTH, HEIGHT)

SPEED = 250
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_SIZE),0,32)
VEL = [5,0]
ACC = 32
FONT = 'freesansbold.ttf'
#VERDANA ='/usr/share/fonts/truetype/msttcorefonts/Verdana.ttf'
#VERDANA = 'pic/Verdana_Bold_Italic.ttf'
VERDANA = 'pic/Verdana_Bold.ttf'
GAME_NAME  = 'Snake game'
OUT = (-100,0)
RECT  = (200,18)
TIMER  = 20 


#images
#fruits images
FRUITS_PIC = pygame.image.load("pic/fruits_full.png")

P = [FRUITS_PIC.subsurface(Rect(0+i*148,0+j*148,148,148)) for i in range(3) for j in range(3)]

P.pop()

CHERRY_PIC = pygame.image.load("pic/cherry.png")
CHERRY = pygame.transform.scale(CHERRY_PIC,(ACC,ACC))

CHERRY1_PIC = pygame.image.load("pic/cherry1.png")
CHERRY1 = pygame.transform.scale(CHERRY1_PIC,(ACC,ACC))

CHERRY2_PIC = pygame.image.load("pic/cherry2.png")
CHERRY2 = pygame.transform.scale(CHERRY2_PIC,(ACC,ACC))

CHERRYS = [CHERRY,CHERRY1,CHERRY2]
FRUITS = map(lambda x: pygame.transform.scale(x,(40,40)), P)

#snake images
HEAD_PIC = pygame.image.load("pic/snake1.png")
IMAGE = pygame.transform.scale(HEAD_PIC, (32,32))
HEAD_PIC_SCALE = pygame.transform.scale(HEAD_PIC, (ACC,ACC))
HEAD_S = pygame.transform.rotate(HEAD_PIC_SCALE, 270.0)

BODY_PIC = pygame.image.load("pic/body2.png")
BODY = pygame.transform.scale(BODY_PIC,(ACC,ACC))
e = pygame.mixer.Sound("pic/piupiu.wav")
z = pygame.mixer.Sound("pic/zhroon.wav")
pygame.mixer.music.load("pic/move.wav")
GAME_MUSIC = pygame.mixer.Sound('pic/start_screen.wav')
SOUND = pygame.mixer.Sound('pic/alarm.wav')

#games images

START_PIC = pygame.image.load("pic/title3.png")

GAME_OVER_PIC = pygame.image.load("pic/game_over.png")
GAME_OVER  = pygame.transform.scale(GAME_OVER_PIC,SCREEN_SIZE)

SPECIAL_FOOD = [pygame.transform.scale(pygame.image.load('pic/special_food/' + file),(40,40)) for file in os.listdir('pic/special_food')]

#sounds and music
#EAT_SOUND = pygame.mixer.music.load("pic/piupiu.wav")

#colors
#               R     G     B
BLACK     =    (0,    0,    0)
WHITE     =    (255,  255,  255)
RED       =    (255,  0,    0)
GREEN     =    (0,    255,  0)
BLUE      =    (0,    0,    255)
LTBLUE    =    (0,    255,  255)
ORANGE    =    (255,  150,  0)
YELLOW    =    (255,  255,  0)
DARKGREEN =    (  0, 155,   0)
DARKGRAY  =    ( 40,  40,  40)

GREEN_M   =    (  72, 194, 180)
PINK      =    (235,  66,  190)
YELLOW_L  =    (245,  201,  59)
#start screen colors

start_colors = [GREEN_M,PINK,YELLOW_L,WHITE]



