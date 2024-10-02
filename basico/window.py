import pygame

from typing import Union, List, Tuple

from basico.tools import get_color, get_image
pygame.init()

class Window:
    def __init__(self,
                 size:Union[List[int], Tuple[int,int]],
                 color:str,
                 background:str= None):
        self.size = size
        self.color = get_color(color)
        self.background = background
        
    def pack(self):
        self.window_surface = pygame.display.set_mode(self.size, pygame.SRCALPHA)
        self.window_surface.fill(self.color)
        self.background = get_image(scale=self.size, coordinates=(0,0), path= self.background, window= self.window_surface)
        return self.window_surface
        
