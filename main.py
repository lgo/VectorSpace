#!/bin/env python2

# foreign imports
import sys, pygame
from pygame.locals import *

# local imports
from display import render
from inputs import input_handler
from events import event_handler

class Game:
   
    # global variables 
    dim = (640, 480)

    # exit sequence
    def quit(self):
        sys.exit()

    # game loop
    def run(self):
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            input_handler()
            event_handler()
            render(self.screen)

    # game entry point
    def __init__(self):

        # pygame initialization
        pygame.init()
        pygame.font.init()

        # display initialization
        pygame.display.set_caption("Vector Space")
        self.screen = pygame.display.set_mode(Game.dim)
        self.clock = pygame.time.Clock()

        self.run()

# program entry point
def main():
    Game()

# if run directly, run program entry
if __name__ == "__main__":
    main()
