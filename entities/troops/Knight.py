from entities.troops.Troop import Troop

class Knight(Troop):
  def __init__(self, scene, x, y):
    super().__init__(scene, x, y)
    self.color = (0, 119, 182)
    self.max_life = 150
    self.life = 150
    self.attack = 25
    self.defence = 20
  
  def tiny_move():
    pass

