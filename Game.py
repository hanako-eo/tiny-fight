import pygame
from objects.Mouse import Mouse
from objects.Scene import Scene
from objects.networking.Client import Client

class Game:
  tick: int = 60
  scenes: list[Scene] = []
  current_scene: Scene = None
  overlays: list[Scene] = []
  keys = []
  mods = []
  
  mouse: Mouse

  def __init__(self, name: str, width: int, height: int, image: str = None):
    pygame.display.set_caption(name)
    if image != None:
      pygame.display.set_icon(pygame.image.load(image))
    self.context = pygame.display.set_mode((width, height))
    
    self.screen_width = width
    self.screen_height = height

    self.client = Client()
    self.change_scene_queue = []
    self.queue = []
    self.mouse = Mouse(self)
    self.delta = 0

  def set_tick(self, tick):
    self.tick = tick

  def get_tick(self) -> int:
    return self.tick

  def add_scene(self, scene: Scene):
    self.scenes.append(scene)

  def change_scene(self, name: str):
    self.change_scene_queue.append(name)

  def add_overlay(self, overlay_name: str):
    for scene in self.scenes:
      if scene.name == overlay_name:
        self.overlays.append(scene)
        return

  def remove_overlay(self, overlay_name: str):
    self.overlays = list(filter(lambda overlay: overlay.name != overlay_name, self.overlays))

  def update(self, delta: float):
    if self.current_scene == None:
      self.current_scene = self.scenes[0]

    for name in self.change_scene_queue:
      for scene in self.scenes:
        if scene.name == name:
          self.current_scene = scene
          break
    self.change_scene_queue = []

    for action in self.queue:
      action()
    self.queue = []

    self.mouse.update()

    self.__update__(delta, self.current_scene)
    for overlay in self.overlays:
      self.__update__(delta, overlay)
  
  def __update__(self, delta: float, scene: Scene):
    if not scene.inited:
      scene.init()
      scene.inited = True

    for entity in scene.entities:
      if not entity.inited:
        entity.init()
        entity.inited = True
      
    scene.update(delta)

    for entity in scene.entities:
      entity.update(delta)

  def draw(self):
    self.context.fill((0, 0, 0))

    for overlay in self.overlays:
      overlay.prescene_draw()
      for entity in overlay.entities:
        entity.prescene_draw()

    self.__draw__(self.current_scene)
    for overlay in self.overlays:
      self.__draw__(overlay)

    self.current_scene.postoverlay_draw()
    for entity in self.current_scene.entities:
      entity.postoverlay_draw()

  def __draw__(self, scene: Scene):
    scene.draw()
    for entity in scene.entities:
      entity.draw()

    