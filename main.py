import pygame
from Game import Game
from scenes.PlateScene import PlateScene

pygame.init()

game = Game(
  "AutoWar", 
  800, 
  600,
  image="./assets/icon.png"
)

game.add_scene(
  PlateScene(game, "PlateScene")
)

game.set_tick(60)

clock = pygame.time.Clock()
running = True
while running:
  delta = clock.tick(game.get_tick()) / 1000
  game.update(delta)
  game.draw()

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      exit(0)
