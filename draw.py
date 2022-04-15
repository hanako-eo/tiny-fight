from email.policy import default
import pygame

loaded = {}
default_style = {
  "reset": True,
  "font": {"size": 24, "family": "Arial"}
}
_style = default_style
_fill_color = (0, 0, 0, 0)
_scale = 1

def scale(value):
  global _scale
  _scale = value

def fill(value):
  global _fill_color
  _fill_color = (
    value[0], 
    value[1], 
    value[2], 
    int(value[3] * 255) if len(value) > 3 and value[3] <= 1 else 255
  )

def style(value: dict[str, object]):
  if value.get("reset") == True:
    _style = value
  else:
    _style |= value

def text(context: pygame.Surface, x: int, y: int, content: str):
  font = pygame.font.SysFont(_style["font"]["family"], _style["font"]["size"])
  surf = font.render(content, True, _fill_color)
  surf.set_alpha(_fill_color[3])
  context.blit(surf, (x, y))

def rect(context: pygame.Surface, x: int, y: int, width: int, height: int):
  shape = pygame.Surface((width, height), pygame.SRCALPHA)
  pygame.draw.rect(shape, _fill_color, shape.get_rect())
  context.blit(shape, [x, y, width, height])

def image(context: pygame.Surface, src: str, x: int, y: int, width: int, height: int):
  global loadeds
  if src not in loaded:
    loaded[src] = pygame.image.load(src).convert_alpha()
  context.blit(loaded[src], [x, y, width, height])

def sprite(context: pygame.Surface, src: str, sx: int, sy: int, swidth: int, sheight: int, dx: int = -1, dy: int = -1, dwidth: int = -1, dheight: int = -1, color = (0, 0, 0)):
  global loadeds
  if src not in loaded:
    loaded[src] = pygame.image.load(src).convert_alpha()

  if dx < 0 or dy < 0 or dwidth < 0 or dheight < 0:
    dx = dy = 0
    dwidth, dheight = swidth, sheight
    
  image = pygame.Surface((dwidth, dheight)).convert_alpha()
  image.blit(loaded[src], (0, 0), (dx, dy, dwidth, dheight))
  image = pygame.transform.scale(image, (swidth * _scale, sheight * _scale))
  image.set_colorkey(color)

  context.blit(image, [sx, sy, swidth, sheight])

def reset():
  scale(1)
  fill((255, 255, 255))
  style(default_style)
