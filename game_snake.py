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
        pygame.font.init()
        self.f = pygame.font.SysFont('freesansbold.ttf',18)

        
    def play(self):
        pygame.init()
        
        pygame.display.set_caption("Snake game")
        self.run()

    def snakeEatFood(self,snake,food):
        if pygame.sprite.collide_rect(snake, food):
                        food.intersect(snake)

    def snakeCrossSelf(self, snake, body):
        for c in  pygame.sprite.spritecollide(snake, body, False):
                        c.intersect(snake)
        


    def drawScore(self, score):
        scoreSurf = self.f.render('Score: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WIDTH - 120, 10)
        self.screen.blit(scoreSurf, scoreRect)


    def run(self):
     

            while True:

                self.G +=1
                if self.G==3:
                    self.screen.fill(ORANGE)
                    self.snakeEatFood(self.snake, self.food)

                    all_objects = pygame.sprite.Group(self.snake,self.food,self.snake.body[1:])
                    body = pygame.sprite.Group(self.snake.body[1:])
                    
                    all_objects.draw(self.screen)
                    self.snakeCrossSelf(self.snake,body)
                    all_objects.update()
                    self.G=0
                    self.drawScore(100)
                #screen.blit(image, Rect(120,120,14,40))

                #pygame.draw.rect(screen,YELLOW,Rect((HALF_W,HALF_H),(50,50)))
                pygame.display.update()
                #pygame.display.flip()
                self.clock.tick(20)





a = GAME()

a.play()

