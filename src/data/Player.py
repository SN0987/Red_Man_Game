import pygame,math
from pygame.locals import *
from data.image import *
from data.animator import *
from data.grid import *
from data.cheapmath import *
from data.Bullet import *
from data.Particles import *

class Player:
    def __init__(self,x,y):
        self.velX = 0
        self.velY = 0

        self.state = "idle"
     
        self.isCollided = False
        self.isGrounded = False

        self.image = load_spritesheet("assets/player.png",0,0,32,32)
        self.rect = pygame.Rect(x,y,28,60)

        self.animator = Animator()
        self.animator.addAnimation(Animation(0,0,4,0,32,32,11,0)) # animation 0 - idle
        self.animator.setAnimationState(0)
        self.animator.addAnimation(Animation(0,1,4,0,32,32,11,0)) # animation 1 - idle left
        self.animator.addAnimation(Animation(0,2,2,0,32,32,10,0)) # animation 2 - move left
        self.animator.addAnimation(Animation(0,3,2,0,32,32,10,0)) # animation 3 - move right

        self.animator.addAnimation(Animation(0,4,3,0,32,32,8,0)) # animation 4 - shoot left
        self.animator.addAnimation(Animation(0,5,3,0,32,32,8,0)) # animation 5 - shoot right

        self.speed = 3
        self.gravity = 2

        self.offsetX = self.rect.x
        self.offsetY = self.rect.y

        #self.gridCheck = Grid(self.rect) # other method of collision if first method failed
    
        self.startPos = [-1,-1]
        self.endPos = [-1,-1]

        self.moveY = False
        self.moveX = False
        self.moveFrameX = 0
        self.moveFrameY = 0

        self.prevVelX = 0 
        self.rad_x = 0
        self.rad_y = 0

        self.isMouse = False
        self.isClick = False

        self.isShoot = False
        self.size = 0
        self.shootFrame = 0

        self.bulletList = BulletList()

        self.parts = ParticleList()
        self.partsTwo = ParticleList()



        
    def colX(self,platform):

        if self.rect.colliderect(platform.rect):
            self.isCollided = True
        else:
            self.isCollided = False
        
        if self.isCollided:
            if self.velX < 0:
                self.rect.x = platform.rect.right
            if self.velX > 0:
                self.rect.right = platform.rect.x

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 450-self.rect.width:
            self.rect.x = 450-self.rect.width

    def colY(self,platform):
        
        if self.rect.colliderect(platform.rect):
            self.isCollided = True
        else:
            self.isCollided = False

        if self.isCollided:
            if self.velY < 0:
                self.rect.y = platform.rect.bottom

            if self.velY > 0:
                self.rect.bottom = platform.rect.y
                self.isGrounded = True
            else:
                self.isGrounded = False


        
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 600-self.rect.height:
            self.rect.y = 600-self.rect.height


    def movementX(self,dt):

        if not self.moveX:
            self.moveFrameX = 0

    

        if self.moveX:
         
            self.velX = int(self.rad_x*int(self.speed))

            if self.velX > 0:
                self.parts.update(dt,1,2,self.rect.x,self.rect.bottom,self.velX,self.velY,2,10)
    
                if not self.isShoot:
                    self.animator.setAnimationState(3)
            elif self.velX < 0:
                self.partsTwo.update(dt,1,2,self.rect.right,self.rect.bottom,self.velX,self.velY,2,10)
              
                if not self.isShoot:
                    self.animator.setAnimationState(2)

            
            self.moveFrameX+=1
            if self.moveFrameX >= 30:
              
                self.prevVelX = self.velX
                self.velX = 0
                self.moveX = False
        else:
            if self.prevVelX < 0 and not self.isShoot:
                self.animator.setAnimationState(1)

            elif self.prevVelX > 0 and not self.isShoot or self.prevVelX == 0 and not self.isShoot:
                self.animator.setAnimationState(0)

        



    def movementY(self,dt):

        if not self.moveY:
            self.velY = int(self.gravity)
            self.moveFrameY = 0


      


        if self.moveY:
           
            self.velY = int(self.rad_y*int(self.speed))

            
            self.moveFrameY+=1
            if self.moveFrameY >= 30:
                self.velY = 0
                self.moveY = False

        

        
    def handleShooting(self,key):
        if key[pygame.K_SPACE]:
            if not self.isShoot:
                self.shootFrame = 0
                self.isShoot = True
                
        


        if self.isShoot:

            self.shootFrame+=1
            if self.shootFrame >= 32:
                if self.velX < 0:
                    self.bulletList.add(self.rect.x+(self.rect.width-10),self.rect.y+10,-8)
                elif self.velX > 0:
                    self.bulletList.add(self.rect.x+self.rect.width,self.rect.y+10,8)
                else:
                    if self.prevVelX == 0 or self.prevVelX > 0:
                        self.bulletList.add(self.rect.x+(self.rect.width-10),self.rect.y+10,8)
                    elif self.prevVelX < 0:
                        self.bulletList.add(self.rect.x,self.rect.y+10,-8)
                self.isShoot = False
            else:


                if self.velX < 0:
                    self.animator.setAnimationState(4)
                elif self.velX > 0:
                    self.animator.setAnimationState(5)
                elif not self.moveX or not self.moveY:
                    if self.prevVelX > 0 or self.prevVelX == 0:
                        self.animator.setAnimationState(5)
                    elif self.prevVelX < 0:
                        self.animator.setAnimationState(4)
                  
           
                
        

    def update(self,dt,platform):

        
        mouse = pygame.mouse.get_pressed()[0]
        mx,my = pygame.mouse.get_pos()
        if mouse:
            if not self.isClick:
                self.startPos = [mx,my]
                self.isClick = True

            self.isMouse = True
            self.endPos = [mx,my]
        if not mouse:
            angle = math.atan2(my-self.rect.y,mx-self.rect.x)
            if self.startPos[0] >= 0 and self.endPos[0] >= 0:
                self.rad_x = math.cos(angle)
                self.moveX = True
            
            if self.startPos[1] >= 0 and self.endPos[1] >= 0:
                self.rad_y = math.sin(angle)
                self.moveY = True

            self.size = calculate_size(self.endPos[0],self.startPos[0],self.endPos[1],self.startPos[1])

            
            self.isClick = False
            self.isMouse = False
            self.startPos = [-1,-1]
            self.endPos = [-1,-1]

        keys = pygame.key.get_pressed()
        self.animator.update(dt)
        self.movementX(dt)
        self.rect.x += self.velX*dt
        self.colX(platform)

        self.movementY(dt)
        self.rect.y += self.velY*dt
        self.colY(platform)

        self.offsetX = self.rect.x-30
        self.offsetY = self.rect.y-18


        self.changeSpeed(keys)
        self.handleShooting(keys)
        self.bulletList.update(dt)

      


        #self.gridCheck.update(self.rect)

    
    def changeSpeed(self,key):
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            if self.speed > 3:
                self.speed-=0.1
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            if self.speed < 20:
                self.speed+=0.1
        
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            if self.gravity > 0:
                self.gravity-=0.2
        elif key[pygame.K_w] or key[pygame.K_UP]:
            if self.gravity < 10:
                self.gravity+=0.2

       
   

            


       

    def draw(self,screen):
        self.parts.draw(screen,(10,10,10))
        self.partsTwo.draw(screen,(10,10,10))
        self.bulletList.draw(screen)
        self.animator.drawWithOffset(screen,self.image,self.rect,96,96,"assets/player.png",self.offsetX,self.offsetY)
      

        if self.isMouse:
            pygame.draw.line(screen,(255,255,255),self.startPos,self.endPos,2)
        
        #pygame.draw.rect(screen,(0,0,0),self.rect)
       # self.gridCheck.draw(screen,(0,255,0))


      