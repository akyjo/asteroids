import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            lv = self.velocity.rotate(angle)
            x, y = self.position
            la = Asteroid(x, y, self.radius - ASTEROID_MIN_RADIUS)
            la.velocity = 1.2 * lv

            rv = self.velocity.rotate(-angle)
            x, y = self.position
            ra = Asteroid(x, y, self.radius - ASTEROID_MIN_RADIUS)
            ra.velocity = 1.2 * rv
