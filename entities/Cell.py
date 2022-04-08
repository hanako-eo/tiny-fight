import pygame
from objects.Entity import Entity

class Cell(Entity):
  cell_pos: tuple[int, int]
  color: tuple[int, int, int]
  def __init__(self, scene, x: int, y: int, cell_x: int, cell_y: int, width: int, height: int):
    super().__init__(scene, f"cell({cell_x}, {cell_y})", x, y, width, height)
    self.cell_pos = (cell_x, cell_y)

    self.scene.entities.append(self)
    self.default_color = (255, 0, 0)

  def init(self):
    self.default_color = (255, 0, 0) if (self.cell_pos[0] + self.cell_pos[1]) % 2 == 0 else (255, 0, 255)

  def update(self, _):
    self.color = self.default_color
    if self.collision(self.game.mouse):
      self.color = (0, 255, 0)

  def draw(self):
    pygame.draw.rect(
      self.game.context,
      self.color,
      pygame.Rect(
        self.x, 
        self.y, 
        self.width, 
        self.height
      )
    )
  