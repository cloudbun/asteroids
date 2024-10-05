import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Common Constants
            velocity_scale = 1.2
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # First Asteroid Split
            first_vector = self.velocity.rotate(random_angle)
            asteroid_first = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_first.velocity = first_vector * velocity_scale

            # Second Asteroid Split
            second_vector = self.velocity.rotate(-random_angle)
            asteroid_second = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_second.velocity = second_vector * velocity_scale