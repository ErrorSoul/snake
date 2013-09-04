from data1 import *
from food import FOOD
from snake import SNAKE , ATOM, HEAD





class GAME(object):
    def __init__(self):
        self.G = 0
        self.food = FOOD(CHERRY)
        self.snake = SNAKE()
        self.screen = pygame.display.set_mode((SCREEN_SIZE),0,32)
        self.clock = pygame.time.Clock()
        
        

        
    def play(self):
        pygame.init()
        pygame.font.init()
        
        pygame.display.set_caption("Snake game")
        self.run()

    def objects_interact(self,snake, objects):
        for c in pygame.sprite.spritecollide(snake, objects, False):
            c.intersect(snake)


        


    def drawScore(self, score):
        self.f = pygame.font.SysFont('freesansbold.ttf',36)
        scoreSurf = self.f.render('Score: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WIDTH - 120, 10)
        self.screen.blit(scoreSurf, scoreRect)


    def run(self):
     

            while True:

                self.G +=1
                if self.G==3:
                    self.screen.fill(ORANGE)
                    
                    
                    all_objects = pygame.sprite.Group(self.snake,self.food,self.snake.body[1:])
                    body_and_food = pygame.sprite.Group(self.snake.body[1:],self.food)
                
                    self.objects_interact(self.snake, body_and_food)
                    all_objects.draw(self.screen)
                    
                    all_objects.update()
                    self.G=0
                    self.drawScore(self.snake.score )
                

                #pygame.draw.rect(screen,YELLOW,Rect((HALF_W,HALF_H),(50,50)))
                pygame.display.update()
                #pygame.display.flip()
                self.clock.tick(20)





a = GAME()

a.play()

