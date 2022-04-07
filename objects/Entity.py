class Entity:
  def __init__(self, game, name:str, x:int, y:int, width:int, height:int):
    self.name = name
    self.game = game
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.SATEntity = None
    
  def draw(self):
    pass
  def update(self):
    pass