from random import randint
from constant import EMPTY
from functions import w_range_y
from entities.troops.Troop import Troop

class Valkyrie(Troop):
  def __init__(self, scene, card, x, y):
    super().__init__(scene, card, x, y)
    self.color = (65, 99, 253)
    self.max_life = 80
    self.life = 80
    self.attack = 25
    self.defence = 20
    self.watch_range = 2
    self.y_search = list(map(lambda x: w_range_y(x)+y, range(0, self.watch_range+1)))

  def search(self, x, _):
    self.enemies = []
    for y in self.y_search:
      future_cell = self.see(x + self.direction, y)
      if type(future_cell) != int and self.is_enemy != future_cell.is_enemy and not future_cell.state.match("dead"):
        self.enemies.append(future_cell)

  def fight(self):
    if len(self.enemies) <= 0:
      self.action_queue(lambda: self.state.use("move", self))
      
    for enemy in self.enemies:
      damage = self.attack - self.attack * (enemy.defence / 100) + (len(self.enemies) - 1) * 4.5 + abs(self.y - enemy.y) * 3
      enemy.life -= damage + min(damage / 4, 10) * (1 if randint(1, 100) <= 5 else 0)
      self.life -= enemy.thorns * damage
      if enemy.life <= 0 or enemy.state.match("dead") or enemy.x != self.x + self.direction:
        self.enemies = list(filter(lambda _enemy: _enemy != enemy, self.enemies))
  
  def tiny_move():
    pass