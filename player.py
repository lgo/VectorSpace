from pygame import *
from particles import Particles

class Player(sprite.Sprite):
    
    height = 10
    width = 10

    speed = 0.5
    drag = 0.995

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.velx = 0
        self.vely = 0
        self.rect = Rect(self.x, self.y, Player.width, Player.height)
        self.image = Surface( (Player.width, Player.height) )
        self.image.fill( Color("Grey") )
        self.image.convert()
        
    def apply_drag(self):
        self.velx *= Player.drag
        self.vely *= Player.drag
    def apply_drag_old(self):
        if (self.velx > 0):
            self.velx -= Player.drag
            if (self.velx < 0):
                self.velx = 0
        elif (self.velx < 0):
            self.velx += Player.drag
            if (self.velx > 0):
                self.velx = 0

        if (self.vely > 0):
            self.vely -= Player.drag
            if (self.vely < 0):
                self.vely = 0
        elif (self.vely < 0):
            self.vely += Player.drag
            if (self.vely > 0):
                self.vely = 0


    def spawn_particles(self):
        Particles(self.rect.x, self.rect.y)

    def update(self):
        
        # take keyboard input
        keys = key.get_pressed()
        if keys[K_s]:
            self.vely += Player.speed     
        if keys[K_w]:
            self.vely -= Player.speed
            self.spawn_particles()
        if keys[K_d]:
            self.velx += Player.speed
        if keys[K_a]:
            self.velx -= Player.speed

        if keys[K_m]:
            self.velx = 0
            self.vely = 0
        if keys[K_n]:
            self.rect.left = 100
            self.rect.top = 100

        self.rect.x += self.velx
        self.rect.y += self.vely

        self.apply_drag()
        
