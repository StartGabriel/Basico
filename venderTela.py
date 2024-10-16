import pygame

from basico.tools import get_color, insert_text, allight_itens, get_mid
from basico.window import Window
from basico.button import Button
from basico.input import Input
from basico.list  import List

from pycss.buttoncss import Shadow,ButtonCss

pygame.init()

class TelaVender:
    def __init__(self):
        self.window_size = [1000,600]
        self.window_color = "gray"
        self.window_background = None
        self.window = Window(size=self.window_size,
                             color=self.window_color,
                             background=self.window_background).pack()
        self.mod = ButtonCss()
        self.list_produtos = []
        self.list_blit = None
        self.valor = []
        self.__buttons()
        self.__input()
    def __buttons(self):
        self.button_size = [100,50]
        self.button_color = "dark_gray"
        self.button_ = None
        self.button_space = 5
        self.button_title_size = 15
        self.button_title_color = "black"
        self.button_size_f = [200,100]
        self.button_size_c = [100,100]
        self.button_cancelar_coordinate = [self.window_size[0]-self.button_space-self.button_size_c[0], self.window_size[1]-self.button_space-self.button_size_c[1]]
        self.button_finalizar_coordinate = [self.button_cancelar_coordinate[0]-self.button_size_f[0]-self.button_space, self.window_size[1]-self.button_space-self.button_size_f[1]]
        self.button_finalizar = Button(window= self.window,
                                       size= self.button_size_f,
                                       color= self.button_color,
                                       coordinate= self.button_finalizar_coordinate,
                                       title="",
                                       title_size=self.button_title_size,
                                       tile_color= self.button_title_color)
        
        self.title_f= insert_text(text="FINALIZAR",
                                  size=self.button_title_size,
                                  color= self.button_title_color)
        self.title_f_size = self.title_f.get_size()
        self.title_f_pos = get_mid(object_size_target=self.title_f.get_size(),
                                   object_size= self.button_size_f,
                                   coordinate_object=self.button_finalizar_coordinate)
    
        self.button_cancelar = Button(window= self.window,
                                       size= self.button_size_c,
                                       color= self.button_color,
                                       coordinate= self.button_cancelar_coordinate,
                                       title="CANCELAR",
                                       title_size=self.button_title_size,
                                       tile_color= self.button_title_color)
        self.button_finalizar.pack()
        self.button_cancelar.pack()
        self.buttons = [self.button_finalizar,self.button_cancelar]
        self.mod.border(buttons= self.buttons)
        self.window.blit(self.title_f,
                         (self.title_f_pos[0],
                          self.button_finalizar_coordinate[1]+self.title_f_size[1]/2))
        pygame.draw.line(surface=self.window,
                         color=(255,255,255),
                         start_pos=(self.button_finalizar_coordinate[0],self.button_finalizar_coordinate[1]+self.title_f_size[1]*2),
                         end_pos=(self.button_finalizar_coordinate[0]+self.button_size_f[0],self.button_finalizar_coordinate[1]+self.title_f_size[1]*2))
    def __input(self):
        self.input_size = [800,50]
        self.input_color = "dark_gray"
        self.input_shadow = Shadow(size=0,
                             color= "black")
        self.input_coordinate = get_mid(object_size= self.window_size,
                                        object_size_target= self.input_size,
                                        coordinate_object=[0,0],
                                        tag="x")
        self.input_title = "PESQUISAR"
        self.input_background = None
        self.input_title_size = 20
        self.input_title_color = "black"

        
        self.input_button = Input(window= self.window,
                                  title= self.input_title,
                                  size= self.input_size,
                                  coordinate= self.input_coordinate,
                                  color= self.input_color,
                                  background= self.input_background,
                                  title_size= self.input_title_size,
                                  text_color= self.input_title_color,
                                  width= 50,
                                  border_color = "white",
                                  shadow=self.input_shadow,
                                  tag="not")
        self.input_button.pack()
    
    def run(self):
        self.window_backup = self.window.copy()
        self.main_loop = True
        while self.main_loop:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if self.list_blit:
                        if True in self.list_blit.iten_verify:
                            print("entrou aqui nessa budega")
                            self.inserir_valor()
                    self.pos = pygame.mouse.get_pos()
                    self.pesquisa = self.input_button.run(pos=self.pos)
                    self.imprimir_copy = self.window_backup.copy()
                    self.imprimir()
                if self.list_blit:
                    self.list_blit.run(events)
                  
                    
                    
                    
            pygame.display.flip()
        
    def imprimir(self):
        from basico.list import List
        try:
            if self.pesquisa is not None and self.pesquisa != '':
                try:
                    self.window.blit(self.imprimir_copy,(0,0))
                    self.consultar_banco = self.consultar(self.pesquisa)
                    self.list_produtos.append(self.consultar_banco[0][1])
                    self.list_blit = List(window=self.window,
                                        list_itens=self.list_produtos,
                                        color="dark_gray",
                                        title_size=20,
                                        coordinate=[self.input_coordinate[0],self.input_size[1]+self.input_coordinate[1]],
                                        bord_size=[500,500],
                                        tag="close")
                    
                    self.inserir_valor()
                    self.update()
                    self.list_blit.pack()
                    pygame.display.flip()
                    self.inserir_copy = self.window.copy()
                except:
                    self.window.blit(self.window_error,(0,0))
        except:
            print("produto nao localizado")
    def inserir_valor(self):
        try:
            if self.list_blit:
                self.valor = []
                for valor in self.list_blit.list_itens:
                    from bdpython.inserir_produdos import conectar,consultar_produto
                    self.cnn = conectar("bdpython/produtos.db")
                    self.valores = (consultar_produto(conn=self.cnn, nome=valor))
                    self.valor.append(self.valores[0][5])
                    self.imprimir_valor()
        except:
             pass
    def imprimir_valor(self):
        self.valor_imprimir = sum(self.valor)
        self.value= insert_text(text=f"R$: {self.valor_imprimir}",
                        size=self.button_title_size*2,
                        color= self.button_title_color)
        
        self.window_error = self.window.copy()
        pygame.display.flip()
    def update(self):
            self.window.blit(self.value,
                            (self.button_finalizar_coordinate[0],
                            self.button_finalizar_coordinate[1]+self.title_f_size[1]*3))
            self.window_error = self.window.copy()
            pygame.display.flip()
    def consultar(self, codigo):
        from bdpython.inserir_produdos import conectar,consultar_produto
        print("consulltar")
        try:
            self.cnn = conectar("bdpython/produtos.db")
            self.consultar_produto = consultar_produto(self.cnn, codigo)
            return self.consultar_produto
        except:
            print("produto não encontrado")
    
kkk = TelaVender()
kkk.run()

'''
janela = Window((1000,600), "white").pack()

lisst = List(janela,["1","2","3"], "black", 20, [300,300], [500,400])
lisst.pack()

while True:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEWHEEL:
            lisst.run(events)
    pygame.display.flip()'''