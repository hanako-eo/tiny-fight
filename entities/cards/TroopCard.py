from typing import Type
import pygame
import draw

from constant import CELL_SIZE
from objects.Entity import Entity
from entities.troops.Troop import Troop

class TroopCard(Entity):
  deck_index: int
  troop: Type[Troop]

  def __init__(self, scene, deck_index: int, troop: Type[Troop]):
    super().__init__(scene, "TroopCard", 0, 0, 40, 40)
    self.deck_index = deck_index
    self.troop = troop

    self.scene.entities.append(self)

  def init(self):
    self.color = (0, 0, 200)
    self.x = self.deck_index * CELL_SIZE + 100 + (CELL_SIZE - self.width) / 2
    self.y = self.game.screen_height - 100 - CELL_SIZE - (CELL_SIZE - self.height) / 2

  def update(self, _):
    hover = self.collision(self.game.mouse)
    if hover:
      self.width = 50
      self.height = 50
    else:
      self.width = 40
      self.height = 40
    self.x = self.deck_index * CELL_SIZE + 100 + (CELL_SIZE - self.width) / 2
    self.y = self.game.screen_height - 100 - CELL_SIZE + (CELL_SIZE - self.height) / 2

    if hover and self.game.mouse.left:
      self.game.mouse.selection = self.troop

  def postoverlay_draw(self):
    draw.fill(self.color)
    draw.rect(
      self.game.context,
      self.x, 
      self.y, 
      self.width, 
      self.height
    )
    draw.reset()
  