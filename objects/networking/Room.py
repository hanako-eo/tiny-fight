class Room:
  def __init__(self, creator):
    self.id = id(self)
    self.creator = creator
    self.players = [creator]