from entities.Cell import Cell
from objects.Scene import Scene

EMPTY = 0

class PlateScene(Scene):
  plate: list[list[int]] = []
  cell_size: tuple[int, int] = (60, 60)

  def init(self):
    self.plate = [
      [
        Cell(
          self,
          x * self.cell_size[0] + 100,
          y * self.cell_size[1] + 150,
          x, y,
          self.cell_size[0],
          self.cell_size[1]
        ) for y in range(5)
      ] for x in range(10)
    ]

  # def draw(self):
  #   pass
    # for x in range(len(self.plate)):
    #   for y in range(len(self.plate[x])):
        
