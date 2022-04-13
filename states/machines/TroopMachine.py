from objects.State import State
from objects.Machine import Machine
from states.states.troop.AttackState import AttackState
from states.states.troop.DeadState import DeadState
from states.states.troop.MoveState import MoveState
from states.states.troop.WaitState import WaitState

class TroopMachine(Machine):
  def __init__(self, troop):
    super().__init__({
      "move": MoveState,
      "attack": AttackState,
      "finish": State,
      "dead": DeadState,
      "wait": WaitState
    }, "wait", troop)
