import pygame 
from data1 import WIDTH,HEIGHT
from data1 import ACC,ZERO
from data1 import HALF_H,HALF_W
from data1 import BODY,HEAD_S, N, z







class ATOM(pygame.sprite.Sprite):

    def __init__(self,image,center_point):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.dir = [0,0]
        self.rect = self.image.get_rect()
        self.rect.center = (center_point)
        

        self.f = False

    def intersect(self, other):
        if not self.f:
            z.play()
            self.f = True
        
        other.stop()
    
        



class HEAD(ATOM):

    def __init__(self, *kwargs):
        ATOM.__init__(self, *kwargs)
        self.dir = [ZERO,ZERO]
        self.FLAG = True
        self.score = ZERO
        self.angle = 1
        
        self.speed = 35
        
    
    def update(self):
        self.rect.x = (self.rect.x + self.dir[0] ) % WIDTH
        self.rect.y = (self.rect.y + self.dir[1] ) % HEIGHT
        



class SNAKE(HEAD):

    def __init__(self):
        
        self.body = [ATOM(BODY, [HALF_W -ACC *c , HALF_H - ACC]) for c in range(N)]
        HEAD.__init__(self, HEAD_S, self.body[0].rect.center)
        self.over_flag = False
        self.score = 0 
        
        
    


    def add(self, food):
        
        self.body.append(ATOM(BODY,(-100,0)))


    def check_horiz_move (self):
        return self.rect.y + self.dir[1] == self.rect.y

    def check_vertic_move(self):
        return self.rect.x + self.dir[0] == self.rect.x

    def need_for_speed(self):
        self.speed += 0.005*(self.score/30)
    
    def head_rotate(self,n):
        if not self.angle:
                self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.rotate(self.image, 90)
        self.angle = 1 
        

    def move_up(self):
        if self.check_horiz_move():
            self.dir[0]= ZERO
            self.dir[1]=-ACC
            if  not self.angle:
                self.image = pygame.transform.rotate(self.image, -90)
            else:
                self.image = pygame.transform.rotate(self.image, 90)
            self.angle = 1 
                
    def move_down(self):
        if self.check_horiz_move():
            self.dir[0] = ZERO
            self.dir[1] = ACC
            if not self.angle:
                self.image = pygame.transform.rotate(self.image, 90)
                
                
            else:
                self.image = pygame.transform.rotate(self.image, -90)
            self.angle = 0  

    def move_right(self):
        if self.check_vertic_move():
            self.dir[0] = ACC
            self.dir[1] = ZERO
            if not self.angle:
                self.image = pygame.transform.rotate(self.image, 90)
                
            else:
                self.image = pygame.transform.rotate(self.image, -90)
            self.angle = 1 
            

    def move_left(self):
        if self.check_vertic_move():
            self.dir[0] = -ACC
            self.dir[1] = ZERO
            if not self.angle:
                self.image = pygame.transform.rotate(self.image, -90)
                
            else:
                self.image= pygame.transform.rotate(self.image, 90)
            self.angle = 0 

    def stop(self):
       
        self.over_flag = True
        self.FLAG = True


    def update(self):
        
        if not self.FLAG:
            self.need_for_speed()
            
            
            HEAD.update(self)
            c = self.rect.center
            k = 0
            while k < len(self.body) :
                c,self.body[k].rect.center = self.body[k].rect.center,c
                k +=1
        
    
    

        
        
    

        

