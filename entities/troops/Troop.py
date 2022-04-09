import pygame
from objects.Entity import Entity

class Troop(Entity):
  def __init__(self, scene, x: int, y: int, cell_x: int, cell_y: int, width: int, height: int):
    super().__init__(scene, "Troop", x, y, width, height)
    self.cell_pos = (cell_x, cell_y)

    self.scene.entities.append(self)
    self.active = active

  def init(self):
    self.default_color = (255, 0, 0, 0.5) if (self.cell_pos[0] + self.cell_pos[1]) % 2 == 0 else (255, 0, 255, 0.5)

  def update(self, _):
    self.color = self.default_color
    if self.active and self.collision(self.game.mouse):
      self.color = (0, 255, 0, 1)

  def draw(self):
    pygame.draw.rect(
      self.game.context,
      self.color,
      [
        self.x, 
        self.y, 
        self.width, 
        self.height
      ],
    )
  