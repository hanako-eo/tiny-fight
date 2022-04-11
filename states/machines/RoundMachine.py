from objects.State import State
from objects.Machine import Machine
from states.states.round.CooldownState import CooldownState
from states.states.round.PlayState import PlayState

class RoundMachine(Machine):
  def __init__(self):
    super().__init__({
      "cooldown": CooldownState,
      "play": PlayState,
      "extra": State
    }, "cooldown")