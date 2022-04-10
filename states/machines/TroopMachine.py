from objects.State import State
from objects.Machine import Machine
from states.states.troop.MoveState import MoveState
from states.states.troop.WaitState import WaitState

class TroopMachine(Machine):
  def __init__(self, troop):
    super().__init__({
      "move": MoveState(troop),
      "attack": State("attack"),
      "finish": State("finish"),
      "dead": State("dead"),
      "wait": WaitState(troop)
    }, "wait")
