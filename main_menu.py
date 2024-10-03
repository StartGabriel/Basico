import pygame
import sys

from typing import Union,List

from basico.button import Button
from basico.input import Input
from basico.tools import get_color, allight_itens
from basico.window import Window
from pycss.buttoncss import ButtonCss

def menu():
    janela = Window(size=[1000,600],
                    color="dark_gray").pack()
    color_line = get_color("light_gray")
    pygame.draw.line(janela,color_line,(320,0),(320,710),5)
    return janela

janela = menu()
def _menu(window:pygame.Surface=janela):
    janela_backup = window.copy()
    but_cadastrar = Button(window=janela,
                    size=[300,50],
                    color="dark",
                    coordinate=[0,0],
                    title="CADASTRAR",
                    title_size=30,
                    tile_color= "white",
                    border_radios= 100,
                    command= _cadastrar)
    but_vender = Button(window=janela,
                    size=[300,50],
                    color="dark",
                    coordinate=[0,0],
                    title="VENDER",
                    title_size=30,
                    tile_color= "white",
                    border_radios= 100,
                    command= _cadastrar)
    but_menu = Button(window=janela,
                      size=[300,50],
                      color="green",
                      coordinate=[10,10],
                      title="MENU",
                      title_size=30,
                      tile_color= "white",
                      border_radios= 100,
                      command= revert)
    buts = [but_cadastrar, but_vender]
    but_menu.pack()
    allight_itens(list_itens=buts,
              start_coordinates=[10,70],
              tag="y")
    css = ButtonCss()
    css.shadow(buttons=[but_menu],
               size=5,
               visibility=50)
    css.shadow(buttons=buts,
               size=5,
               visibility=50)
    
    
    loop_menu = True
    
    while loop_menu:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for but in buts:
                    but.run(pos=pos)
                    but_menu.run(pos=pos)
                    if but_menu.clicked == -1:
                        janela.blit(janela_backup,(0,0))
                        loop_menu = False

                    
        pygame.display.flip()
def revert():
    pass                
def _cadastrar():
    print("teste cadastro")
    


but_menu = Button(window=janela,
                      size=[300,50],
                      color="dark",
                      coordinate=[10,10],
                      title="MENU",
                      title_size=30,
                      tile_color= "white",
                      border_radios= 100,
                      command= _menu)





css = ButtonCss()
css.shadow(buttons=[but_menu],
           size=5,
           visibility=50)


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            but_menu.run(pos=pos)
    pygame.display.flip()