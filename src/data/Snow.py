import pygame,random


class Snow:
    def __init__(self,x,y,velX,velY):
        self.velX = velX

        self.velY = velY
        self.size = random.randrange(2,5)

        self.rect = pygame.Rect(x,y,self.size,self.size)
        self.image = pygame.image.load("assets/snow.png").convert_alpha()
    def update(self,dt):
        self.rect.y += self.velY*dt
        self.rect.x += self.velX*dt
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        


class SnowList:
    def __init__(self,amount):
        
        self.list = []

        for i in range(amount):
            self.list.append(Snow(450/2+random.randrange(-100,100),650,random.randrange(-2,2),random.randrange(-3,-1)))
    def update(self,dt):
        for snow in self.list:
            snow.update(dt)

            if snow.rect.y < -snow.rect.height:
                snow.rect.x = random.randrange(0,450)
                snow.rect.y = 600+snow.rect.height
                snow.velX = random.randrange(-2,2)
                snow.velY = random.randrange(-3,-1)

    def draw(self,screen):
        for snow in self.list:
            snow.draw(screen)

