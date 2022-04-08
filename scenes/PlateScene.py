from entities.Cell import Cell
from objects.Scene import Scene

EMPTY = 0

class PlateScene(Scene):
  plate: list[list[int]] = []
  cell_size: tuple[int, int] = (60, 60)

  def init(self):
    self.deck = [
      Cell(
          self,
          x * self.cell_size[0] + 100,
          self.game.screen_height - 100 - self.cell_size[1],
          x, 0,
          self.cell_size[0],
          self.cell_size[1]
        ) for x in range(10)
    ]
    self.plate = [
      [
        EMPTY for y in range(5)
      ] for x in range(10)
    ]

  # def draw(self):
  #   pass
    # for x in range(len(self.plate)):
    #   for y in range(len(self.plate[x])):
        
