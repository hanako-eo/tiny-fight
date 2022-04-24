from entities.cards.TroopCard import TroopCard
from entities.troops.Archer import Archer

class ArcherCard(TroopCard):
  def __init__(self, scene, deck_index):
    super().__init__(scene, deck_index, Archer)
    self.color = (135, 89, 26)