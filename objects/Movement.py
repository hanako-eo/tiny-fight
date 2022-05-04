class Movement:
  def __init__(self, current_time = 0, begin = 0, change = 0, duration = 1):
    self.current_time = current_time
    self.begin = begin
    self.change = change
    self.duration = duration

  def set_begin(self, begin = 0):
    self.begin = begin
    self.current_time = 0

  def set_duration(self, duration = 0):
    self.duration = duration
    self.current_time = 0

  def update(self, delta):
    self.current_time += delta

  def get_pos(self):
    return self.change * self.current_time / self.duration + self.begin
