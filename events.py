import pygame

def event_handler(entities):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    entities['particles'].update()
    entities['player'].update()
