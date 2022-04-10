from constant import NEXT, PREV
from objects.State import State

class MoveState(State):
  def __init__(self, troop):
    super().__init__("move", troop)

  def enter(self):
    self.value.timer.callback = self.update

  def update(self, delta):
    self.value.move()

  def allow_transition(self, order, state):
    return (order == NEXT and state.name == "attack") or (order == NEXT and state.name == "finish") or (order == PREV and state.name == "wait")