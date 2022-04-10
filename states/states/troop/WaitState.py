from constant import NEXT
from objects.State import State

class WaitState(State):
  def __init__(self, troop):
    super().__init__("wait", troop)

  def enter(self):
    self.value.timer.callback = self.update

  def allow_transition(self, order, state):
    return order == NEXT and state.name == "move"