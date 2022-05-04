from entities.troops.Troop import Troop

class Archer(Troop):
  def __init__(self, scene, card, x, y):
    super().__init__(scene, card, x, y)
    self.color = (135, 89, 26)
    self.max_life = 120
    self.life = 120
    self.attack = 20
    self.defence = 20
    self.watch_range = 2
  def tiny_move():
    pass
