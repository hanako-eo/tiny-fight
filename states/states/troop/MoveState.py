from constant import NEXT, PREV
from objects.State import State

class MoveState(State):
  def __init__(self, troop):
    super().__init__("move", troop)
    self.from_wait = True

  def enter(self):
    self.value.timer.set_callback(self.update)
    if not self.from_wait:
      self.update(0)

  def update(self, _):
    if not self.value.moved and self.value.life > 0:
      self.value.move(self.value.x, self.value.y)
    self.value.moved = False

  def allow_transition(self, order, state):
    self.from_wait = state.name == "wait"
    return (order == NEXT and state.name == "attack") or (order == NEXT and state.name == "finish") or (order == PREV and state.name == "wait") or (order == PREV and state.name == "attack")