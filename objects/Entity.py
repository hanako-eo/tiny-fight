from __future__ import annotations
from typing import TYPE_CHECKING
from objects.EventBus import EventBus
if TYPE_CHECKING:
  from Game import Game
  from Scene import Scene

class Entity(EventBus):
  scene: Scene = None
  game: Game = None

  def __init__(self, scene: Scene, name: str, x: int, y: int, width: int, height: int):
    super().__init__()
    self.inited = False

    self.name = name
    self.game = scene.game
    self.scene = scene
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def collision(self, test: Entity) -> bool:
    return self.x < test.x + test.width and self.x + self.width > test.x and self.y < test.y + test.height and self.y + self.height > test.y
    
  def init(self):
    pass

  def prescene_draw(self):
    pass

  def postoverlay_draw(self):
    pass

  def draw(self):
    pass

  def update(self, delta: float):
    pass

  def action_queue(self, callback):
    self.game.queue.append(callback)

  def destroy(self):
    self.scene.entities = list(filter(lambda entity: entity != self, self.scene.entities))
