import pygame

from scene import Scene
from maze import Maze
from ghost import Ghost
from game_stats import GameStats


class GameScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

        self.game_stats = GameStats(director)

        self.maze = Maze("assets/maze.txt", director.screen)

        characters = self.maze.get_characters()

        self.blinky = Ghost(director.screen, characters['blinky'], self.maze.block_size, 1)
        self.inkey = Ghost(director.screen, characters['inkey'], self.maze.block_size, 2)
        self.pinky = Ghost(director.screen, characters['pinky'], self.maze.block_size, 3)
        self.clyde = Ghost(director.screen, characters['clyde'], self.maze.block_size, 4)

        self.reset()

        self.old_ticks = pygame.time.get_ticks()

    def reset(self):
        self.game_stats.reset()

    def keydown(self, key):
        pass

    def update(self):
        self.game_stats.update()

    def render(self):
        self.director.screen.fill(self.background)

        self.game_stats.render()
        self.maze.render()

        self.blinky.render()
        self.inkey.render()
        self.pinky.render()
        self.clyde.render()
