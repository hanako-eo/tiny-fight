from constant import CELL_SIZE
from functions import pos
from entities.Cell import Cell
from objects.Scene import Scene

class OverlayScene(Scene):
  plate: list[list[int]] = []

  def init(self):
    self.deck = [
      Cell(
          self,
          self.game.current_scene,
          x * CELL_SIZE + 100,
          self.game.screen_height - 100 - CELL_SIZE,
          (x, 0),
          CELL_SIZE
        ) for x in range(10)
    ]
    self.plate = [
      [
        Cell(
          self,
          self.game.current_scene,
          pos(x), pos(y),
          (x, y),
          CELL_SIZE,
          x < 2 or x > 7
        ) for y in range(5)
      ] for x in range(10)
    ]        
