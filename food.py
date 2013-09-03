
import random 
from data1 import *



class FOOD (pygame.sprite.Sprite):
    image = pygame.image.load("cherry.png")
    image = pygame.transform.scale(image,(48,48))
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = FOOD.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH)
        self.rect.y = random.randint(0,HEIGHT)
    
