from constant import EMPTY
from objects.State import State

class PlayState(State):
  def __init__(self, game):
    super().__init__("play", game)

  def enter(self):
    self.value.remove_overlay("OverlayScene")
    for _, entity in self.value.current_scene.plate:
      if entity != EMPTY:
        entity.state.use("move", entity)

  def update(self, _):
    play_state = self.value.current_scene
    if play_state.n_units == 0:
      play_state.state.use("cooldown", self.value)
