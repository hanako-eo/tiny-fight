from objects.Scene import Scene
from ui.Button import Button
from ui.Input import Input

class MenuScene(Scene):
  def __init__(self, game):
    super().__init__(game, "MenuScene")
    x = game.screen_width / 2 - 80
    y = game.screen_height / 2 - 32
    
    self.local_play_button = Button(self, x, y - 64, 160, 64, "Play in local")
    self.play_button = Button(self, x, y + 64, 160, 64, "Play")

    self.entities.append(self.play_button)
    self.entities.append(self.local_play_button)

  def init(self):
    self.play_button.add_listener("click", lambda: self.game.change_scene("PlateScene"))
    self.local_play_button.add_listener("click", lambda: self.game.change_scene("LocalRoomScene"))
