from objects.State import State

class CooldownState(State):
  def __init__(self):
    super().__init__("cooldown", 180)

  def enter(self):
    self.value = 180

  def update(self, delta):
    self.value -= delta

  def display(self):
    s = int(self.value % 60 // 1)
    return f"{int(self.value // 60)}:{f'0{s}' if s < 10 else s}"
