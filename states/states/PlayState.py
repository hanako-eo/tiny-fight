from objects.State import State

class PlayState(State):
  def __init__(self, game):
    super().__init__("play", game)

  def enter(self):
    print(self.value)
    self.value.remove_overlay("OverlayScene")
