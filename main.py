import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  pygame.init()
  clock = pygame.time.Clock()
  delta_time = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  player_init_x = SCREEN_WIDTH / 2
  player_init_y = SCREEN_HEIGHT / 2

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  player = Player(player_init_x, player_init_y)

  Shot.containers = (updatable, drawable, shots)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroidField = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    dt_in_millis = clock.tick(60)
    delta_time = dt_in_millis / 1000
    
    screen.fill("black")

    for to_draw in drawable:
      to_draw.draw(screen) 
    for to_update in updatable:
      to_update.update(delta_time) 

    for asteroid in asteroids:
      if asteroid.detect_collision(player):
        print("Game over!")
        sys.exit()
      for shot in shots:
        if asteroid.detect_collision(shot):
          asteroid.split()
          shot.kill()
    
    pygame.display.flip()

if __name__ == "__main__":
  main()