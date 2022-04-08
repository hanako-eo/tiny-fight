from __future__ import annotations

class Entity:
  def __init__(self, scene, name: str, x: int, y: int, width: int, height: int):
    self.inited = False

    self.name = name
    self.game = scene.game
    self.scene = scene
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def collision(self, test: Entity):
    return self.x < test.x + test.width and self.x + self.width > test.x and self.y < test.y + test.height and self.y + self.height > test.y
    
  def init(self):
    pass

  def draw(self):
    pass

  def update(self):
    pass
