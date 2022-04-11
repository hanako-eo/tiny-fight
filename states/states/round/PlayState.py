from objects.State import State

class PlayState(State):
  def __init__(self, game):
    super().__init__("play", game)

  def enter(self):
    self.value.remove_overlay("OverlayScene")
    for entity in self.value.current_scene.entities:
      if entity.name == "Troop":
        entity.state.use("move", entity)
