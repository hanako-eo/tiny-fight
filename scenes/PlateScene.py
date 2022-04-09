from pprint import pprint

from constant import EMPTY
from entities.Cell import Cell
from entities.cards.TroopCard import TroopCard
from entities.troops.Troop import Troop
from objects.Scene import Scene

class PlateScene(Scene):
  plate: list[list[int]] = []

  def init(self):
    self.deck = [
      TroopCard(self, 0, Troop)
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
        
