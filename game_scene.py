import pygame

from scene import Scene
from maze import Maze
from ghost import Ghost
from pacman import Pacman
from game_stats import GameStats


class GameScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

        self.game_stats = GameStats(director)

        self.maze = Maze("assets/maze.txt", director.screen)

        characters = self.maze.get_characters()

        self.blinky = Ghost(director.screen, characters['blinky'],
                            self.maze.block_size, 1)
        self.inkey = Ghost(director.screen, characters['inkey'],
                           self.maze.block_size, 2)
        self.pinky = Ghost(director.screen, characters['pinky'],
                           self.maze.block_size, 3)
        self.clyde = Ghost(director.screen, characters['clyde'],
                           self.maze.block_size, 4)

        self.pacman = Pacman(director.screen, characters['pacman'],
                             self.maze.block_size, self.maze.rows)

        self.food = characters['food']
        self.power = characters['power']

        self.reset()

        self.old_ticks = pygame.time.get_ticks()

    def reset(self):
        self.game_stats.reset()

    def keydown(self, key):
        if key == pygame.K_LEFT:
            if self.pacman.rect.y % self.maze.block_size == 0:
                self.pacman.direction = 1
            else:
                self.pacman.next_direction = 1
        elif key == pygame.K_UP:
            if self.pacman.rect.x % self.maze.block_size == 0:
                self.pacman.direction = 2
            else:
                self.pacman.next_direction = 2
        elif key == pygame.K_RIGHT:
            if self.pacman.rect.y % self.maze.block_size == 0:
                self.pacman.direction = 3
            else:
                self.pacman.next_direction = 3
        elif key == pygame.K_DOWN:
            if self.pacman.rect.x % self.maze.block_size == 0:
                self.pacman.direction = 4
            else:
                self.pacman.next_direction = 4
        elif key == pygame.K_a:
            self.pacman.portal_direction = 1
        elif key == pygame.K_w:
            self.pacman.portal_direction = 2
        elif key == pygame.K_d:
            self.pacman.portal_direction = 3
        elif key == pygame.K_s:
            self.pacman.portal_direction = 4

    def update(self):
        self.pacman.update()

        for food in self.food:
            if food.rect.colliderect(self.pacman.rect):
                self.food.remove(food)
                self.game_stats.score += 10

        for power in self.power:
            if power.rect.colliderect(self.pacman.rect):
                self.power.remove(power)
                self.game_stats.score += 50

        self.game_stats.update()

    def render(self):
        self.director.screen.fill(self.background)

        self.game_stats.render()
        self.maze.render()

        for food in self.food:
            food.render()

        for power in self.power:
            power.render()

        self.blinky.render()
        self.inkey.render()
        self.pinky.render()
        self.clyde.render()

        self.pacman.render()
