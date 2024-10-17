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
        self.button_delete =  []
        self.window_backup = self.window.copy()
        self.button_title_finalizar_gambiarra = 'R$: 0'
        
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
                                       title=self.button_title_finalizar_gambiarra,
                                       title_size=30,
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
    def pack(self):
        self.window.blit(self.window_backup,(0,0))
        self.__buttons()
        self.__input()
        self.__list_prod()
        self.__delete_itens()
        pygame.display.update()
        
    def __list_prod(self):
        self.list_blit = List(window=self.window,
                                        list_itens=self.list_produtos,
                                        color="dark_gray",
                                        title_size=20,
                                        coordinate=[self.input_coordinate[0],self.input_size[1]+self.input_coordinate[1]],
                                        bord_size=[500,500])
        self.list_blit.pack()
        
    def __delete_itens(self,event = None):
        self.button_delete =  []
        self.button_delete_color = "light_gray"
        self.button_delete_ = None
        self.button_delete_title = "X"
        self.button_delete_title_color = "red"
        self.button_delete_title_size = 20
        self.button_delete_size = [20,20]
        for index, but in enumerate(self.list_blit.list_itens):
            self.button_delete.append(Button(window=self.window,
                                             size=self.button_delete_size,
                                             color=self.button_delete_color,
                                             coordinate=[600,self.list_blit.coordinate_update[index][1]+self.list_blit.title_size*2],
                                             title="X",
                                             title_size=20,
                                             tile_color=self.button_delete_title_color,
                                             command=self.deletar_itens).pack())
            
            
        pygame.display.update()
        
        
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
    
    def run(self, events):
        self.main_loop = True
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            self.pos = pygame.mouse.get_pos()
            self.pesquisa = self.input_button.run(pos=self.pos)
            self.imprimir()
            if self.list_blit:
                self.__delete_itens(events)
                for index,but in enumerate(self.button_delete):
                    self.index = index
                    but.run(self.pos)
        if self.list_blit:
            self.list_blit.run(events)
        
        pygame.display.update()
        
        
                    
    def imprimir(self):
        from basico.list import List
        try:
            if self.pesquisa is not None and self.pesquisa != '':
                try:
                    self.consultar_banco = self.consultar(self.pesquisa)
                    self.list_produtos.append(self.consultar_banco[0][1])
                    self.pack()
                    self.inserir_valor()
                    pygame.display.update()
                except:
                    self.pack()
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
        self.button_title_finalizar_gambiarra = f"R$: {self.valor_imprimir}"
        self.pack()
        
        self.window_error = self.window.copy()
        pygame.display.update()
    def update(self):
            self.window.blit(self.value,
                            (self.button_finalizar_coordinate[0],
                            self.button_finalizar_coordinate[1]+self.title_f_size[1]*3))
            self.window_error = self.window.copy()
            pygame.display.update()
    def consultar(self, codigo):
        from bdpython.inserir_produdos import conectar,consultar_produto
        print("consulltar")
        try:
            self.cnn = conectar("bdpython/produtos.db")
            self.consultar_produto = consultar_produto(self.cnn, codigo)
            return self.consultar_produto
        except:
            print("produto não encontrado")
    
    def deletar_itens(self):
        del self.list_produtos[self.index]
        self.inserir_valor()
        self.pack()
        pygame.display.update()
    def main_loop(self):
        self.janelatela = TelaVender()
        self.janelatela.pack()
        loop = True
        while loop:
            for e in pygame.event.get():
                self.janelatela.run(e)

