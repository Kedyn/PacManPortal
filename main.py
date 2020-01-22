from framework.Game import Game
from framework.SceneManager import SceneManager
from game.characters.loader import load_characters
from game.scenes.game import GameScene
from game.scenes.high_scores import HighScoresScene
from game.scenes.menu import MenuScene
from game.constants import WIDTH, HEIGHT

game = Game.get_instance()
scene_manager = SceneManager.get_instance()

game.create((WIDTH, HEIGHT), "Pacman Portal", debug_mode=True)

load_characters()

scene_manager.add_scene("menu", MenuScene(game.get_surface()))
scene_manager.add_scene("game", GameScene(game.get_surface()))
scene_manager.add_scene("high_scores", HighScoresScene(game.get_surface()))

scene_manager.set_scene("menu")

game.start()
