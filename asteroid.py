import pygame
from circleshape import CircleShape
from constants import *
import random
from score import Score

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        score = Score()
        score.add_points(100)
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_vector_one = self.velocity.rotate(random_angle)
        new_vector_two = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
    
        asteroid_one.velocity = new_vector_one * 1.2
        asteroid_two.velocity = new_vector_two * 1.2
        return asteroid_one, asteroid_two