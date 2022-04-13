import pygame

from constant import EMPTY
from entities.Cell import Cell
from entities.cards.TroopCard import TroopCard
from entities.troops.Troop import Troop
from objects.Plate import Plate
from objects.Scene import Scene
from states.machines.RoundMachine import RoundMachine

class PlateScene(Scene):
  plate: list[list[int]] = []

  def init(self):
    self.state = RoundMachine()

    self.deck = [
      TroopCard(self, 0, Troop)
    ]
    self.plate = Plate()

  def update(self, delta: float):
    self.state.current.update(delta)
    if self.state.match("cooldown") and self.state.current.value <= 0:
      self.state.use("play", self.game)

    for _, value in self.plate:
      if value != EMPTY:
        value.update(delta)

  def draw(self):
    if self.state.match("cooldown"):
      font = pygame.font.SysFont("Arial", 24)
      self.game.context.blit(font.render(self.state.current.display(), True, (255, 255, 255, 100)), (20, 20))

  def postoverlay_draw(self):
    for pos, value in self.plate:
      if value != EMPTY:
        value.draw(pos[0], pos[1])
        value.x = pos[0]
