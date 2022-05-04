from constant import EMPTY
from functions import w_range_y
from entities.troops.Troop import Troop

class Valkyrie(Troop):
  def __init__(self, scene, card, x, y):
    super().__init__(scene, card, x, y)
    self.color = (65, 99, 253)
    self.max_life = 80
    self.life = 80
    self.attack = 30
    self.defence = 20
    self.watch_range = 2

  def search(self, x, y, direction):
    self.enemies = []
    for i in range(0, self.watch_range+1):
      future_cell = self.see(x + direction, y + w_range_y(i))
      if future_cell != EMPTY and self.is_enemy != future_cell.is_enemy and not future_cell.state.match("dead"):
        self.enemies.append(future_cell)
  
  def tiny_move():
    pass