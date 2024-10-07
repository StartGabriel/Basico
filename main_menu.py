import pygame
import sys


from typing import Union,List

from basico.button import Button
from basico.input import Input
from basico.tools import get_color, allight_itens
from basico.window import Window
from pycss.buttoncss import ButtonCss
class Main:
    def __init__(self):
        """Cria o laço principal
        """
        self.janela = Window(size=[1000,600],
                             color="dark_gray").pack()
        self.color_line = get_color("dark")
        self.line_pos_start =  [320,0]
        self.line_pos_end = [320,710]
        self.line_width = 5
        self.__set_defauth_values()

    def __set_defauth_values(self):
        """Seta valores padrões e facilita manipulação futura.
        """
        pygame.draw.line(surface= self.janela,
                         color= self.color_line,
                         start_pos= self.line_pos_start,end_pos= self.line_pos_end,
                         width=self.line_width)
        self.button_color = get_color("dark")
        self.button_defaut_pos = [0,0]
        self.button_title_size = 20
        self.button_title_color = get_color("white")
        self.button_border_radius = 100
        self.button_size = [300,50]
        self.button_menu_color = get_color("green")
        self.button_menu_title_color = get_color("black")
        self.button_menu_pos = [10,10]
        self.start_coordinates = [10,70]
        self.inp_return = [0,1,2,3]
        self.input_color = "dark_gray"
        self.input_title_size = 20
        self.input_title_color = "black"
        
    def menu(self):
        self.__set_defauth_values()
        self.janela_backup = self.janela.copy()
        self.but_cadastrar = Button(window=self.janela,
                        size= self.button_size,
                        color= self.button_color,
                        coordinate= self.button_defaut_pos,
                        title= "CADASTRAR",
                        title_size= self.button_title_size,
                        tile_color= self.button_title_color,
                        border_radios= self.button_border_radius,
                        command= self.cadastrar)
        self.but_vender = Button(window=self.janela,
                        size= self.button_size,
                        color= self.button_color,
                        coordinate= self.button_defaut_pos,
                        title= "VENDER",
                        title_size= self.button_title_size,
                        tile_color= self.button_title_color,
                        border_radios= self.button_border_radius,
                        command= self.cadastrar)
        self.but_menu = Button(window= self.janela,
                        size= self.button_size,
                        color= self.button_menu_color,
                        coordinate= self.button_menu_pos,
                        title="MENU",
                        title_size= self.button_title_size,
                        tile_color= self.button_menu_title_color,
                        border_radios= self.button_border_radius,
                        command= self.revert)
        self.buttons = [
                     self.but_cadastrar,
                     self.but_vender]
        self.but_menu.pack()
        allight_itens(list_itens=self.buttons,
                start_coordinates=self.start_coordinates,
                tag="y")
        self.modificadores = ButtonCss()
        self.modificadores.shadow(buttons=self.buttons,
                size=5,
                visibility=50)
        
        self.main_loop_menu = True
        
        while self.main_loop_menu:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    for but in self.buttons:
                        but.run(pos=self.pos)
                    self.but_cadastrar.run(pos=self.pos)
                    self.but_menu.run(pos=self.pos)
                    if self.but_menu.clicked == 1:
                        self.janela.blit(self.janela_backup,(0,0))
                        self.but_menu.clicked = -1
                        self.main_loop_menu = False

                        
            pygame.display.flip()
        
        
    def cadastrar(self):
        self.janela_backup_ = self.janela.copy()
        self.inp_nome = Input(window=self.janela,
                        title="NOME DO PRODUTO",
                        size=[600,50],
                        coordinate=[350,10],
                        color=self.input_color,
                        title_size= self.input_title_size,
                        text_color= self.input_title_color,
                        tag="not")
        self.inp_marca = Input(window=self.janela,
                        title= "MARCA DO PRODUTO",
                        size=[295,50],
                        coordinate=[350,70],
                        color=self.input_color,
                        title_size=self.input_title_size,
                        text_color= self.input_color,
                        tag="not")
        self.inp_codigo = Input(window=self.janela,
                        title="CODIGO DE BARRAS",
                        size=[295,50],
                        coordinate=[655,70],
                        color=self.input_color,
                        title_size=self.input_title_size,
                        text_color= self.input_color,
                        tag="not")
        self.inp_qtd = Input(window=self.janela,
                        title="QUANTIDADE",
                        size=[150,50],
                        coordinate=[350,130],
                        color=self.input_color,
                        title_size=self.input_title_size,
                        text_color= self.input_color,
                        tag="not")
        self.but_enviar = Button(window=self.janela,
                            title="ENVIAR",
                            size=[200,50],
                            coordinate=[510,130],
                            title_size=30,
                            color="green",
                            command=self.revert,
                            border_radios=100)
        
        self.inputs = [self.inp_nome,
                     self.inp_marca,
                     self.inp_codigo,
                     self.inp_qtd]
        
        self.modificadores.shadow(buttons=[self.but_enviar],size=5,visibility=50)
        self.get_inp_but = []
        for inp in self.inputs:
            inp.pack()
            self.get_inp_but.append(inp.get_but())
        self.modificadores.border(buttons=self.get_inp_but,color="black")
        self.main_loop_inputs = True
        while self.main_loop_inputs:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.pos_inp = pygame.mouse.get_pos()
                    self.but_enviar.run(pos=self.pos_inp)
                    for index,inp in enumerate(self.inputs):
                        self.verify = inp.run(pos=self.pos_inp)
                        if self.verify is not None:
                            self.inp_return[index]=(self.verify)
                            inp.pack()
                        
                    if self.but_enviar.clicked == 1:
                        self.but_enviar.clicked = -1
                        self.janela.blit(self.janela_backup_,(0,0))
                        self.main_loop_inputs = False
            pygame.display.flip()
        self.inserir()

    def revert(self):
        #apenas para update do botão menu dentro da função _menu
        pass 
    def inserir(self):
        from bdpython.inserir_produdos import conectar,criar_tabela, inserir
        self.cnn = conectar("bdpython/produtos.db")
        criar_tabela(self.cnn)
        inserir(self.cnn, self.inp_return[2],self.inp_return[0], self.inp_return[1], self.inp_return[3])         
a = Main()
def _menu():
    a.menu()

but_menu = Button(window=a.janela,
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