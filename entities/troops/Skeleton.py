from entities.troops.Troop import Troop

class Skeleton(Troop):
  def __init__(self, scene, x, y):
    super().__init__(scene, x, y)
    self.color = (255, 255, 255)
    self.max_life = 80
    self.life = 80
    self.attack = 18
    self.defence = 10
  def tiny_move():
    pass