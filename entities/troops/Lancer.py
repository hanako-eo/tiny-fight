from entities.troops.Troop import Troop

class Lancer(Troop):
  def __init__(self, scene, x, y):
    super().__init__(scene, x, y)
    
    self.color = (252, 163, 17)
    self.max_life = 130
    self.life = 130
    self.attack = 17
    self.defence = 20
    self.set_speed(44) # c'etait la reponse :)
    
  def tiny_move():
    pass