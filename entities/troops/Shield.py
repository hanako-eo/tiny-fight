from entities.troops.Troop import Troop

class Shield(Troop):
  def __init__(self, scene, card, x, y):
    super().__init__(scene, card, x, y)
    self.color = (255, 175, 204)
    self.max_life = 200
    self.life = 200
    self.attack = 12
    self.defence = 40
    
  def tiny_move():
    pass