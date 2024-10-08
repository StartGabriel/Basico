import pygame
from basico.tools import insert_text, get_color, draw_rect
from typing import Union, List, Tuple

pygame.init()

class List:
    def __init__(self,
                 window: pygame.Surface,
                 list_itens: List[str],
                 color: str,
                 title_size: int,
                 coordinate: Union[List[int], Tuple[int, int]],
                 bord_size: Union[List[int]]):
        self.window = window
        self.color = get_color(color)
        self.title_size = title_size
        self.coordinates = coordinate
        self.verify_coordinate = self.coordinates
        print(f"primeira coord: {self.coordinates}")
        self.list_itens = list_itens
        self.bord_size = bord_size
        draw_rect(self.window, self.bord_size, self.coordinates, self.color, 1, 0)
        self.window_backup = window.copy()
        self.window_size = self.window.get_size()
        self.sub_window = pygame.Surface(self.bord_size)
        self.sub_window.fill((17, 17, 17))

    def pack(self):
        self.coordinate_update = []
        self.list_itens_blit = []
        self.coordinate_blit = [0, 0]  # Coordenadas dentro da sub_window
        for texts in self.list_itens:
            self.text_blit = insert_text(text=texts,
                                         color=self.color,
                                         size=self.title_size,
                                         coordinate=self.coordinate_blit)
            self.title_size_y = self.text_blit.get_size()
            self.list_itens_blit.append(self.text_blit)
            self.sub_window.blit(self.text_blit, self.coordinate_blit)
            self.coordinate_blit[1] += self.title_size_y[1]
            self.coordinate_update.append([self.coordinates[0], self.coordinate_blit[1]])

        # Blitar a sub_window (com texto) na janela principal
        self.window.blit(self.sub_window, self.coordinates)
        pygame.display.flip()  # Atualiza a janela após desenhar tudo

    def run(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                self.update_up()
            elif event.y < 0:
                self.update_down()

    def update_up(self):

        self.sub_window.fill((17, 17, 17))  # Limpa o subdisplay
        print("maior que 34")
        for index, text in enumerate(self.list_itens_blit):
            self.coordinate_update[index][1] = self.coordinate_update[index][1] - self.title_size_y[1]
            self.sub_window.blit(self.list_itens_blit[index], (0, self.coordinate_update[index][1]))

        # Atualiza a tela principal com o subdisplay
        self.window.blit(self.sub_window, self.coordinates)
        pygame.display.flip()

    def update_down(self):
            self.sub_window.fill((17, 17, 17))  # Limpa o subdisplay
            print("maior q 34")
            for index, text in enumerate(self.list_itens_blit):
                self.coordinate_update[index][1] = self.coordinate_update[index][1] + self.title_size_y[1]
                self.sub_window.blit(self.list_itens_blit[index], (0, self.coordinate_update[index][1]))

            # Atualiza a tela principal com o subdisplay
            self.window.blit(self.sub_window, self.coordinates)
            pygame.display.flip()
