from constant import PREV
from objects.State import State

class DeadState(State):
  def __init__(self, troop):
    super().__init__("dead", troop)

  def enter(self):
    self.value.timer.set_callback(self.update)

  def update(self, _):
    self.value.destroy()

  def allow_transition(self, order, state):
    return order == PREV and state.name == "attack" or order == PREV and state.name == "move"