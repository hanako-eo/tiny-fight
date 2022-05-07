import pygame
from Game import Game
from scenes.MenuScene import MenuScene
from scenes.PlateScene import PlateScene
from scenes.OverlayScene import OverlayScene
from scenes.LocalRoomScene import LocalRoomScene

pygame.init()

game = Game(
  "Tiny Fight", 
  800, 
  600,
  image="./assets/icon.png"
)

game.add_scene(MenuScene(game))
game.add_scene(LocalRoomScene(game))
game.add_scene(PlateScene(game))
game.add_scene(OverlayScene(game))

game.set_tick(60)

clock = pygame.time.Clock()
running = True
while running:
  delta = clock.tick(game.get_tick()) / 1000
  game.delta = delta
  game.update(delta)
  game.draw()

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.mod >= 4096: event.mod -= 4096

      if event.mod == pygame.KMOD_NONE:
        game.keys.append(event)
      else:
        game.mods.append(event)

    elif event.type == pygame.KEYUP:
      if event.mod >= 4096: event.mod -= 4096

      if event.mod == pygame.KMOD_NONE:
        game.keys = list(filter(lambda key: key.key != event.key, game.keys))
      else:
        game.mods = list(filter(lambda key: key.key != event.key, game.mods))
        
    elif event.type == pygame.QUIT:
      running = False
      game.client.close()
      pygame.quit()
      exit(0)
