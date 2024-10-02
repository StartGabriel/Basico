
import pygame
pygame.init()
from typing import Union, List, Tuple

def get_color(name_of_color:str):
    """Função para pegar tupla de cores

    Args:
        name_of_color (str): nome da cor(inglês)

    Returns:
        tuple: retorna uma tupla com os valores RGB
    """
    COLORS =   {"red": (255, 0, 0),
                "green": (0, 255, 0),
                "blue": (0, 0, 255),
                "white": (255, 255, 255),
                "black": (0, 0, 0),
                "yellow": (255, 255, 0),
                "cyan": (0, 255, 255),
                "magenta": (255, 0, 255),
                "gray": (128, 128, 128),
                "light_gray": (211, 211, 211),
                "dark_gray": (64, 64, 64),
                "very_dark": (20,20,20),
                "dark": (15,15,15),
                "orange": (255, 165, 0),
                "purple": (128, 0, 128),
                "pink": (255, 192, 203),
                "brown": (139, 69, 19),
                "lime": (0, 255, 0),
                "navy": (0, 0, 128),
                "teal": (0, 128, 128),
                "gold": (255, 215, 0),
                "olive": (128, 128, 0),
                "maroon": (128, 0, 0),
                "silver": (192, 192, 192)}
    try:#retorna uma lista de tupla caso esteja no dicionário de cores
        if type(name_of_color) == str:
            return COLORS[name_of_color]

        else:
            return name_of_color
    except:
        print("formato inválido ou cor não encontrada")
        return (0,0,0)
    
def draw_rect(window:pygame.Surface,
            size:Union[list[int], Tuple[int,int]],
            coordinate:tuple,
            color:tuple,
            width:int,
            border_radios:int,
            tag:str=None):
    """Desenha um retangulo na tela

    Args:
        window (pygame.Surface): Janela onde sera desenhado
        size (Union[list[int], Tuple[int,int]]): Tamanho do retangulo
        coordinate (tuple): Posição do retângulo
        color (tuple): Cor do retangulo
        width (int): grossura da linha do retangulo(se existir)

    Returns:
        rect: retorna um objeto rect pygame
    """

    
    
    color_tuple = get_color(color)

    try:
        rect = pygame.draw.rect(window,color,(coordinate[0], coordinate[1], size[0], size[1]),width,border_radios)
        return rect
    except:
        print("Parametros inválidos"
              "\nUse:"
              "\ndraw_rect("
              "\njanela=Pygame.Surface #janela principal"
              "\nsize=[50,50] #altura e largura"
              "\ncoordinates=[100,100] #posição x,y"
              "\ncolor='branco' #cor"
              "\nwidth=1 #grossura do contorno)")
        surface = pygame.display.set_mode((600,600))
        rect = pygame.draw.rect(surface=surface,
                                color=(255,255,255),
                                rect=(100,100,50,50),
                                width=1,
                                border_radius= border_radios)
        return rect
    
def get_image(scale:Union[List[int],Tuple[int,int]],
              coordinates:Union[List[int],Tuple[int,int]],
              window:pygame.Surface= None,
              path:str= None):
    """Transformna o caminho de uma imagem em surface

    Args:
        scale (Union[List[int],Tuple[int,int]]): escala da imagem
        coordinates (Union[List[int],Tuple[int,int]]): coordenada onde a imagem será inserida
        window (pygame.Surface, optional): tela onde a imagem sera inserida
        path (str, optional): caminho da imagem. Defaults to None.

    Returns:
        pygame.Surface: imagem surface
    """
    
    if path is not None:
        image = pygame.image.load(path)
        image_scale = pygame.transform.scale(surface=image,size=scale)
        
    if window is not None and path is not None:
        window.blit(image_scale,coordinates)
    
    if path is not None and window is None:
        return image_scale
        
def insert_text(text:str,
                color: str,
                size: int,
                window: pygame.Surface = None,
                coordinate:Union[List[int],Tuple[int,int]] = None):
    """Insere um texto ou cria um texto surface

    Args:
        text (str): Texto a ser inserido
        color (str): Cor
        size (int): Tamanho
        window (pygame.Surface, optional): Janela a ser inserido. Defaults to None.
        coordinate (Union[List[int],Tuple[int,int]], optional): Coordenada do texto. Defaults to None.

    Returns:
        pygame.Surface: retona um texto surface
    """
    try:
        fonte = pygame.font.Font(None, size)
        text_blit = fonte.render(text,True, color)
        if window is not None:
            window.blit(text_blit,coordinate)
        return text_blit
    except:
        return text

def get_center_window(window_size:Union[List[int],Tuple[int, int]],
            object_size:Union[List[int],Tuple[int, int]],
            tag:str=None):
    """Informa o centro da janela

    Args:
        window_size (Union[List[int],Tuple[int, int]]): Tamanho da janela
        object_size (Union[List[int],Tuple[int, int]]): Tamanho do objeto
        tag (str, optional): Tag para orientação 'x' ou 'y'. Defaults to None.

    Returns:
        List[int]: retorna o valor da coordenada de acordo com a tag.
    """
    
    center_x = window_size[0]/2 - object_size[0]/2
    center_y = window_size[1]/2 - object_size[1]/2
    center = [center_x,center_y]
    if tag == "x":
        return center_x
    if tag == "y":
        return center_y
    else:
        return center

def get_mid(object_size:Union[List[int],Tuple[int, int]],
            object_size_target:Union[List[int],Tuple[int, int]],
            coordinate_object:Union[List[int],Tuple[int, int]],
            tag:str=None):
    """Encontra o meio de um objeto

    Args:
        object_size (Union[List[int],Tuple[int, int]]): Tamanho do objeto.
        object_size_target (Union[List[int],Tuple[int, int]]): Tamanho do a ser centralizado
        coordinate_object (Union[List[int],Tuple[int, int]]): Coordenada do obejo
        tag (str, optional): Tag para orientação 'x' ou 'y'. Defaults to None.

    Returns:
        List[int]: Retorna a coordenada do centro do obejto de acordo com a tag
    """
    center_x = coordinate_object[0]+object_size[0]/2-object_size_target[0]/2
    center_y = coordinate_object[1]+object_size[1]/2-object_size_target[1]/2
    if tag == "x":
        return center_x
    if tag == "y":
        return center_x
    else:
        return [center_x, center_y]

def allight_itens(list_itens:list,
                  start_coordinates:Union[List[int], Tuple[int,int]],
                  tag:str = "x",
                  space:int= 10):
    if tag == "x":
        for iten in list_itens:
            iten.coordinate = [start_coordinates[0],start_coordinates[1]]
            start_coordinates[0] += iten.size[0]+space
            print(iten.coordinate)
    
