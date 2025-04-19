import pygame
from data.image import *

from data.animator import *

class Bullet:
    def __init__(self,x,y,velX):
        self.velX = velX
        self.velY = 0
        self.rect = pygame.Rect(x,y,25,5)
        self.image = load_spritesheet("assets/bullet.png",0,0,25,5)
        self.destroy = False
        self.animator = Animator()
        self.animator.addAnimation(Animation(0,0,0,0,25,5,0,0))
        self.animator.addAnimation(Animation(1,0,3,0,25,5,10,0))
        self.animator.setAnimationState(0)
        self.destroyCounter = 0
    
    def update(self,dt):
        if not self.destroy:
            self.rect.x += self.velX*dt
         
        else:
            self.destroyCounter+=1

        if self.rect.x <= 0:
            self.animator.setAnimationState(1)
            self.destroy = True

            
        elif self.rect.x >= 450-25:
            self.animator.setAnimationState(1)
            self.destroy = True

      


        self.animator.update(dt)
    def draw(self,screen):

        if not self.destroy:

            self.animator.draw(screen,self.image,self.rect,25,5,"assets/bullet.png")
        elif self.destroy:
            self.animator.draw(screen,self.image,self.rect,50,10,"assets/bullet.png")
         


class BulletList:
    def __init__(self):
        self.bullets = []

    def add(self,x,y,velX):
        self.bullets.append(Bullet(x,y,velX))

    def update(self,dt):
        for bullet in self.bullets:
            bullet.update(dt)

        for bullet in self.bullets:
            if bullet.destroyCounter >= 20:
                self.bullets.remove(bullet)

    def collideWithPlayer(self,player):
        isCol = False
        for bullet in self.bullets:
            if bullet.rect.colliderect(player.rect):
                isCol = True
            else:
                isCol = False
        
        return isCol
                
    def draw(self,screen):
        for bullet in self.bullets:
            bullet.draw(screen)
