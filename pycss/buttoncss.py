from typing import Union, List
from basico.button import Button
from basico.tools import get_color 
import pygame
pygame.init()
class ButtonCss:
    def __init__(self,
                 tag:callable = None):
        self.tag = tag
    
    def shadow(self, buttons: List[Button], 
            size: int, 
            color_of_shadow: str = "black", 
            visibility: int = 255, 
            orientation: List[int] = [1, 1]):
        """Cria uma sombra no botão

        Args:
            buttons (List[Button]): Lista de botões a serem aplicados
            size (int): Distância da sombra
            color_of_shadow (str, optional): Cor da sombra. Defaults to "black".
            visibility (int, optional): Transparência da sombra. Defaults to 255.
            orientation (List[int], optional): Orientação da sombra, use [-1, -1] para inverter. Defaults to [1, 1].
        """
        color_of_shadow = get_color(color_of_shadow)
        for but in buttons:
            temp_surface = pygame.Surface((but.size[0], but.size[1]), pygame.SRCALPHA)
            temp_surface_color = (color_of_shadow[0], color_of_shadow[1], color_of_shadow[2], visibility)

            # Desenhe a sombra na superfície temporária
            pygame.draw.rect(temp_surface, temp_surface_color, (0, 0, but.size[0], but.size[1]), but.width, but.border_radios)

            # Calcule a posição da sombra
            temp_surface_coordinate_x = but.coordinate[0] + size * orientation[0]
            temp_surface_coordinate_y = but.coordinate[1] + size * orientation[1]

            # Blit a superfície temporária na janela do botão
            but.window.blit(temp_surface, (temp_surface_coordinate_x, temp_surface_coordinate_y))
            
            # Chame o método de empacotamento do botão, se necessário
            but.pack()

    def border(self, buttons:List[Button], width:int = 2, color:str = "white"):
        color = get_color(color)
        for but in buttons:
            color_backup = but.color
            but.size[0] += width
            but.size[1] += width
            but.color = color
            but.pack()
            but.size[0] -= width
            but.size[1] -= width
            but.coordinate[0] += width/2
            but.coordinate[1] += width/2
            but.color = color_backup
            but.pack()
            pygame.display.flip()
    def color_press(self,buttons:List[Button], color:str = "white"):
        color = get_color(color)
        for but in buttons:
            print(but.color)
            color_backup = get_color(but.color)
            if but.clicked == -1:
                print("troca")
                but.color = color
                but.pack()
                but.color = color_backup
            if but.clicked == 1:
                print("troca -1")
                but.color = color_backup
                but.pack()
            pygame.display.flip()