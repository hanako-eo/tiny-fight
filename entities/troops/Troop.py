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
    self._speed = 60

    self.state = TroopMachine(self)
    self.timer = Tick(self.state.current.update, self._speed)
    self.enemy = x > 7
    self.moved = False

    self.max_life = 100
    self.life = 100
    self.attack = 20
    self.defence = 20
    self.thorns = 0

    self.watch_range = (1, 0)
    self.id = x+y

  def get_speed(self):
    return self._speed

  def set_speed(self, value):
    self._speed = value
    self.timer.set_waiting(value)

  def update(self, delta):
    self.timer.update(delta)
    if self.life <= 0:
      self.state.use("dead", self)

  def move(self, x, y):
    direction = -2 * int(self.enemy) + 1
    if x+direction < 0 or x+direction >= 10:
      self.state.use("finish", self)
      return False

    enemy = None
    for i in range(1, self.watch_range[0]+1):
      future_cell = self.see(x + direction * i, y)
      if future_cell != EMPTY and self.enemy != future_cell.enemy and not future_cell.state.match("dead"):
        enemy = future_cell
        break

    if enemy != None:
      self.state.use("attack", self, enemy)
      return False

    next_cell = self.see(x + direction, y)

    if next_cell == EMPTY or next_cell.state.match("dead") or not next_cell.state.match("attack") and next_cell.timer.can(self.game.delta) and next_cell.move(x + direction, y):
      self.action_queue(lambda: self.scene.plate.move((x + direction, y), (x, y)))
      self.moved = True
      return True

  def see(self, x, y):
    if 10 > x > 0:
      return self.scene.plate.get((x, y))
    return EMPTY


  def draw(self, x: int, y: int):
    life = self.width * (self.life / self.max_life)
    if life < 0:
      return

    x = pos(x)
    y = pos(y)

    draw.fill(self.color)
    draw.rect(self.game.context, x, y, self.width, self.height)
    draw.reset()
    if not self.state.match("wait"):
      draw.fill((255, 0, 0, 0.5))
      draw.rect(self.game.context, x, y, self.width, 4)
      draw.reset()
      draw.fill((255, 0, 0))
      draw.rect(self.game.context, x, y, life, 4)
      draw.reset()
  
  def destroy(self):
    super().destroy()
    self.scene.plate.remove(self)
    self.state = None
    self.timer = None
  