import pygame
from constants import *
from player import Player

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
  player = Player(player_init_x, player_init_y)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    dt_in_millis = clock.tick(60)
    delta_time = dt_in_millis / 1000
    screen.fill("black")
    player.draw(screen)
    player.update(delta_time)
    pygame.display.flip()

if __name__ == "__main__":
  main()