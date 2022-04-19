import draw
from objects.Entity import Entity

class Button(Entity):
  def __init__(self, scene, x, y, width, height, content):
    super().__init__(scene, "Button", x, y, width, height)
    self.color = (255, 0, 0)
    self.content = content
    self.hover = False

  def update(self, delta):
    self.hover = self.collision(self.game.mouse)
    if self.hover and self.game.mouse.click:
      self.emit("click")
  
  def draw(self):
    (width, height) = draw.measure_text(self.content)
    if self.hover:
      draw.fill((205, 0, 0))
    else:
      draw.fill(self.color)
    draw.rect(self.game.context, self.x, self.y, self.width, self.height)
    draw.fill((255, 255, 255))
    draw.text(
      self.game.context, 
      self.x + self.width / 2 - width / 2, 
      self.y + self.height / 2 - height / 2, 
      self.content
    )
    draw.reset()
