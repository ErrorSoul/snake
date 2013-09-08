
from data1 import *
from food import FOOD, S_FOOD
from snake import SNAKE 
from linebar import Linebar


# HWSURFACE | FULLSCREEN

class GAME(object):
    def __init__(self):
        self.G = 0
        self.food = FOOD(CHERRY)
        self.snake = SNAKE()
        self.special_food = S_FOOD()
        self.screen = pygame.display.set_mode((SCREEN_SIZE),0,32)
        self.clock = pygame.time.Clock()
        self.linebar = Linebar(WHITE,(30,25),RECT)
        self.timer = 0 
        
        

        
    def play(self):
    
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        self.run()

    def new_game(self,over_flag):

        if over_flag:
             
            self.snake = SNAKE()
            self.score = 0
            self.G = 0
            self.special_food.g = True
            self.special_food.fl = True


    def terminate(self):
        pygame.quit()
        exit()
        


    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()

            elif event.type == KEYDOWN:
                if(event.key == K_r):
                    self.snake.dir[0] = ACC
                    self.snake.FLAG = False

                elif(event.key == K_a):
                    
                    self.special_food.fl = False
                        
                elif (event.key == K_t):
                    self.terminate()
                elif (event.key == K_g):
                    self.new_game(self.snake.over_flag)

                if not self.snake.FLAG:

                    if (event.key == K_UP or event.key == K_w) :
                        self.snake.move_up()

                    elif (event.key == K_DOWN):
                            self.snake.move_down()

                    elif (event.key == K_RIGHT):
                        self.snake.move_right()


                    elif (event.key == K_LEFT):
                        self.snake.move_left()
        
    

    def objects_interact(self,snake, objects):
        if not snake.over_flag:
            for c in pygame.sprite.spritecollide(snake, objects, False):
                c.intersect(snake)
                

        
    def showGameOverScreen(self,over_flag):
        if over_flag:
            
            game = GAME_OVER
            gameRect = game.get_rect()
            gameRect.midtop = (HALF_W, 0)
            self.screen.blit(game, gameRect)
            self.drawPressKeyMsg('Press g key to new play.',(WIDTH - 250, HEIGHT - 30))
            pygame.time.wait(500)
            

    def special_food_life(self):
        
        if not self.special_food.g:
            seconds = self.clock.tick()
            self.timer += seconds
            self.linebar.play(self.screen,self.timer)
            
            if self.timer == TIMER:
                self.snake.score +=5
                self.special_food.rect.center = OUT 
            if self.timer == TIMER + 5:
                self.special_food.g = True
                self.special_food.fl = True
                self.timer = 0
        
        else:
            self.timer = 0
            self.special_food.rect.center = OUT
            self.linebar.f = False

    
    def drawStart(self, over_flag, flag):
        if not over_flag and  flag:
            self.drawPressKeyMsg('Press r to start',(0,HEIGHT - 30))

    def drawPressKeyMsg(self,str,(x,y)):
        pressKeySurf = pygame.font.Font(FONT, 18).render(str, True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (x,y)
        self.screen.blit(pressKeySurf, pressKeyRect)

    def drawScore(self, score):
        self.f = pygame.font.SysFont(FONT,36)
        scoreSurf = self.f.render('Score: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WIDTH - 140, 10)
        self.screen.blit(scoreSurf, scoreRect)


    def run(self):
     

            while True:
                self.key_handler()
                self.G +=1
                if self.G==4:
                    self.screen.fill(ORANGE)
                    all_objects = pygame.sprite.Group(self.snake,self.food,self.snake.body[1:],self.special_food)
                    self.special_food.other = self.snake
                    body_and_food = pygame.sprite.Group(self.snake.body[1:],self.food,self.special_food)
                    self.special_food.add(self.snake.score)
                    self.objects_interact(self.snake, body_and_food)
                    self.special_food.add(self.snake.score)
                    self.special_food_life()
                    all_objects.draw(self.screen)
                    all_objects.update()
                    self.G=0
                    self.drawScore(self.snake.score )
                    self.drawStart(self.snake.over_flag, self.snake.FLAG)
                    self.showGameOverScreen(self.snake.over_flag)
                

                
                pygame.display.update()
                pygame.display.flip()
                self.clock.tick(self.snake.speed)




#run game 
a = GAME()
a.play()
