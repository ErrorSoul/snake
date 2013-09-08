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
        obj.update(clock)
        pygame.display.flip()
        clock.tick(FPS)


class Linebar(object):
    def __init__(self,color,start,rect_size, width =  17):
        self.start = start
        self.color = color
        self.width = width
        self.rect = Rect((start[0],start[1] -10),rect_size)
        self.x = self.start[0]
        self.screen_name = "LINEBAR"
        self.s = 0
        self.f = False 
       
    

    def play(self, screen, seconds):
        if not self.f:
            self.draw(screen)
            self.upda(seconds)
            
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect, 3)
        pygame.draw.line(screen, self.color, self.start, (self.x,self.start[1]),self.width)
    def upda(self,seconds):
        #k = RECT[0]/float(TIMER)
        #k= 11
        if self.x < self.rect.bottomright[0] -3:
            
            self.x = self.start[0]  + seconds*11
        else:
            self.f = True
            self.x = self.start[0]

    def update(self,clock):
        f = FPS//4
        seconds = self.s //f
        self.s += 1
        if self.x < self.rect.bottomright[0]:
            
            self.x = HALF_W + seconds*2.5
            print seconds
        

if __name__ == "__main__":
    linebar = Linebar(GREEN,START_POS,RECT)
    main(linebar)
