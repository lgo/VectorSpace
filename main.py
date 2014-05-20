#!/bin/env python2

# foreign imports
import sys, pygame
import pygame.camera
from pygame.locals import *
from pygame import *
# local imports
from player import Player
from display import render
from events import event_handler
from shared import Shared

class Game:
   
    # global variables 
    dim = (640, 480)

    # exit sequence
    def quit(self):
        sys.exit()
    
    def draw_fps(self, screen):
        pass
    # game loop
    def run(self):
        player = Player()
        Shared.groups['player'].add(player)
        while True:
            self.clock.tick(60)

            keys = key.get_pressed()
            if keys[K_DOWN]:
                self.camera['y'] -= 1
            
            event_handler(Shared.groups)
            
            self.draw_fps(self.screen)
            render(self.screen, Shared.groups, self.camera)

    # game entry point
    def __init__(self):

        # pygame initialization
        pygame.init()
        pygame.font.init()
        pygame.camera.init()

        # display initialization
        pygame.display.set_caption("Vector Space")
        self.screen = pygame.display.set_mode(Game.dim)
        self.clock = pygame.time.Clock()

        Shared.groups['player'] = pygame.sprite.Group()
        Shared.groups['particles'] = pygame.sprite.Group()

        self.camera = { 'x':0, 'y':0}
        self.clock = time.Clock()
        self.run()

# program entry point
def main():
    Game()

# if run directly, run program entry
if __name__ == "__main__":
    main()
