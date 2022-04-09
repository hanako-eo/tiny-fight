from entities.Cell import Cell
from entities.cards.TroopCard import TroopCard
from objects.Scene import Scene

EMPTY = 0

class PlateScene(Scene):
  plate: list[list[int]] = []
  cell_size: int = 60

  def init(self):
    self.deck = [
      TroopCard(self, 0, self.cell_size)
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
        
