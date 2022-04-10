class Timer:
  def __init__(self, callback, time):
    self.callback = callback
    self.time = time
    self.delta = 0

  def update(self, delta: float):
    self.delta += delta
    if self.time <= self.delta:
      self.delta = 0
      self.callback()

class Tick:
  def __init__(self, callback, tick):
    self.callback = callback
    self.tick = tick
    self.delta = 0

  def update(self):
    self.delta += 1
    if self.tick <= self.delta:
      self.delta = 0
      self.callback()
