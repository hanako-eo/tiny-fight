from typing import Any
import pygame

class Mouse:
  left: bool = False
  middle: bool = False
  right: bool = False
  click: bool = False

  selection: Any = None

  def __init__(self):
    self.x = 0
    self.y = 0
    self.width = 1
    self.height = 1

  def update(self):
    self.x, self.y = pygame.mouse.get_pos()
    self.left, self.middle, self.right = pygame.mouse.get_pressed()
    self.click = self.left or self.middle or self.right
  