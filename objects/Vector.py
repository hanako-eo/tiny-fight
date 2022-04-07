import math

class Vector:
  x: int | float = 0
  y: int | float = 0

  def __init__(self, x: int | float, y: int | float):
    self.x, self.y = x, y

  def __str__(self):
    return '{:g}x + {:g}y'.format(self.x, self.y)

  def __repr__(self):
    return repr((self.x, self.y))

  def dot(self, other):
    if not isinstance(other, Vector):
        raise TypeError('Can only take dot product of two Vector objects')
    return self.x * other.x + self.y * other.y

  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y)

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __mul__(self, scalar):
    if isinstance(scalar, Vector):
      return Vector(self.x * scalar.x, self.y * scalar.y)
    return Vector(self.x * scalar, self.y * scalar)

  def __rmul__(self, scalar):
    return self.__mul__(scalar)

  def __neg__(self):
    return Vector(-self.x, -self.y)

  def __truediv__(self, scalar):
    return Vector(self.x / scalar, self.y / scalar)

  def __mod__(self, scalar):
    return Vector(self.x % scalar, self.y % scalar)

  def __abs__(self):
    return math.sqrt(self.x**2 + self.y**2)

  def distance_to(self, other):
    return abs(self - other)

  def to_polar(self):
    return self.__abs__(), math.atan2(self.y, self.x)
