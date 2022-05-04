import pygame
import draw
from random import randint
from constant import EMPTY, RESERVE
from functions import pos
from objects.Entity import Entity
from objects.Timer import *
from states.machines.TroopMachine import TroopMachine

class Troop(Entity):
  def __init__(self, scene, card, x: int, y: int):
    super().__init__(scene, "Troop", x, y, 60, 60)
    self.card = card
    self.color = (0, 200, 0)
    self._speed = 60

    self.state = TroopMachine(self)
    self.timer = Tick(self.state.current.update, self._speed)
    self.is_enemy = x > 7
    self.direction = -2 * int(self.is_enemy) + 1
    self.moved = False

    self.max_life = 100
    self.life = 100
    self.attack = 20
    self.defence = 20
    self.thorns = 0

    self.watch_range = 1
    self.id = x+y
    self.enemies = []

  def get_speed(self):
    return self._speed

  def set_speed(self, value):
    self._speed = value
    self.timer.set_waiting(value)

  def update(self, delta):
    self.timer.update(delta)
    if self.life <= 0:
      self.state.use("dead", self)
      self.destroy()

  def see(self, x, y):
    if 10 > x > -1 and 5 > y > -1:
      return self.scene.plate.get((x, y))
    return EMPTY

  def search(self, x, y):
    self.enemies = []
    for i in range(1, self.watch_range+1):
      future_cell = self.see(x + self.direction * i, y)
      if type(future_cell) != int and self.is_enemy != future_cell.is_enemy and not future_cell.state.match("dead"):
        self.enemies.append(future_cell)
        break
    
  def fight(self):
    if len(self.enemies) <= 0:
      self.action_queue(lambda: self.state.use("move", self))
      
    for enemy in self.enemies:
      damage = self.attack - self.attack * (enemy.defence / 100)
      enemy.life -= damage + min(damage / 4, 8) * (1 if randint(1, 100) <= 5 else 0)
      self.life -= enemy.thorns * damage
      if enemy.life <= 0 or enemy.state.match("dead"):
        self.enemies = list(filter(lambda _enemy: _enemy != enemy, self.enemies))

  def move(self, x, y):
    if x+self.direction < 0 or x+self.direction >= 10:
      self.state.use("finish", self)
      return True

    self.search(x, y)

    if len(self.enemies) > 0:
      self.state.use("attack", self)
      return False

    next_cell = self.see(x + self.direction, y)
    if next_cell == RESERVE:
      return False

    if next_cell == EMPTY or next_cell.state.match("dead") or not next_cell.state.match("attack") and next_cell.timer.can(self.game.delta) and next_cell.move(x + self.direction, y):
      self.scene.plate.set((x + self.direction, y), RESERVE)
      self.action_queue(lambda: self.scene.plate.set((x + self.direction, y), EMPTY))
      self.action_queue(lambda: self.scene.plate.move((x + self.direction, y), (x, y)))
      self.moved = True
      return True
    return False

  def draw(self, x: int, y: int):
    life = self.width * (self.life / self.max_life)
    if life <= 0:
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
  