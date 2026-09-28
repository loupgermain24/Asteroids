import random

import pygame

import circleshape
import constants
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.color = "white"

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen, self.color, self.position, self.radius, constants.LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        new_vector = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_vector * 1.2
        if new_radius > constants.ASTEROID_MIN_RADIUS:
            asteroid.color = "Yellow"
        else: asteroid.color = "red"
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector2 * 1.2
        if new_radius > constants.ASTEROID_MIN_RADIUS:
            asteroid2.color = "Yellow"
        else: asteroid2.color = "red"
