from typing import Union, List
from basico.button import Button
from basico.tools import get_color 
import pygame
pygame.init()
class ButtonCss:
    def __init__(self,
                 tag:callable = None):
        self.tag = tag
    
    def shadow(self,buttons:List[Button], 
               size:int, 
               color_of_shadow:str = "black", 
               visibility:int = 255, 
               orientation:List[int]=[1,1]):
        """Cria uma sombra no botão

        Args:
            buttons (List[Button]): Lista de botões a serema aplicados
            size (int): Distancia da sombra
            color_of_shadow (str, optional): Cor da sombra. Defaults to "black".
            visibility (int, optional): Transparencia da sombra. Defaults to 255.
            orientation (List[int], optional): Orinetação da sombra, use [-1,-1] para inverter. Defaults to [1,1].
        """
        color_of_shadow = get_color(color_of_shadow)
        for but in buttons:
            temp_surface = pygame.Surface((but.size[0], but.size[1]), pygame.SRCALPHA)
            temp_surface_color = (color_of_shadow[0], color_of_shadow[1], color_of_shadow[2], visibility)
            temp_surface_coordinate_x= but.coordinate[0] + size*orientation[0]
            temp_surface_coordinate_y = but.coordinate[1] + size*orientation[1]
            temp_round_shadadow = pygame.draw.rect(temp_surface,temp_surface_color, (but.coordinate[0], but.coordinate[1], but.size[0], but.size[1]),but.width, but.border_radios)
            but.window.blit(temp_surface,[temp_surface_coordinate_x, temp_surface_coordinate_y])
            but.pack()
