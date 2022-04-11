from __future__ import annotations
from typing import Callable, Optional, TYPE_CHECKING
from constant import NEXT, PREV
if TYPE_CHECKING:
  from State import State

class Machine:
  current: State

  def __init__(self, states: dict[str, Callable[[], State]], default: Optional[str] = None, *args):
    self.states = states
    if default == None or default not in states:
      self.current = states[list(states.keys())[0]](*args)
    else:
      self.current = states[default](*args)

  def match(self, *state_name: list[str]) -> bool:
    for state in state_name:
      if self.current.name == state:
        return True
    return False

  def use(self, state_name: str, *args) -> bool:
    if not self.can(state_name):
      return False

    state = self.states[state_name](*args)

    if self.current.allow_transition(NEXT, state) and state.allow_transition(PREV, self.current):
      self.current.exit()
      state.enter()
      self.current = state

      return True

    return False

  def can(self, state: str):
    return state in self.states
