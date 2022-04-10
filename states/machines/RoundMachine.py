from objects.State import State
from objects.Machine import Machine
from states.states.CooldownState import CooldownState

class RoundMachine(Machine):
  def __init__(self):
    super().__init__({
      "cooldown": CooldownState(),
      "play": State("play"),
      "extra": State("extra")
    }, "cooldown")

  # start = cooldown.to(play)
  # end = play.to(extra)
  # wait = extra.to(cooldown)