import pygame

class Mouse:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.width = 1
    self.height = 1

  def update(self):
    self.x, self.y = pygame.mouse.get_pos()
  