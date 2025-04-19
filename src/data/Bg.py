import pygame
from data.image import *
from data.animator import *


class Background:

    def __init__(self,path : str, maxFrames : int, fps : int):
        self.path = path
        self.image = load_spritesheet(self.path,0,0,30,40)
        self.image = pygame.transform.scale(self.image,(450,600))
        self.frames = 0
        self.maxFrames = maxFrames
        self.count = 0
        self.fps = fps
        self.backgroundWidth = 30
        self.backgroundHeight = 40
        self.anim = Animator()
        self.anim.addAnimation(Animation(0,0,maxFrames,0,self.backgroundWidth,self.backgroundHeight,fps,0))
        self.anim.setAnimationState(0)
        
        

    
    def update(self,dt):
        self.anim.update(dt)

    def draw(self,screen):
        self.anim.draw(screen,self.image,pygame.Rect(0,0,450,600),450,600,self.path)

