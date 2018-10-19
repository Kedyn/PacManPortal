from director import Director
from menu_scene import MenuScene
from game_scene import GameScene


class Game:
    def __init__(self):
        self.director = Director((1200, 1000), "Space Invaders")

        self.menu_scene = MenuScene(self.director)
        self.game_scene = GameScene(self.director)
        self.scores_scene = None

        self.director.scene_list = {
            "menu": self.menu_scene,
            "game": self.game_scene,
            "scores": self.scores_scene
        }

        self.director.set_scene("menu")

    def play(self):
        self.director.loop()