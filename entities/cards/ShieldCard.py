from entities.cards.TroopCard import TroopCard
from entities.troops.Shield import Shield

class ShieldCard(TroopCard):
  def __init__(self, scene, deck_index):
    super().__init__(scene, deck_index, Shield)
    self.color = (255, 175, 204)