from ui.Button import Button
from ui.Input import Input
from objects.Scene import Scene

class LocalRoomScene(Scene):
  def __init__(self, game):
    super().__init__(game, "LocalRoomScene")
    self.back = Button(self, 16, 16, 64, 64, "<")
    self.button = Button(self, self.game.screen_width / 4 - 80, self.game.screen_height / 2 - 32, 160, 64, "Create Room")
    self.input = Input(self, self.game.screen_width * 3 / 4 - 80, self.game.screen_height / 2 - 32, 160, 64, "")
    
  def init(self):
    self.back.add_listener("click", lambda: self.game.change_scene("MenuScene"))

    self.entities.append(self.button)
    self.entities.append(self.input)
    self.entities.append(self.back)

  # def update(self, delta):
