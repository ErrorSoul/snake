
from data1 import *
from food import FOOD







class ATOM(pygame.sprite.Sprite):

    def __init__(self,image,center_point):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.dir = [0,0]
        self.rect = self.image.get_rect()
        self.rect.center = (center_point)
        #self.rect.center[1] = center_point[1]

    def update(self):
        self.rect.x = (self.rect.x + self.dir[0]) % WIDTH
        self.rect.y = (self.rect.y + self.dir[1]) % HEIGHT

    def intersect(self, other):
        
        other.stop()
    
        



class HEAD(ATOM):

    def __init__(self, *kwargs):
        ATOM.__init__(self, *kwargs)
        self.dir = [ZERO,ZERO]
    



class SNAKE(HEAD):

    def __init__(self):
        
        self.body = [ATOM(BODY, [HALF_W -ACC *c , HALF_H - ACC]) for c in range(N)]
        HEAD.__init__(self, HEAD_S, self.body[0].rect.center)
        self.FLAG = True
        self.score = ZERO


    def add(self, food):
        self.score += 5
        self.body.append(ATOM(BODY,(-100,0)))
        

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

    def stop(self):
        self.FLAG = True

    def key_handler(self):
        

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) :
                    self.move_up()

                elif(event.key == K_r):
                    self.dir[0] = ACC
                    self.FLAG = False
                    

                elif (event.key == K_DOWN):
                    self.move_down()

                elif (event.key == K_RIGHT):
                    
                    self.move_right()
                    

                elif (event.key == K_LEFT):
                    self.move_left()
        
    

    def update(self):
        self.key_handler()
        if not self.FLAG:
            HEAD.update(self)
            c = self.rect.center
            k = 0
            while k < len(self.body) :
                c,self.body[k].rect.center = self.body[k].rect.center,c
                k +=1
        
    
    

        
        
    

        

