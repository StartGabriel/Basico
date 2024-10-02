import pygame

from typing import Union, List, Tuple
pygame.init()
from basico.tools import get_color, draw_rect, insert_text, get_mid

class Button:
    def __init__(self,
                 window:pygame.Surface,
                 size:Union[List[int], Tuple[int, int]] = [50,50],
                 color:Union[str,Tuple[int,int,int], List[int]] = "white",
                 coordinate:Union[List[int],Tuple[int,int]] = [0,0],
                 title: str = "Button",
                 title_size:int = 50,
                 tile_color:str = "black",
                 background:str = None,
                 width = 0, #Não mecha caso use o self border radios
                 border_radios= -1,
                 command:callable = None,
                 tags:callable = None):
        
        self.clicked = -1
        self.window = window
        self.size = size
        self.color = get_color(color)
        self.coordinate = coordinate
        self.title = title
        self.title_size = title_size
        self.title_color = get_color(tile_color)
        self.background = background
        self.command = command
        self.tags = tags
        self.width = width 
        self.border_radios = border_radios
    def pack(self):
        self.color = get_color(self.color)

        self.rect = draw_rect(self.window,self.size,self.coordinate, self.color, self.width, self.border_radios)
        
        self.title = insert_text(text=self.title,
                                 color=self.title_color,
                                 size=self.title_size)
        self.title_size_blit = self.title.get_size()
        self.title_coordinate = get_mid(object_size=self.size,
                                        object_size_target=self.title_size_blit,
                                        coordinate_object=self.coordinate)
        if self.background is not None:
            self.insert_background()
        self.window.blit(source=self.title,dest=self.title_coordinate)
        if self.tags:
            self.tags()
        return self
    def run(self,
            pos:Union[List[int],Tuple[int, int]]):
        self.verify = self.rect.collidepoint(pos)
        if self.verify == True:
            self.clicked = self.clicked *-1
            print(self.clicked)
            self.command()
    def insert_background(self):
        from basico.tools import get_image
        get_image(window= self.window,
                  path= self.background,
                  scale= self.size,
                  coordinates= self.coordinate)     

