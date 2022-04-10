import pygame

def rect(context: pygame.Surface, color: tuple[int, int, int], x: int, y: int, width: int, height: int):
  shape = pygame.Surface((width, height), pygame.SRCALPHA)
  pygame.draw.rect(shape, color, shape.get_rect())
  context.blit(shape, [x, y, width, height])
