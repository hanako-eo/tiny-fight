from objects.State import State

class CooldownState(State):
  def __init__(self):
    super().__init__("cooldown", 181)

  def enter(self):
    self.value = 181

  def update(self, delta):
    self.value -= delta

  def display(self):
    m = int(self.value // 60 % 60)
    s = int(self.value % 60)
    return f"{m}:{f'0{s}' if s < 10 else s}"
