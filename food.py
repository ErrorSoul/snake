
import random 
from data1 import *



class FOOD (pygame.sprite.Sprite):
    
    def __init__(self, image):

        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-ACC)
        self.rect.y = random.randint(0,HEIGHT-ACC)

    def intersect(self, other):
        others = pygame.sprite.Group(other,other.body[1:])
        
        while pygame.sprite.spritecollide(self,others,False):
            self.__update()
        return other.add(self)

    def __update(self):
    
        self.rect.x = random.randint(0,WIDTH-ACC)
        self.rect.y = random.randint(0,HEIGHT-ACC)


        
