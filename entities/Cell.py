import pygame
import draw
from constant import EMPTY
from objects.Entity import Entity

class Cell(Entity):
  active: bool = False
  cell_pos: tuple[int, int]
  color: tuple[int, int, int]

  def __init__(self, scene, plate_scene, x: int, y: int, cell_pos: tuple[int, int], size: int, active: bool = False):
    super().__init__(scene, f"cell{cell_pos}", x, y, size, size)
    self.plate_scene = plate_scene
    self.cell_pos = cell_pos

    scene.entities.append(self)
    self.active = active

  def init(self):
    self.default_color = (255, 0, 0, 0.3) if (self.cell_pos[0] + self.cell_pos[1]) % 2 == 0 else (255, 0, 255, 0.3)

  def update(self, _):
    self.color = self.default_color
    if self.active and self.collision(self.game.mouse):
      self.color = (0, 255, 0)
      if self.game.mouse.left and self.game.mouse.selection != None:
        (troop, card) = self.game.mouse.selection
        cell = self.plate_scene.plate.get(self.cell_pos)

        if cell != EMPTY:
          self.plate_scene.n_units -= 1
          cell.card.quantity += 1

        self.plate_scene.plate.set(self.cell_pos, troop(
          self.plate_scene,
          card,
          self.cell_pos[0],
          self.cell_pos[1]
        ))
        self.game.mouse.selection = None
        self.plate_scene.n_units += 1
        card.quantity -= 1

  def draw(self):
    draw.fill(self.color)
    draw.rect(
      self.game.context,
      self.x, 
      self.y, 
      self.width, 
      self.height
    )
    draw.reset()
  