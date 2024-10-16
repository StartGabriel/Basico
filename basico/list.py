import pygame
from basico.tools import insert_text, get_color, draw_rect, collidepoint
from typing import Union, List, Tuple
from basico.button import Button

pygame.init()

class List:
    def __init__(self,
                 window: pygame.Surface,
                 list_itens: List[str],
                 color: str,
                 title_size: int,
                 coordinate: Union[List[int], Tuple[int, int]],
                 bord_size: Union[List[int]],
                 bord_color: str = "dark",
                 tag:str = None):
        self.window = window
        self.color = get_color(color)
        self.title_size = title_size
        self.coordinates = coordinate
        self.verify_coordinate = self.coordinates
        self.list_itens = list_itens
        self.bord_size = bord_size
        self.bord_color = get_color(bord_color)
        draw_rect(self.window, self.bord_size, self.coordinates, self.color, 1, 0)
        self.window_backup = window.copy()
        self.window_size = self.window.get_size()
        self.sub_window = pygame.Surface(self.bord_size)
        self.sub_window.fill(self.bord_color)
        self.tag = tag
        self.buttons:Button = []
        
        

    def pack(self):
        self.iten_verify= []
        self.coordinate_update = []
        self.list_itens_blit = []
        self.coordinate_blit = [0, 0]
        for texts in self.list_itens:
            self.iten_verify.append(False)
            self.text_blit = insert_text(text=texts,
                                         color=self.color,
                                         size=self.title_size,
                                         coordinate=self.coordinate_blit,
                                         background_color="black")
            self.title_size_y = self.text_blit.get_size()
            self.list_itens_blit.append(self.text_blit)
            self.sub_window.blit(self.text_blit, self.coordinate_blit)
            self.buttons.append(Button(window= self.sub_window,
                                   size= [self.title_size,self.title_size],
                                   color= self.color,
                                   coordinate=[self.bord_size[0]-self.title_size, self.coordinate_blit[1]+self.title_size_y[1]/2],
                                   title= "X",
                                   title_size= self.title_size,
                                   tile_color="red",
                                   command=self.excluirs).pack())
            print(self.bord_size[0]-self.title_size+self.coordinates[0])
            self.coordinate_blit[1] += self.title_size_y[1]
            self.coordinate_update.append([self.coordinates[0], self.coordinate_blit[1]])
        if self.tag:
            self.tags()
        
        # Blitar a sub_window (com texto) na janela principal
        self.window.blit(self.sub_window, self.coordinates)
        pygame.display.flip()  # Atualiza a janela após desenhar tudo

    def run(self, event):

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                self.update_up()
            elif event.y < 0:
                self.update_down()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pos = pygame.mouse.get_pos()
            for index, but in enumerate(self.buttons):
                try:
                    self.clique = collidepoint(self.buttons[index].coordinate, [self.title_size,self.title_size], self.pos, self.coordinates)
                    self.iten_verify[index] = self.clique
                    if self.clique == True:
                        print(self.iten_verify)
                        self.excluirs(index)
                except:
                    pass
    def update_up(self):

        self.sub_window.fill(self.bord_color)  # Limpa o subdisplay
        for index, text in enumerate(self.list_itens_blit):
            self.coordinate_update[index][1] = self.coordinate_update[index][1] - self.title_size_y[1]
            self.sub_window.blit(self.list_itens_blit[index], (0, self.coordinate_update[index][1]))
            self.buttons[index].coordinate = [self.bord_size[0]-self.title_size, self.coordinate_update[index][1]+self.title_size_y[1]/2]
            self.buttons[index].pack()

        # Atualiza a tela principal com o subdisplay
        self.window.blit(self.sub_window, self.coordinates)
        pygame.display.flip()

    def update_down(self):
            self.sub_window.fill(self.bord_color)  # Limpa o subdisplay
            for index, text in enumerate(self.list_itens_blit):
                self.coordinate_update[index][1] = self.coordinate_update[index][1] + self.title_size_y[1]
                self.sub_window.blit(self.list_itens_blit[index], (0, self.coordinate_update[index][1]))
                self.buttons[index].coordinate = [self.bord_size[0]-self.title_size, self.coordinate_update[index][1]+self.title_size_y[1]/2]

                self.buttons[index].pack()
            # Atualiza a tela principal com o subdisplay
            self.window.blit(self.sub_window, self.coordinates)
            pygame.display.flip()
    def update(self):
        self.sub_window.fill(self.bord_color)  # Limpa o subdisplay
        for index, text in enumerate(self.list_itens_blit):
            self.coordinate_update[index][1] = self.coordinate_update[index][1]
            self.sub_window.blit(self.list_itens_blit[index], (0, self.coordinate_update[index][1]))
            self.buttons[index].coordinate = [self.bord_size[0]-self.title_size, self.coordinate_update[index][1]]

            self.buttons[index].pack()
        # Atualiza a tela principal com o subdisplay
        self.window.blit(self.sub_window, self.coordinates)
        pygame.display.flip()

    def tags(self):
        pass
    
    def excluirs(self, index):
        try:
            del self.list_itens[index]
            del self.list_itens_blit[index]
          
            pygame.display.flip()
            self.update()
        except:
            pass