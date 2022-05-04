from constant import CELL_SIZE

def pos(x: int):
  return x * CELL_SIZE + 100

def w_range_y(x: int):
  if x == 0:
    return 0
  return (-1)**x
