import pygame,sys


class Text:
    def __init__(self,font_path,string,size,color):
        self.string = string
        self.font = pygame.font.Font(font_path,size)
        self.size = size
        self.color = color
        

    def setText(self,string):
        self.string = string
    def setSize(self,size):
        self.size = size
    
    def setColor(self,color):
        self.color = color

    def draw(self,screen,x,y):

        text_surf = self.font.render(self.string,False,self.color)

        screen.blit(text_surf,(x,y))
    
        