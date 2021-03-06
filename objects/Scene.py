from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from Game import Game
  from Entity import Entity

class Scene:
  game: Game = None
  entities: list[Entity] = []

  def __init__(self, game: Game, name: str):
    self.inited = False
    self.name = name
    self.game = game
    self.entities = []

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
