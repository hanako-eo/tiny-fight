from entities.cards.TroopCard import TroopCard
from entities.troops.Knight import Knight

class KnightCard(TroopCard):
  def __init__(self, scene, deck_index):
    super().__init__(scene, deck_index, Knight)
      