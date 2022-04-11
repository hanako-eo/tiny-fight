from constant import NEXT, PREV
from objects.State import State

class AttackState(State):
  def __init__(self, troop, enemy):
    super().__init__("attack", (troop, enemy))

  def enter(self):
    self.value[0].timer.set_callback(self.update)

  def update(self, _):
    (troop, enemy) = self.value
    enemy.life -= troop.attack - troop.attack * (enemy.defence / 100)
    if troop.life <= 0:
      return 
    if enemy.life <= 0:
      troop.state.use("move", troop)

  def allow_transition(self, order, state):
    return (order == NEXT and state.name == "move") or (order == NEXT and state.name == "dead") or (order == PREV and state.name == "move")