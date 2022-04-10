import pygame

from constant import EMPTY
from entities.Cell import Cell
from entities.cards.TroopCard import TroopCard
from entities.troops.Troop import Troop
from objects.Scene import Scene
from states.machines.RoundMachine import RoundMachine

class PlateScene(Scene):
  plate: list[list[int]] = []

  def init(self):
    self.state = RoundMachine(self.game)

    self.deck = [
      TroopCard(self, 0, Troop)
    ]
    self.plate = [
      [
        EMPTY for y in range(5)
      ] for x in range(10)
    ]

  def update(self, delta: float):
    self.state.current.update(delta)
    if self.state.current.name == "cooldown" and self.state.current.value <= 0:
      self.state.use("play")

  def draw(self):
    if self.state.current.name == "cooldown":
      font = pygame.font.SysFont("Arial", 24)
      self.game.context.blit(font.render(self.state.current.display(), True, (255, 255, 255, 100)), (20, 20))
