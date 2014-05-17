from pygame import *
from shared import Shared
from random import randint

class Particles():
    def __init__(self, x, y, engine_active):
        if (engine_active):
            random = randint(2,4)
        else:
            random = 1
        for i in range(random):
            Shared.groups['particles'].add(Particle(x + randint(-10, 10), y + randint(0, 10)))

class Particle(sprite.Sprite):
    colors = [ 0xFFC904, 0xE8A004, 0xFF9808, 0xE86804, 0xFF4D04 ]
    def fill(self, alpha=255):
        self.image = Surface((2,2))
        self.image.fill(self.color)
        if alpha == 255:
            self.image.convert()
        else:
            self.image.set_alpha(alpha)
            self.image.convert_alpha()

    
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.color = Particle.colors[randint(0,4)]
        self.rect = Rect(x, y, 2, 2)
        self.fill(0)
        self.ticks = 40

    def update(self):
        self.rect.y += 0
        self.ticks -= 1
        if self.ticks < 36 and self.ticks > 26:
            self.fill(25 * (44 - self.ticks))
        if self.ticks == 26:
            self.fill()
        if self.ticks < 19:
            self.fill(255 - 12 * (18 - self.ticks))
        if self.ticks == 0:
            Shared.groups['particles'].remove(self)
