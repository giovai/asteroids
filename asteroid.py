import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_VELOCITY_MULTIPLIER

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
     pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    new_angle = random.uniform(20, 50)
    forward_a = self.velocity.rotate(new_angle)
    forward_b = self.velocity.rotate(-new_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_a.velocity = forward_a * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
    asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_b.velocity = forward_b * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
