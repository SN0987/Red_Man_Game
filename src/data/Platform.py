import pygame
from data.Particles import *

class Platform:
    def __init__(self,x,y):
        
        self.rect = pygame.Rect(x,y,250,30)
        self.image = pygame.image.load("assets/purple_platform.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.listOfParticles = []

        for i in range(int(250/10)):
            self.listOfParticles.append(ParticleList())

    def update(self,dt):
        
        for i in range(int(250/10)):
            self.listOfParticles[i].update(dt,7,2,self.rect.x+i*10,self.rect.bottom-10,0,3,5,10)


    def draw(self,screen : pygame.Surface):
        screen.blit(self.image,self.rect)
       

        for particle in self.listOfParticles:
            particle.draw(screen,(130,47,168))
        #pygame.draw.rect(screen,(0,0,0),self.rect)

