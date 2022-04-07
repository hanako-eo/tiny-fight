import pygame
from objects.Scene import Scene

EMPTY = 0

class PlateScene(Scene):
  plate: list[list[int]] = []

  def init(self):
    super().init()
    self.plate = [
      [EMPTY for _ in range(8)] for _ in range(5)
    ]

  def draw(self):
    pygame.draw.rect(
      self.game.context,
      (255, 0, 0),
      pygame.Rect(10, 10, 20, 20)
    )