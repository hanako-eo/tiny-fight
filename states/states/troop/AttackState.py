from constant import NEXT, PREV
from objects.State import State

class AttackState(State):
  def __init__(self, troop):
    super().__init__("attack", troop)

  def enter(self):
    self.value.timer.set_callback(self.update)
    self.update(0)

  def update(self, _):
    self.value.fight()
      

  def allow_transition(self, order, state):
    return (order == NEXT and state.name == "move") or (order == NEXT and state.name == "dead") or (order == PREV and state.name == "move")