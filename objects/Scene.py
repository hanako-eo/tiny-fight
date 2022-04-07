from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from Game import Game

class Scene:
  game: Game

  def __init__(self, game: Game, name: str):
    self.inited = False
    self.name = name
    self.game = game
    self.entities = []

  def init(self):
    self.inited = True

  def draw(self):
    for entity in self.entities:
      entity.draw()
    
  def update(self, delta: float):
    for entity in self.entities:
      entity.update(delta)
