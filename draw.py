import pygame

def rect(context: pygame.Surface, color: tuple[int, int, int] | tuple[int, int, int, float], x: int, y: int, width: int, height: int):
  alpha_color = (
    color[0], 
    color[1], 
    color[2], 
    int(color[3] * 255) if len(color) > 3 and color[3] <= 1 else 255
  )

  shape = pygame.Surface((width, height), pygame.SRCALPHA)
  pygame.draw.rect(shape, alpha_color, shape.get_rect())
  context.blit(shape, [x, y, width, height])
