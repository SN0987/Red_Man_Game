import pygame



#load spritesheet simply

def load_spritesheet(path : str, srcX : int, srcY : int, srcWidth : int, srcHeight : int):
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((srcWidth,srcHeight))
    surface.blit(image,[0,0],[srcX,srcY,srcWidth,srcHeight])
    surface.set_colorkey((0,0,0))

    return surface

def cut_image(image,srcX,srcY,srcWidth,srcHeight):
    surface = pygame.Surface((srcWidth,srcHeight))
    surface.blit(image,[0,0],[srcX,srcY,srcWidth,srcHeight])
    surface.set_colorkey((0,0,0))
    return surface



def tint_image(surf,tint_color):
    surf = surf.copy()
    surf.fill((255,255,255,0),None,pygame.BLEND_RGBA_MULT)
    surf.fill(tint_color[0:3]+(0,),None,pygame.BLEND_RGBA_ADD)
    return surf