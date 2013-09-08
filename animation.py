from data1 import CHERRYS
import pygame
from pygame.locals import *
from sys import exit


#global variables
WIDHT = 640
HEIGHT = 480
SCREEN_SIZE = (WIDHT,HEIGHT)
HALF_W = WIDHT/2
HALF_H = HEIGHT/2
START_POS = (HALF_W,HALF_H)
START = True
RECT  = (200,25)
ZERO = 0
TIMER = 20
FPS = 20
frame_count = ZERO
#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK
## "LINEBAR"

#helper function
def terminate():
    pygame.quit()
    exit()


def main(obj):
    pygame.init()
    display = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(obj.screen_name)
    clock = pygame.time.Clock()

    while START:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if(event.key== K_a):
                    terminate()



        display.fill(WHITE)
        obj.draw(display)
        #obj.update()
        pygame.display.flip()
        clock.tick(FPS)


class Linebar(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect  = self.image.get_rect()
        self.screen_name = "ANIMATION"
        self.c  = 0
       
    

    def play(self, screen, seconds):
        
        self.draw(screen)
        self.update()
            
    def draw(self,screen):
        self.c +=1
        a = self.c%3
        
       
        screen.blit(CHERRYS[a],(START_POS[0]+50,START_POS[1]))
        ## screen.blit(CHERRYS[1],(START_POS[0]+100,START_POS[1]))
        ## screen.blit(CHERRYS[2],(START_POS[0]+200,START_POS[1]))

lin = Linebar(CHERRYS[0])
main(lin)
