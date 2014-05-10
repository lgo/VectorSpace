import pygame

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
