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
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, 2, 2)
        self.image = Surface( (2, 2) )
        self.image.fill(Color("Orange"))
        self.image.set_alpha(0)
        self.image.convert_alpha()
        self.ticks = 40
    def update(self):
        self.rect.y += 0
        self.ticks -= 1
        if self.ticks < 36 and self.ticks > 26:
            self.image = Surface( (2,2) )
            self.image.fill(Color("Orange"))
            self.image.set_alpha(25 * (44 - self.ticks))
            self.image.convert_alpha()
        if self.ticks == 26:
            self.image = Surface( (2,2) )
            self.image.fill(Color("Orange"))
            self.image.convert()
        if self.ticks < 19:
            self.image = Surface( (2, 2) )
            self.image.fill(Color("Orange"))
            self.image.set_alpha(255 - 12 * (18 - self.ticks))
            self.image.convert_alpha()
        if self.ticks == 0:
            Shared.groups['particles'].remove(self)
