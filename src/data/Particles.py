import pygame,random
from data.image import *

pygame.init()




class Particle:
    def __init__(self,x,y,velX,velY,minSizeW,maxSizeW):
        self.width = random.randrange(minSizeW,maxSizeW)
    

        self.rect = pygame.Rect(x,y,self.width,self.width)
        self.velX = velX
        self.velY = velY

        self.time = 0

        

    def update(self,dt,subtractTime):

        self.rect.x += self.velX*dt
        self.rect.y +=self.velY*dt
        self.time+=1*dt

        if self.time >= subtractTime:
            self.time = 0
            self.rect.width-=1
            self.rect.height-=1

        
        

    def draw(self,screen,color):



        pygame.draw.rect(screen,color,self.rect)
      

class ParticleList:
    def __init__(self):
        self.particles = []
        self.time = 0
    def update(self,dt,addTime,subtractTime,x,y,velX,velY,minSizeW,maxSizeW):
        self.time+=1*dt

        if self.time >= addTime:
            self.Time = 0
            self.particles.append(Particle(x,y,velX,velY,minSizeW,maxSizeW))
        
        for particle in self.particles:
            particle.update(dt,subtractTime)

        
        for particle in self.particles:
            if particle.rect.width <= 0 or particle.rect.height <= 0:
                self.particles.remove(particle)
       
    def draw(self,screen,color):
        for particle in self.particles:
            particle.draw(screen,color)

