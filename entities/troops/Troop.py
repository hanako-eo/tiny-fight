import pygame
from objects.Entity import Entity

class Troop(Entity):
  def __init__(self, scene, x: int, y: int, cell_pos: tuple[int, int]):
    super().__init__(scene, "Troop", x, y, 60, 60)
    self.cell_pos = cell_pos

    self.scene.entities.append(self)
    self.color = (0, 200, 0)

  # def init(self):
    # self.default_color = (0, 200, 0)

  # def update(self, _):
    # if self.active and self.collision(self.game.mouse):
    #   self.color = (0, 255, 0, 1)

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
  