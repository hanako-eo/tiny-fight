import pygame
import draw
from constant import EMPTY
from functions import pos
from objects.Entity import Entity
from objects.Timer import *
from states.machines.TroopMachine import TroopMachine

class Troop(Entity):
  def __init__(self, scene, x: int, y: int, cell_pos: list[int, int]):
    super().__init__(scene, "Troop", x, y, 60, 60)
    self.cell_pos = cell_pos

    self.scene.entities.append(self)
    self.color = (0, 200, 0)

    self.state = TroopMachine(self)
    self.timer = Tick(self.state.current.update, 30)
    self.enemy = cell_pos[0] > 7

    self.max_life = 100
    self.life = 100
    self.attack = 20
    self.defence = 20

  def update(self, delta):
    self.timer.update(delta)
    if self.life <= 0:
      self.destroy()

  def move(self):
    i = -2 * int(self.enemy) + 1
    [x, y] = self.cell_pos
    if x+i < 0 or x+i >= 10:
      return

    next_cell = self.scene.plate[x + i][y]
    if next_cell == EMPTY or next_cell.enemy == self.enemy:
      self.scene.plate[x][y], self.scene.plate[x + i][y] = next_cell, self.scene.plate[x][y]
      self.cell_pos[0] += i
      self.x = pos(x+i)
      self.y = pos(y)
    else:
      self.state.use("attack", self, next_cell)
      

  def postoverlay_draw(self):
    draw.rect(
      self.game.context,
      self.color,
      self.x, 
      self.y, 
      self.width, 
      self.height
    )
  
  def destroy(self):
    super().destroy()
    [x, y] = self.cell_pos
    self.scene.plate[x][y] = EMPTY
  