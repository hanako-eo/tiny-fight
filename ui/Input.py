import draw
import pygame
from objects.Entity import Entity

class Input(Entity):
  def __init__(self, scene, x, y, width, height, content):
    super().__init__(scene, "Button", x, y, width, height)
    self.color = (255, 0, 0)
    self._continue = False
    self.content = content
    self.previous_key = 0
    self.hover = False
    self.focus = False
    self.time = 0
    self.cursor_pos = 0

  def update(self, delta):
    self.hover = self.collision(self.game.mouse)
    if self.hover and self.game.mouse.click:
      self.focus = True
    elif self.game.mouse.click:
      self.focus = False
      
    if not self.focus:
      self.previous_key = 0
      return 

    key = None
    n_keys = len(self.game.keys)
    if n_keys > 0:
      key = self.game.keys[n_keys - 1]

    if key != None and self.previous_key != key.key:
      self.previous_key = key.key
      self.time = 0

    if self.time == 0 and key != None:
      suffix = self.content[:self.cursor_pos]
      prefix = self.content[self.cursor_pos:]
      if key.key == pygame.K_BACKSPACE:
        self.content = suffix[:-1] + prefix
        self.cursor_pos -= 1
      elif key.key == pygame.K_DELETE:
        self.content = suffix + prefix[1:]
      elif key.key == pygame.K_LEFT:
        self.cursor_pos -= 1
      elif key.key == pygame.K_RIGHT:
        self.cursor_pos += 1
      else:
        self.content = suffix + key.unicode + prefix
        self.cursor_pos += 1

      self.cursor_pos = max(0, min(len(self.content), self.cursor_pos))

    self.time += 1
    if self.time >= (4 if self._continue else 26) or n_keys == 0:
      self._continue = True
      self.time = 0
      if n_keys == 0:
        self._continue = False
        self.previous_key = 0

  
  def draw(self):
    (width, height) = draw.measure_text(self.content)
    if self.hover:
      draw.fill((205, 0, 0))
    else:
      draw.fill(self.color)
    draw.rect(self.game.context, self.x, self.y, self.width, self.height)
    draw.fill((255, 255, 255))
    draw.text(
      self.game.context, 
      self.x + 4,# + self.width / 2 - width / 2, 
      self.y + self.height / 2 - height / 2, 
      self.content
    )
    draw.reset()
