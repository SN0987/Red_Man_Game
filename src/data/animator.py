import pygame
from data.image import *


class Animation:
    def __init__(self,frameX : int, frameY : int, maxFrameX : int, maxFrameY : int, srcWidth : int, srcHeight : int, fpsX : int, fpsY : int):
        self.startFrameX = frameX
        self.startFrameY = frameY
        self.frameX = frameX
        self.frameY = frameY
        self.maxFramesX = maxFrameX
        self.maxFramesY = maxFrameY
        self.srcWidth = srcWidth
        self.srcHeight = srcHeight
        self.fpsX = fpsX
        self.fpsY = fpsY


    
class Animator:
    def __init__(self):
        self.anims = []
        self.countX = 0
        self.countY = 0
        self.fx = 0
        self.fy = 0
        self.currentState = -1
        self.destroy = False

        


    def addAnimation(self,animation : Animation):
        self.anims.append(animation)  
    def setAnimationState(self,value : int):
        if not self.currentState == value:
            self.currentState = value
            self.fx = self.anims[self.currentState].startFrameX
            self.fy = self.anims[self.currentState].startFrameY

    

    def update(self,dt):
        if self.anims[self.currentState].maxFramesX != 0:
            self.countX+=1*dt
            if self.countX >= self.anims[self.currentState].fpsX:
                self.countX = 0
                if self.fx >= self.anims[self.currentState].maxFramesX:
                    self.fx = self.anims[self.currentState].startFrameX
                else:
                    self.fx+=1

        else:
            self.fx = self.anims[self.currentState].startFrameX

        if self.anims[self.currentState].maxFramesY != 0:
            self.countY+=1*dt
            if self.countY >= self.anims[self.currentState].fpsY:
                self.countY = 0
                if self.fy >= self.anims[self.currentState].maxFramesY:
                    self.fy = self.anims[self.currentState].startFrameY
                else:
                    self.fy+=1
        else:
            self.fy = self.anims[self.currentState].startFrameY
    def draw(self,screen,image,rect,sizeW,sizeH,path):
        image = load_spritesheet(path,self.fx*self.anims[self.currentState].srcWidth,self.fy*self.anims[self.currentState].srcHeight,self.anims[self.currentState].srcWidth,self.anims[self.currentState].srcHeight)
        #image = cut_image(image,self.fx*self.anims[self.currentState].srcWidth,self.fy*self.anims[self.currentState].srcHeight,self.anims[self.currentState].srcWidth,self.anims[self.currentState].srcHeight)
        image = pygame.transform.scale(image,(sizeW,sizeH))
        screen.blit(image,rect)
    
        
    def drawWithOffset(self,screen,image,rect,sizeW,sizeH,path,offsetX,offsetY):
        image = load_spritesheet(path,self.fx*self.anims[self.currentState].srcWidth,self.fy*self.anims[self.currentState].srcHeight,self.anims[self.currentState].srcWidth,self.anims[self.currentState].srcHeight)
        image = pygame.transform.scale(image,(sizeW,sizeH))
        screen.blit(image,(offsetX,offsetY,rect.width,rect.height))
        #pygame.draw.rect(screen,(0,0,0),(rect.x,rect.y,rect.width,rect.height))


      
        