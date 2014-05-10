import pygame

def render(screen):
    screen.fill( (0, 0, 0) )
    pygame.draw.rect(screen, (255, 255, 255), (0, 100, 30, 30))
    pygame.display.flip()
