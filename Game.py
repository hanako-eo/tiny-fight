import pygame
from objects.Scene import Scene

class Game:
  tick = 60

  def __init__(self, name: str, width: int, height: int):
    pygame.display.set_caption(name)
    self.context = pygame.display.set_mode((width, height))
    
    self.screen_width = width
    self.screen_height = height

    self.scenes = []
    self.current_scene = None

  def set_tick(self, tick):
    self.tick = tick

  def get_tick(self):
    return self.tick

  def add_scene(self, scene: Scene):
    self.scenes.append(scene)

  def update(self, delta):
    if self.current_scene == None:
      self.current_scene = self.scenes[0]
      
    self.current_scene.update(delta)

  def draw(self):
    self.context.fill((0, 0, 0))
    # self.current_scene.draw()
    