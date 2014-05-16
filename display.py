from pygame import Color
import pygame
from pygame import Rect

def draw(screen, group, camera):
    for sprite in group:
        screen.blit(sprite.image, Rect(sprite.rect.x + camera['x'],
            sprite.rect.y + camera['y'], sprite.rect.width, sprite.rect.height))

    # method 2 of drawing - no camera modification
    # group.draw(screen)

def render(screen, entities, camera):
   
    # bg
    screen.fill( Color("Black") )
    
    # draw objeccts
    draw(screen, entities['particles'], camera)
    draw(screen, entities['player'], camera)
    
    # write screen buffer
    pygame.display.flip()
