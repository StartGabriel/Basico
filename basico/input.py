import pygame
from sys import exit


from basico.tools import get_color, insert_text, get_mid
from typing import Union, List, Tuple
from basico.button import Button
from pycss.buttoncss import Shadow

pygame.init()
class Input:
    def __init__(self,
                 window: pygame.Surface,
                 title:str,
                 size:Union[List[int],Tuple[int,int]],
                 coordinate:Union[List[int],Tuple[int,int]],
                 color:str,
                 background:str=None,
                 title_size:int = 30,
                 text_color:str = "black",
                 width:int = 50,
                 border_color:str = "black",
                 border_color_clicked:str = "green",
                 shadow:Shadow = None,
                 tag:str = "text"):
        self.window = window
        self.size = size
        self.coordinate = coordinate
        self.color = get_color(color)
        self.background = background
        self.title = title
        self.title_backup = title
        self.title_size= title_size
        self.text_color = get_color(text_color)
        self.width = width
        self.tag = tag
        self.window_backup = window.copy()
        self.color_clicked = border_color_clicked
        self.border = True
        self.border_color = border_color
        self.border_color_backup = self.border_color
        self.shadow = shadow
        self.first = True

    def pack(self):
        from pycss.buttoncss import ButtonCss, Shadow
        self.mod = ButtonCss()
        self.but_input = Button(window= self.window,
                                size= self.size,
                                color= self.color,
                                coordinate= self.coordinate,
                                title='',
                                title_size= self.title_size,
                                background= self.background,
                                width=self.width,
                                command=self.get_text)
        if self.shadow is not None:
            self.shadow.pack(self.but_input)
            self.shadow.visibility = 0
        self.but_input.pack()
        self.mod.border([self.but_input],2,self.border_color)
        self.window_backup_pack = self.window.copy()
        self.but_input.title = self.title
        self.but_input.pack()
        self.size_title_blit = self.but_input.title_size_blit
    def run(self,pos):
        self.retorned= self.but_input.run(pos=pos)
        return self.retorned

    
    def get_text(self):
        self.loop = True
        self.key_return = ''
        self.title = ''
        self.pack()
        while self.loop:
            self.first_click()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.loop = False
                    pygame.quit()
                    exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.pos_verify = pygame.mouse.get_pos()
                    self.pos_verify_click= self.but_input.rect.collidepoint(self.pos_verify)
                    
                    if self.pos_verify_click == False:
                        self.clear()
                        return self.key_return
                    
                if events.type == pygame.KEYDOWN:
                    self.key_pressed = pygame.key.get_pressed()
                    if events.unicode.isprintable():
                        self.key = events.unicode
                        self.key_return+=self.key
                        self.update()
                    if events.key == pygame.K_BACKSPACE:
                        self.k_backspace()
                    
                    if events.key == pygame.K_RETURN:
                        self.clear()
                        return self.key_return
                        
                    if self.size_validation [0]>= self.size[0]:
                        self.k_backspace()
            pygame.display.flip()

    def first_click(self):
        if self.first == True:
            from pycss.buttoncss import ButtonCss
            self.mod = ButtonCss()
            self.mod.border([self.but_input],2,self.color_clicked)
        self.first = False

                        
    def update(self):
        self.title = ''
        self.border_color = self.color_clicked
        self.pack()
        self.text_blit = insert_text(self.key_return,self.text_color,self.title_size)
        self.size_validation = self.text_blit.get_size()
        self.text_blit_coordinate = get_mid(object_size=self.size,
                                            object_size_target=self.size_title_blit,
                                            coordinate_object=self.coordinate)
        self.title = self.key_return
        self.pack()  
        pygame.display.flip()
        
    def k_backspace(self):
        self.key_return = self.key_return[:-1]
        self.update()
    
    def clear(self):
        if self.tag == "all":
            self.window.blit(self.window_backup,(0,0))
        if self.tag == "text":
            self.key_return = ''
            self.update()
        if self.tag == "not":
            self.border_color = self.border_color_backup
            if self.title != '':
                self.title = self.key_return
                print(self.border_color_backup)
                from pycss.buttoncss import ButtonCss
                self.mod = ButtonCss()
                self.mod.border([self.but_input],2,self.border_color_backup)
                self.pack()
                self.first = True
            else:
                self.title = self.title_backup
                print(self.border_color_backup)
                from pycss.buttoncss import ButtonCss
                self.mod = ButtonCss()
                self.mod.border([self.but_input],2,self.border_color_backup)
                self.pack()
                self.first = True

    
    def get_but(self):
        return self.but_input