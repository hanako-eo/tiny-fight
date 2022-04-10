from typing import Any

class State:
  def __init__(self, name: str, value: Any = None):
    self.name = name
    self.value = value

  def enter():
    pass

  def update(delta: float):
    pass

  def exit():
    pass

  def allow_transition(name: str, state: 'State') -> bool:
    return True