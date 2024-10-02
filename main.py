#from basico.input import Input
from basico.button import Button
from basico.window import Window
from pycss.buttoncss import ButtonCss
from basico.tools import allight_itens, draw_rect

import pygame

janela = Window(size=(1000,1000), color= "white", background= "images/paisagem.jpg").pack()

but = Button(window=janela,size=[300,50], width= 0, color="red", border_radios= 100)
'''
but2 = Button(window=janela, width= 100, color="red")
allight_itens([but,but2],[0,0])
but.pack()

'''

#draw_rect(janela,[300,50],[100,100], (255,0,0), 0, border_radios=100)
b = ButtonCss()
b.shadow([but],10, visibility= 50)
#b.shadow([but,but2],10)
#b.shadow([but,but2], size= 10, visibility= 50)
while True:
    pygame.display.flip()