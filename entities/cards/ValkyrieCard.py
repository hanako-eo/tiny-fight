from entities.cards.TroopCard import TroopCard
from entities.troops.Valkyrie import Valkyrie

class ValkyrieCard(TroopCard):
  def __init__(self, scene, deck_index):
    super().__init__(scene, deck_index, Valkyrie)
    self.color = (65, 99, 253)