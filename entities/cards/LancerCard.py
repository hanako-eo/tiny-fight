from entities.cards.TroopCard import TroopCard
from entities.troops.Lancer import Lancer

class LancerCard(TroopCard):
  def __init__(self, scene, deck_index):
    super().__init__(scene, deck_index, Lancer)
    self.color = (252, 163, 17)