from objects.Scene import Scene
from ui.Button import Button

class MenuScene(Scene):
  def __init__(self, game):
    super().__init__(game, "MenuScene")
    self.play_button = Button(self, 50, 50, 160, 64, "Play")
    self.entities.append(self.play_button)

  def init(self):
    self.play_button.add_listener("click", lambda: self.game.change_scene("PlateScene"))
