import draw

from constant import EMPTY
from entities.cards.ValkyrieCard import ValkyrieCard
from entities.cards.KnightCard import KnightCard
from entities.cards.ShieldCard import ShieldCard
from entities.cards.LancerCard import LancerCard
from entities.cards.ArcherCard import ArcherCard
from entities.cards.TroopCard import TroopCard
from entities.troops.Troop import Troop
from objects.Plate import Plate
from objects.Scene import Scene
from states.machines.RoundMachine import RoundMachine

class PlateScene(Scene):
  plate: list[list[int]] = []

  def __init__(self, game):
    super().__init__(game, "PlateScene")

  def init(self):
    self.game.add_overlay("OverlayScene")
    self.state = RoundMachine()

    self.deck = [
      TroopCard(self, 0, Troop),
      KnightCard(self, 1),
      ShieldCard(self, 2),
      LancerCard(self, 3),
      ArcherCard(self, 4),
      ValkyrieCard(self, 5)
    ]
    self.plate = Plate()

  def update(self, delta: float):
    self.state.current.update(delta)
    if self.state.match("cooldown") and self.state.current.value <= 1:
      self.state.use("play", self.game)

    for _, value in self.plate:
      if type(value) != int:
        value.update(delta)

  def draw(self):
    if self.state.match("cooldown"):
      draw.text(self.game.context, 20, 20, self.state.current.display())
      
  def postoverlay_draw(self):
    for pos, value in self.plate:
      if type(value) != int:
        value.draw(pos[0], pos[1])
        value.x = pos[0]
