from entities.troops.Troop import Troop

class Archer(Troop):
  def __init__(self, scene, x, y):
    super().__init__(scene, x, y)
    self.color = (135, 89, 26)
    self.max_life = 120
    self.life = 120
    self.attack = 20
    self.defence = 20
    self.watch_range = (2, 0)
  def tiny_move():
    pass
