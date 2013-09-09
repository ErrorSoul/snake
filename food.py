import pygame
import random 
from data1 import WIDTH,HEIGHT,ACC
from data1 import CHERRY1, CHERRYS, FRUITS,SPECIAL_FOOD
from data1 import OUT, ZERO, e ,SOUND



class FOOD (pygame.sprite.Sprite):
    
    def __init__(self, image):

        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-ACC)
        self.rect.y = random.randint(0,HEIGHT-ACC)
         
        

    def check_position(self,other):

        others = pygame.sprite.Group(other.body[1:],other)
        while pygame.sprite.spritecollide(self,others,False):
            self.pdate()
        return self.rect.center 



    def intersect(self, other):
        other.score += 5

        e.set_volume(0.3)
        e.play()
        self.check_position(other)
        other.add(self)
       
            

    def pdate(self):

        self.rect.x = random.randint(0,WIDTH-ACC)
        self.rect.y = random.randint(0,HEIGHT-ACC)
        self.image = random.choice(FRUITS)




class S_FOOD(FOOD):

    def __init__(self):
        FOOD.__init__(self,CHERRY1)
        self.numbers = range(50,1000, 50)
        self.rect.center = OUT 
        self.fl = True
        self.g = True
        self.c = ZERO
        self.r = ZERO
        

    def check_position(self,other):

        others = pygame.sprite.Group(other.body[1:],other)
        while pygame.sprite.spritecollide(self,others,False)  or self.rect.center == OUT :
            self.pdate()
        
    
       

    def add(self,score):
        self.score = score
                
    
        
        
      
            
    def update(self):
        self.r +=1
        if self.r ==1:
            self.c += 1
           
            g = self.c % 3
            #self.image = CHERRYS[t]
            self.image = SPECIAL_FOOD[g]
            self.r = 0
        
        
           
        
        a = filter(lambda x: x == self.other.score,self.numbers)
        if a and self.fl:
            self.check_position(self.other)
            self.g = False
            self.fl = False
            return  
                
                
        
            

 
        
    def intersect(self, other):
        other.score +=10
        self.fl = True
        self.g = True
        
        self.rect.center = OUT 
        e.set_volume(0.3)
        SOUND.stop()
        e.play()
        pygame.mixer.music.unpause()
        other.add(self)
        
   
        
    def pdate(self):

        self.rect.x = random.randint(0,WIDTH-ACC)
        self.rect.y = random.randint(0,HEIGHT-ACC)
