
import random 
from data1 import *



class FOOD (pygame.sprite.Sprite):
    
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH)
        self.rect.y = random.randint(0,HEIGHT)
    
