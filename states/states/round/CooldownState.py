from objects.State import State

class CooldownState(State):
  def __init__(self, game):
    super().__init__("cooldown", game)
    self.time = 30

  def enter(self):
    self.value.add_overlay("OverlayScene")
    self.time = 181

  def update(self, delta):
    self.time -= delta

  def display(self):
    m = int(self.time // 60 % 60)
    s = int(self.time % 60)
    return f"{m}:{f'0{s}' if s < 10 else s}"
