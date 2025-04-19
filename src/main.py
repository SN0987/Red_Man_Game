import pygame,sys,random
from data.Bg import *
from data.image import *
from data.Platform import *
from data.Player import *
from data.Snow import *
from data.Block import *
from data.text import *

pygame.init()


class Game:
    def __init__(self,width,height,fps):
        self.fps = fps
        self.width = width
        self.height = height


        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width,self.height))

        self.menu()


    def menu(self):

        

        currentTime = 0
        dt = 0
        lastTime = 0

        titleText = Text("fonts/font_pixel.ttf","Red Man",50,(255,255,255))

        while True:
            currentTime = pygame.time.get_ticks()
            dt = (currentTime-lastTime)/1000
            dt*=60
            lastTime = currentTime

            self.screen.fill((235, 76, 70))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game()


            titleText.draw(self.screen,self.width/2,30)
            
            pygame.display.update()
            self.clock.tick(self.fps)

    def game(self):
        

        cs_image = pygame.image.load("assets/crosshair.png").convert_alpha()
     
        gameBackground = Background("assets/Red_Man_Bg.png",3,21)
        platform = Platform(self.width/2-125,self.height-150)
        player = Player(self.width/2-32,self.height-400)
        snow = SnowList(80)
        spawner = BlockSpawner()


        dt = 0
        lastTime = 0
        currentTime = 0

        showScore = False

      
        scoreText = Text("fonts/font_basic.ttf","Blocks Destroyed: " + str(0),18,(255,255,255))
        
        speedText = Text("fonts/font_basic.ttf","Speed: " + "Slow",18,(255,255,255))
        gravityText = Text("fonts/font_basic.ttf","Gravity: " + "Slow",18,(255,255,255))

        pygame.mouse.set_visible(False)

        
        while True:
            

            currentTime = pygame.time.get_ticks()
            dt = (currentTime-lastTime)/1000
            dt*=60
            lastTime = currentTime
            
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_LSHIFT:
                        showScore = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT:
                        showScore = False
              

            mx,my = pygame.mouse.get_pos()

           
            
            if spawner.blocksGoOutOfBound():
                self.menu()
            
            if spawner.collideWithPlayer(player):
                self.menu()
            
            if spawner.gameScore >= 1000:
                self.win()
            #update code
            gameBackground.update(dt)
            platform.update(dt)
            player.update(dt,platform)
            snow.update(dt)
            spawner.update(dt,player.bulletList,scoreText)


            if player.speed >= 20:
                speedText.setText("Speed: Very High")
            elif player.speed >= 15:
                speedText.setText("Speed: High")
            elif player.speed >= 10:
                speedText.setText("Speed: Mid-High")
            elif player.speed >= 5:
                speedText.setText("Speed: Medium")
            else:
                speedText.setText("Speed: Slow")

            if player.gravity >= 10:
                gravityText.setText("Gravity: High")
            elif player.gravity >= 5:
                gravityText.setText("Gravity: Medium")
            elif player.gravity < 5 and not player.gravity <= 0:
                gravityText.setText("Gravity: Low")
            else:
                gravityText.setText("Gravity: None")



            #draw code
            gameBackground.draw(self.screen)
            if showScore:
                scoreText.draw(self.screen,20,20)
                speedText.draw(self.screen,20,40)
                gravityText.draw(self.screen,20,60)
            platform.draw(self.screen)
            player.draw(self.screen)
            spawner.draw(self.screen)

            

            snow.draw(self.screen)
            self.screen.blit(cs_image,(mx,my))

        
            pygame.display.update()
            self.clock.tick(self.fps)
    def win(self):
        gameBackground = Background("assets/Red_Man_Bg.png",3,21)


        dt = 0 
        lastTime = 0
        currentTime = 0

        text = Text("fonts/font_pixel.ttf","You Win!",45,(255,255,255))
        while True:

            currentTime = pygame.time.get_ticks()
            dt = (currentTime-lastTime)/1000
            dt*=60
            lastTime = currentTime
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu()

            gameBackground.update(dt)
            gameBackground.draw(self.screen)

            text.draw(self.screen,self.width/2-60,self.height/2-45)
            pygame.display.update()
            self.clock.tick(self.fps)



if __name__ == "__main__":
    game = Game(450,600,60)

