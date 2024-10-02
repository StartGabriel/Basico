import pygame

from typing import Union, List, Tuple
pygame.init()

class Button:
    def __init__(self,
                 window:pygame.Surface,
                 size:Union[List[int], Tuple[int, int]] = [300,50],
                 color:Union[str,Tuple[int,int,int], List[int]] = "white",
                 coordinate:Union[List[int],Tuple[int,int]] = [0,0],
                 title: str = "Button",
                 title_size:int = 50,
                 tile_color:str = "black",
                 background:str = None,
                 width = 50,
                 command:callable = None,
                 tags:callable = None):
        
        self.window = window
        self.size = size
        self.color = color
        self.coordinate = coordinate
        self.title = title
        self.title_size = title_size
        self.title_color = tile_color
        self.background = background
        self.command = command
        self.tags = tags
        self.width = width
    def pack(self):
        from tools import get_color, draw_rect, insert_text, get_mid
        if self.background:
            self.insert_background()
        self.color = get_color(self.color)
        self.rect = draw_rect(window= self.window,
                              size= self.size,
                              coordinate= self.coordinate,
                              color= self.color,
                              width=self.width)
        self.title = insert_text(text=self.title,
                                 color=self.title_color,
                                 size=self.title_size)
        self.title_size_blit = self.title.get_size()
        self.title_coordinate = get_mid(object_size=self.size,
                                        object_size_target=self.title_size_blit,
                                        coordinate_object=self.coordinate)
        self.window.blit(source=self.title,dest=self.title_coordinate)
        if self.tags:
            self.tags()
        return self
    def run(self,
            pos:Union[List[int],Tuple[int, int]]):
        self.verify = self.rect.collidepoint(pos)
        if self.verify == True:
            self.command()
    def insert_background(self):
        from tools import get_image
        get_image(window= self.window,
                  path= self.background,
                  scale= self.size,
                  coordinates= self.coordinate)     

