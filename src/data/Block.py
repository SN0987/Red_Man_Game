import pygame,random
from data.image import *
from data.animator import *
from data.Bullet import *
from data.Particles import *
from data.text import *

class Block:
    def __init__(self,x,y,frameTime,srcY):

       
        self.rect = pygame.Rect(x,y*25,25,25)
        self.image = load_spritesheet("assets/blocks.png",0,srcY*25,25,25)

        self.image = pygame.transform.scale(self.image,(25,25))

        self.anima = Animator()
        self.anima.addAnimation(Animation(0,srcY,0,0,25,25,0,0))
        self.anima.addAnimation(Animation(1,srcY,3,0,25,25,8,0)) # 1 destroy animation
        self.anima.setAnimationState(0)
        self.frameTime = frameTime
        self.destroyTime = 0
        self.time = 0

        self.destroy = False
        self.frame = 0
        self.updateFrame = 0
        self.srcY = srcY
        self.particleList = ParticleList()
        self.particleListTwo = ParticleList()
        self.particleListThree = ParticleList()
        self.particleListFour = ParticleList()

        self.drawInfo = False
        

        if self.srcY == 0:
            self.explainText = Text("fonts/font_basic.ttf","Red Block, Shoot It.. By Pressing Space!",15,(255,255,255))
        else:
            self.explainText = Text("fonts/font_basic.ttf","Green Block, Shoot It.. By Pressing Space!",15,(255,255,255))
            
        self.explainTextTwo = Text("fonts/font_basic.ttf","Don't Let It Get To The Other Side!",15,(255,255,255))


    def update(self,dt,bulletList):
        
        mx,my = pygame.mouse.get_pos()


        if self.rect.collidepoint((mx,my)):
            self.drawInfo = True
        else:
            self.drawInfo = False

        
        self.time+=1*dt
        if self.time >= self.frameTime:
            self.time = 0

            if self.srcY == 1:
                self.rect.x-=25
            else:
                self.rect.x+=25
        
      
        self.particleList.update(dt,16,4,self.rect.right,self.rect.y+12,2,2,2,5)
        self.particleListTwo.update(dt,16,4,self.rect.x-5,self.rect.y+12,-2,2,2,5)
        self.particleListThree.update(dt,16,4,self.rect.x+12,self.rect.y-5,0,-2,2,5)
        self.particleListFour.update(dt,16,4,self.rect.x+12,self.rect.bottom,0,2,2,5)
        
            
        
        if self.destroy:
            self.destroyTime+=1

        self.anima.update(dt)

        self.collideWithBullet(bulletList)


    def collideWithBullet(self,bulletList):
        for bullet in bulletList.bullets:
            if bullet.rect.colliderect(self.rect):
                self.destroy = True
                bullet.destroy = True
                

    def draw(self,screen):
        #self.animation.draw(screen,self.image,self.rect,25,25,"assets/blocks.png")
        #self.image = load_spritesheet("assets/blocks.png",self.frame*25,0,25,25)
        #screen.blit(self.image,self.rect)

        if self.destroy:
            self.anima.setAnimationState(1)
            self.anima.draw(screen,self.image,self.rect,75,75,"assets/blocks.png")
        else:
            self.anima.draw(screen,self.image,self.rect,25,25,"assets/blocks.png")

        if self.srcY == 1:
            self.particleList.draw(screen,(6,194,37))
            self.particleListTwo.draw(screen,(6,194,37))
            self.particleListThree.draw(screen,(6,194,37))
            self.particleListFour.draw(screen,(6,194,37))
        elif self.srcY == 0:
            self.particleList.draw(screen,(212,38,25))
            self.particleListTwo.draw(screen,(212,38,25))
            self.particleListThree.draw(screen,(212,38,25))
            self.particleListFour.draw(screen,(212,38,25))

        if self.drawInfo:
            
           
            if self.srcY == 0:
                self.explainText.draw(screen,self.rect.x+40,self.rect.y+15)
                self.explainTextTwo.draw(screen,self.rect.x+40,self.rect.y+35)
                pygame.draw.line(screen,(255,255,255),(self.rect.right+15,self.rect.y+12),(self.rect.right+205,self.rect.y+12),3)
            elif self.srcY == 1:
                self.explainText.draw(screen,self.rect.x-217,self.rect.y+15)
                self.explainTextTwo.draw(screen,self.rect.x-217,self.rect.y+35)
                pygame.draw.line(screen,(255,255,255),(self.rect.x-15,self.rect.y+12),(self.rect.x-218,self.rect.y+12),3)


        
     


class BlockSpawner:
    def __init__(self):
      
        self.redBlocks = []
        self.greenBlocks = []

        self.spawnTime = 60*10
        self.time = 0
        self.speed = 5*60
        self.gameScore = 0

        


    def update(self,dt,bulletList,text):
        self.time+=1*dt

        if self.time >= self.spawnTime:
            self.time = 0

            redBlockY = random.randrange(0,14)
            

            self.redBlocks.append([Block(-25,redBlockY,self.speed,0),Block(-25,redBlockY+1,self.speed,0)])

            greenBlockY = random.randrange(0,14)

            self.greenBlocks.append([Block(475,greenBlockY,self.speed,1),Block(475,greenBlockY+1,self.speed,1)])

        if self.gameScore >= 500:
            self.spawnTime = 6*60
            self.speed = 4*60
        elif self.gameScore >= 200:
            self.spawnTime = 7*60
            self.speed = 4*60
        elif self.gameScore >= 100:
            self.spawnTime = 8*60
        elif self.gameScore >= 50:
            self.spawnTime = 9*60
        else:
            self.spawnTime = 10*60



        for listOf in self.redBlocks:
            for block in listOf:
                block.update(dt,bulletList)

        for listOf in self.greenBlocks:
            for block in listOf:
                block.update(dt,bulletList)


      
        
        for listOf in self.greenBlocks:
            for block in listOf:
                if block.destroyTime >= 24:
                    listOf.remove(block)
                    self.gameScore+=1
                    text.setText("Blocks Destroyed: " + str(self.gameScore))

        for listOf in self.redBlocks:
            for block in listOf:
                if block.destroyTime >= 24:
                    listOf.remove(block)
                    self.gameScore+=1
                    text.setText("Blocks Destroyed: " + str(self.gameScore))
                  
            

    def blocksGoOutOfBound(self):
        isBound = False

        for listOf in self.redBlocks:
            for block in listOf:
                if block.rect.x >= 425:
                    isBound = True
            
        for listOf in self.greenBlocks:
            for block in listOf:
                if block.rect.x <= -25:
                    isBound = True

        return isBound
    
    def collideWithPlayer(self,player):
        isCol = False

        for listOf in self.redBlocks:
            for block in listOf:
                if block.rect.colliderect(player.rect):
                    isCol = True
            
        for listOf in self.greenBlocks:
            for block in listOf:
                if block.rect.colliderect(player.rect):
                    isCol = True

        return isCol
    
    def draw(self,screen):
        for listOf in self.redBlocks:
            for block in listOf:
                block.draw(screen)

        for listOf in self.greenBlocks:
            for block in listOf:
                block.draw(screen)
        
        