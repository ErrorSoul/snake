import pygame
from pygame.locals import *
from sys import exit
from data1 import *
from food import FOOD


image = pygame.image.load("redball.png")
image = pygame.transform.scale(image, (32,32))
image1 = pygame.transform.scale(image, (24,24))




class ATOM(pygame.sprite.Sprite):

    def __init__(self,image,center_point):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.dir = [0,0]
        self.rect = self.image.get_rect()
        self.rect.x = center_point[0]
        self.rect.y = center_point[1]

    def update(self):
        self.rect.x = (self.rect.x + self.dir[0]) % WIDTH
        self.rect.y = (self.rect.y + self.dir[1]) % HEIGHT
    
        



class HEAD(ATOM):

    def __init__(self, *kwargs):
        ATOM.__init__(self, *kwargs)
        self.dir = [ACC,0]
    



class SNAKE(HEAD):

    def __init__(self):
        HEAD.__init__(self, image1, [HALF_W,HALF_H])
        self.body = [ATOM(image1, [HALF_W - ACC + c * -ACC, HALF_H]) for c in range(N)]

    
    def move_up(self):
        if self.rect.y + self.dir[1] == self.rect.y:
            self.dir[0]= ZERO
            self.dir[1]=-ACC

    def move_down(self):
        if self.rect.y + self.dir[1] == self.rect.y:
            self.dir[0] = ZERO
            self.dir[1] = ACC

    def move_right(self):
        if self.rect.x + self.dir[0] == self.rect.x:
            self.dir[0] = ACC
            self.dir[1] = ZERO
            

    def move_left(self):
        if self.rect.x + self.dir[0] == self.rect.x:
            self.dir[0] = -ACC
            self.dir[1] = ZERO

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) :
                    self.move_up()

                elif (event.key == K_DOWN):
                    self.move_down()

                elif (event.key == K_RIGHT):
                    self.move_right()

                elif (event.key == K_LEFT):
                    self.move_left()
        
    

    def update(self):
        self.key_handler()
        


        HEAD.update(self)
        c = self.rect.center
        k = 0
        while k < len(self.body):
            c,self.body[k].rect.center = self.body[k].rect.center,c
            k +=1
    
    

        
        
    """def update (self):
     
        c = 0
            
            
        while c < len(self.body) :
                h = [self.rect.x, self.rect.y]

                if c == 0:
                        g = h
                        self.rect.x = (self.rect.x  )%WIDTH
                        self.rect.y = (self.rect.y )%HEIGHT
                self.body[c].rect.center,g = g,self.body[c].rect.center
                c +=1"""
    
"""
class SNAKE(pygame.sprite.Sprite):

    

    def __init__(self,image,number):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.number = number
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self):
        self.rect.x += self.number"""
        

pygame.init()
#a = HEAD(image,[HALF_W,HALF_H])
#b= ATOM(image,[HALF_W+64,HALF_H])
e = SNAKE()
#c =  pygame.sprite.Group([a,b,e])


food = FOOD()
f = pygame.sprite.GroupSingle()
f.add(food)
body = pygame.sprite.Group(e.body)
g = pygame.sprite.Group(e,food,e.body)

screen = pygame.display.set_mode((SCREEN_SIZE),0,32)
clock = pygame.time.Clock()
G=0
while True:
    global G
    
                 
               
    G +=1
    if G==4:
        screen.fill(ORANGE)
        pygame.sprite.spritecollide(e, f,True)
        pygame.sprite.spritecollide(e, body,True)

        g.draw(screen)
        g.update()
        G=0

    #screen.blit(image, Rect(120,120,14,40))
    
    pygame.draw.rect(screen,YELLOW,Rect((HALF_W,HALF_H),(50,50)))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(20)
    
