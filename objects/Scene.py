class Scene:
  def __init__(self, game, name: str):
    self.name = name
    self.game = game
    self.entities = []

  def draw(self):
    for entity in self.entities:
      entity.draw()
    
  def update(self, delta: float):
    for entity in self.entities:
      entity.update(delta)
