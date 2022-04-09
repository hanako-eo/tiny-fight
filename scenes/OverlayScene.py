from entities.Cell import Cell
from objects.Scene import Scene

class OverlayScene(Scene):
  plate: list[list[int]] = []
  cell_size: int = 60

  def init(self):
    self.deck = [
      Cell(
          self,
          x * self.cell_size + 100,
          self.game.screen_height - 100 - self.cell_size,
          x, 0,
          self.cell_size,
          self.cell_size
        ) for x in range(10)
    ]
    self.plate = [
      [
        Cell(
          self,
          x * self.cell_size + 100,
          y * self.cell_size + 100,
          x, y,
          self.cell_size,
          self.cell_size,
          x < 2 or x > 7
        ) for y in range(5)
      ] for x in range(10)
    ]

  # def draw(self):
  #   pass
    # for x in range(len(self.plate)):
    #   for y in range(len(self.plate[x])):
        
