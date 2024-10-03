#from basico.input import Input
from basico.button import Button
from basico.window import Window
from pycss.buttoncss import ButtonCss
from basico.tools import allight_itens, draw_rect, get_color

import pygame

def menu():
    janela = Window(size=(1200,600), color= "very_dark").pack()
    color_line = get_color("light_gray")
    pygame.draw.line(janela,color_line,(320,0),(320,710),5)
    return janela
clock = pygame.time.Clock()
fps = 60
janela = menu()
def teste():
    print("press")

def buttons(window:pygame.Surface):
    but_menu = Button(window=window,size=[300,50],color="dark")
but = Button(window=janela,size=[300,50], coordinate=[10,10], title= "MENU",tile_color="white",width= 0, color="dark", border_radios= 100, command= teste)
but1 = Button(window=janela,size=[300,50], coordinate=[10,10], title= "MENU",tile_color="white",width= 0, color="dark", border_radios= 100, command= teste)
but2 = Button(window=janela,size=[300,50], coordinate=[10,10], title= "MENU",tile_color="white",width= 0, color="dark", border_radios= 100, command= teste)
'''
but2 = Button(window=janela, width= 100, color="red")
allight_itens([but,but2],[0,0])
but.pack()

'''
allight_itens([but,but1,but2],[10,10],"x")
buts =[but,but1,but2]

#draw_rect(janela,[300,50],[100,100], (255,0,0), 0, border_radios=100)
b = ButtonCss()
b.shadow([but,but1,but2],size= 10, color_of_shadow="black",visibility=100)
b.border([but,but1,but2])
#b.shadow([but,but2],10)
#b.shadow([but,but2], size= 10, visibility= 50)
while True:
    pygame.display.flip()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            but.run(pos)
            but1.run(pos)
            but2.run(pos)
            b.color_press([but,but1,but2],"red")

    pygame.display.flip()