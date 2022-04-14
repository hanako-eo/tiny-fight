class Timer:
  def __init__(self, callback, time):
    self.callback = callback
    self.time = time
    self.reset()

  def set_waiting(self, value):
    self.time = value

  def set_callback(self, callback):
    self.callback = callback
    self.reset()

  def reset(self):
    self.delta = 0

  def can(self, delta):
    return self.time <= self.delta + delta

  def update(self, delta: float):
    self.delta += delta
    if self.time <= self.delta:
      self.callback(self.delta)
      self.delta = 0

class Tick:
  def __init__(self, callback, tick):
    self.callback = callback
    self.tick = tick
    self.reset()

  def set_waiting(self, value):
    self.tick = value

  def set_callback(self, callback):
    self.callback = callback
    self.reset()

  def reset(self):
    self.delta = 0
    self.wait = 0

  def can(self, _):
    return self.tick <= self.wait + 1

  def update(self, delta):
    self.delta += delta
    self.wait += 1
    if self.tick <= self.wait:
      self.callback(self.delta)
      self.delta = self.wait = 0
