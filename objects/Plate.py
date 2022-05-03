from constant import EMPTY

class Plate:
  def __init__(self):
    self.plate = [
      [
        EMPTY for _ in range(5)
      ] for _ in range(10)
    ]

  def advance(self, pos: tuple[int, int], i = 1):
    if self.get(pos) == EMPTY:
      return

    next_pos = pos
    while self.get((next_pos[0] + i, next_pos[1])) != EMPTY:
      next_pos = (next_pos[0] + i, next_pos[1])

    next_pos = (next_pos[0] + i, next_pos[1])
    curr_pos = (next_pos[0] - i, next_pos[1])
    while next_pos != pos:
      self.move(curr_pos, next_pos)
      next_pos = curr_pos
      curr_pos = (next_pos[0] - i, next_pos[1])

  def move(self, pos1: tuple[int, int], pos2: tuple[int, int]):
    self.plate[pos1[0]][pos1[1]], self.plate[pos2[0]][pos2[1]] = self.plate[pos2[0]][pos2[1]], self.plate[pos1[0]][pos1[1]]

  def set(self, pos: tuple[int, int], value):
    self.plate[pos[0]][pos[1]] = value

  def remove(self, value):
    for x in range(len(self.plate)):
      for y in range(len(self.plate[x])):
        if self.plate[x][y] == value:
          self.plate[x][y] = EMPTY

  def remove_pos(self, pos: tuple[int, int]):
    self.plate[pos[0]][pos[1]] = EMPTY

  def get(self, pos: tuple[int, int]):
    return self.plate[pos[0]][pos[1]]

  def is_empty(self, pos: tuple[int, int]):
    return self.get(pos) == EMPTY

  def __iter__(self):
    for x in range(len(self.plate)):
      for y in range(len(self.plate[x])):
        yield ((x, y), self.plate[x][y])
