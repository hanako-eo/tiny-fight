from __future__ import annotations
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
  from State import State

class Machine:
  current: State

  def __init__(self, states: dict[str, State], default: Optional[str] = None):
    self.states = states
    if default == None or default not in states:
      self.current = states[list(states.keys())[0]]
    else:
      self.current = states[default]

  def use(self, state_name: str) -> bool:
    if not self.can(state_name):
      return False

    state = self.states[state_name]

    if self.current.allow_transition(state) and state.allow_transition(self.current):
      self.current.exit()
      state.enter()
      self.current = state

      return True

    return False

  def can(self, state: string):
    return state in self.states
