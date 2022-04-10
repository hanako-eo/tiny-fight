import pygame
import draw
from constant import EMPTY
from functions import pos
from objects.Entity import Entity
from objects.Timer import Tick

class Troop(Entity):
  def __init__(self, scene, x: int, y: int, cell_pos: list[int, int]):
    super().__init__(scene, "Troop", x, y, 60, 60)
    self.cell_pos = cell_pos

    self.scene.entities.append(self)
    self.color = (0, 200, 0)

    self.move = Tick(self.move, 120)
    self.enemy = False

  def update(self, delta):
    self.move.update()

  def move(self):
    i = -2 * int(self.enemy) + 1
    [x, y] = self.cell_pos
    if x+i >= 0 and x+i < 10 and self.scene.plate[x + i][y] == EMPTY:
      self.scene.plate[x][y], self.scene.plate[x + i][y] = self.scene.plate[x + i][y], self.scene.plate[x][y]
      self.cell_pos[0] += i
      self.x = pos(x+i)
      self.y = pos(y)

  def postoverlay_draw(self):
    draw.rect(
      self.game.context,
      self.color,
      self.x, 
      self.y, 
      self.width, 
      self.height
    )
  