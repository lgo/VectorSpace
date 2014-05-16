from pygame import *
from shared import Shared


class Particles():
    def __init__(self, x, y):
        random = 5 #TODO random placeholder for amount of particles generated
        self.timer = 600 #TODO kill particle group after 10s or randomly close to timer point
        for i in range(random):
            Shared.groups['particles'].add(Particle(x, y + 5))

class Particle(sprite.Sprite):
    count = 0
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, 2, 2)
        self.image = Surface( (2, 2) )
        self.image.fill(Color("Orange"))
        self.image.convert()
        Particle.count += 1
        self.ticks = 40
        print ("Particle count: %s" % Particle.count)
    def update(self):
        self.rect.y += 1
        self.ticks -= 1
        if self.ticks <= 0:
            print ("I'm dead!")
            Particle.count -= 1
            Shared.groups['particles'].remove(self)
