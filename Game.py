import pygame
from objects.Mouse import Mouse
from objects.Scene import Scene

class Game:
  tick: int = 60
  scenes: list[Scene] = []
  current_scene: Scene = None

  def __init__(self, name: str, width: int, height: int, image: str = None):
    pygame.display.set_caption(name)
    if image != None:
      pygame.display.set_icon(pygame.image.load(image))
    self.context = pygame.display.set_mode((width, height))
    
    self.screen_width = width
    self.screen_height = height

    self.mouse = Mouse()

  def set_tick(self, tick):
    self.tick = tick

  def get_tick(self):
    return self.tick

  def add_scene(self, scene: Scene):
    self.scenes.append(scene)

  def update(self, delta):
    if self.current_scene == None:
      self.current_scene = self.scenes[0]

    if not self.current_scene.inited:
      self.current_scene.init()
      self.current_scene.inited = True

    for entity in self.current_scene.entities:
      if not entity.inited:
        entity.init()
        entity.inited = True
      
    self.mouse.update()
    self.current_scene.update(delta)

    for entity in self.current_scene.entities:
      entity.update(delta)

  def draw(self):
    self.context.fill((0, 0, 0))
    self.current_scene.draw()
    for entity in self.current_scene.entities:
      entity.draw()
    