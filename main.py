import pygame
from constants import *

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  pygame.init()
  clock = pygame.time.Clock()
  delta_time = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill("black")
    pygame.display.flip()
    dt_in_millis = clock.tick(60)
    delta_time = dt_in_millis / 1000

if __name__ == "__main__":
  main()