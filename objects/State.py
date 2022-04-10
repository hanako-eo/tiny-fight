from typing import Any

class State:
  def __init__(self, name: str, value: Any = None):
    self.name = name
    self.value = value

  def enter(self):
    pass

  def update(self, delta: float):
    pass

  def exit(self):
    pass

  def allow_transition(self, order: int, state: 'State') -> bool:
    return True