import pygame
from Game import Game

pygame.init()

game = Game(
  "AutoWar", 
  800, 
  600
)
# game.add_scene()
game.set_tick(60)

clock = pygame.time.Clock()
running = True
while running:
  delta = clock.tick(game.get_tick()) / 1000
  # game.update(delta)
  game.draw()

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      exit(0)
