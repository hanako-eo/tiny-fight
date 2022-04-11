from objects.State import State
from objects.Machine import Machine
from states.states.round.CooldownState import CooldownState
from states.states.round.PlayState import PlayState

class RoundMachine(Machine):
  def __init__(self, game):
    super().__init__({
      "cooldown": CooldownState(),
      "play": PlayState(game),
      "extra": State("extra")
    }, "cooldown")