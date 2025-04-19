import pygame


class Grid:
    def __init__(self,rect_to_split):
        self.rtc = rect_to_split
        self.right = pygame.Rect(self.rtc.x+self.rtc.width,self.rtc.y,4,self.rtc.height)
        self.left = pygame.Rect(self.rtc.x,self.rtc.y,4,self.rtc.height)
        self.down = pygame.Rect(self.rtc.x,self.rtc.y+self.rtc.height,self.rtc.width,4)
        self.up = pygame.Rect(self.rtc.x,self.rtc.y,self.rtc.width,4)

    def update(self,rect_to_split):
        self.rtc = rect_to_split

        self.right = pygame.Rect(self.rtc.x+self.rtc.width,self.rtc.y+7,4,self.rtc.height-10)
        self.left = pygame.Rect(self.rtc.x,self.rtc.y+7,4,self.rtc.height-10)
        self.down = pygame.Rect(self.rtc.x,self.rtc.y+self.rtc.height+4,self.rtc.width,4)
        self.up = pygame.Rect(self.rtc.x,self.rtc.y-4,self.rtc.width,4)

    def draw(self,screen,color):
        pygame.draw.rect(screen,color,self.right)
        pygame.draw.rect(screen,color,self.left)

        pygame.draw.rect(screen,color,self.down)
        pygame.draw.rect(screen,color,self.up)



      
