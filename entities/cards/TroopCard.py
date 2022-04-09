from typing import Type
import pygame
from objects.Entity import Entity
from entities.troops.Troop import Troop

class TroopCard(Entity):
  deck_index: int
  troop: Type[Troop]

  def __init__(self, scene, deck_index: int, cell_size: int):
    super().__init__(scene, "TroopCard", 0, 0, 40, 40)
    self.cell_size = cell_size
    self.deck_index = deck_index

    self.scene.entities.append(self)

  def init(self):
    self.color = (0, 0, 200)
    self.x = self.deck_index * self.cell_size + 100 + (self.cell_size - self.width) / 2
    self.y = self.game.screen_height - 100 - self.cell_size - (self.cell_size - self.height) / 2

  def update(self, _):
    hover = self.collision(self.game.mouse)
    if hover:
      self.width = 50
      self.height = 50
    else:
      self.width = 40
      self.height = 40
    self.x = self.deck_index * self.cell_size + 100 + (self.cell_size - self.width) / 2
    self.y = self.game.screen_height - 100 - self.cell_size + (self.cell_size - self.height) / 2

    if hover and self.game.mouse.left:
      self.game.mouse.selection = self.troop

  def postoverlay_draw(self):
    pygame.draw.rect(
      self.game.context,
      self.color,
      [
        self.x, 
        self.y, 
        self.width, 
        self.height
      ],
    )
  