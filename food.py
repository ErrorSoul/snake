
import random 
from data1 import *



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
        e.set_volume(0.1)
        
        e.play()
        self.check_position(other)
        print self.rect.center, '1'
        other.add(self)
       
            

    def pdate(self):
        
    
        self.rect.x = random.randint(0,WIDTH-ACC)
        self.rect.y = random.randint(0,HEIGHT-ACC)
        self.image = random.choice(FRUITS)

class S_FOOD(FOOD):

    def __init__(self):
        FOOD.__init__(self,CHERRY1)
        self.c = 0
        self.numbers = range(40,300, 40)
        self.rect.center = (-100,0)
        self.fl = True

    def check_position(self,other):
        print "sss"
        others = pygame.sprite.Group(other.body[1:],other)
        
        
        while pygame.sprite.spritecollide(self,others,False):
            print 'collide'
            self.pdate()
    
        

    def add(self,score):
    
        self.score = score
                

    def update(self):
        a = filter(lambda x: x == self.score,self.numbers)
        print a
        print "special_food.rect.center", self.rect.center
        if a :
            others = pygame.sprite.Group(self.other.body[1:],self.other)
        
            
            while pygame.sprite.spritecollide(self,others,False) or self.rect.center == (-100,0):
                print 'collide'
                self.pdate()
            
                self.fl = False
        
       
       

               
             
             
             
             
    
        
    def intersect(self, other):
        
        self.rect.center = (-100,0)
        self.fl= True
        e.set_volume(0.1)
        
        e.play()
        
        other.add(self)
        
   
        
