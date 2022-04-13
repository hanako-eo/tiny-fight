import pygame
import draw
from constant import EMPTY
from functions import pos
from objects.Entity import Entity
from objects.Timer import *
from states.machines.TroopMachine import TroopMachine

class Troop(Entity):
  def __init__(self, scene, x: int, y: int):
    super().__init__(scene, "Troop", x, y, 60, 60)
    self.color = (0, 200, 0)

    self.state = TroopMachine(self)
    self.timer = Tick(self.state.current.update, 60)
    self.enemy = x > 7
    self.moved = False

    self.max_life = 100
    self.life = 100
    self.attack = 20
    self.defence = 20
    self.thorns = 0
    self.id = x+y

  def update(self, delta):
    self.timer.update(delta)
    if self.life <= 0:
      self.state.use("dead", self)

  def move(self, x, y):
    i = -2 * int(self.enemy) + 1
    if x+i < 0 or x+i >= 10:
      return False

    next_pos = (x + i, y)
    next_cell = self.scene.plate.get(next_pos)
    if next_cell == EMPTY:
      self.scene.plate.move(next_pos, (x, y))
    elif next_cell.enemy and not next_cell.state.match("dead"):
      self.state.use("attack", self, next_cell)
      next_cell.state.use("attack", next_cell, self)
      return False
    elif next_cell.state.match("dead") or not next_cell.state.match("attack") and next_cell.move(x + i, y):
      self.scene.plate.move(next_pos, (x, y))

    self.moved = True
    return True

  def draw(self, x: int, y: int):
    life = self.width * (self.life / self.max_life)
    if life < 0:
      return

    draw.rect(
      self.game.context,
      self.color,
      pos(x), 
      pos(y), 
      self.width, 
      self.height
    )
    if not self.state.match("wait"):
      draw.rect(
        self.game.context,
        (255, 0, 0),
        pos(x), 
        pos(y),
        life,
        4
      )
  
  def destroy(self):
    super().destroy()
    self.scene.plate.remove(self)
  