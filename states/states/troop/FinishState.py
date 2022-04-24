from constant import PREV
from objects.State import State

class FinishState(State):
  def __init__(self, troop):
    super().__init__("finish", troop)

  def enter(self):
    self.value.timer.set_callback(self.update)
    self.value.destroy()

  def update(self, _):
    self.value.destroy()

  def allow_transition(self, order, state):
    return order == PREV and state.name == "move"