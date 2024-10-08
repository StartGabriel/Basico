import pygame

from basico.list import List


pygame.init()

janela = pygame.display.set_mode((600,600))

teste = List(janela,["abacate","banana","coentro"],"white",30,[10,100],[500,500])
teste.pack()

while True:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEWHEEL:
            teste.run(events)
    pygame.display.flip()