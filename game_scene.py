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

        self.blinky = Ghost(director.screen, self.maze.blinky,
                            self.maze.block_size, 1)
        self.inkey = Ghost(director.screen, self.maze.inkey,
                           self.maze.block_size, 2)
        self.pinky = Ghost(director.screen, self.maze.pinky,
                           self.maze.block_size, 3)
        self.clyde = Ghost(director.screen, self.maze.clyde,
                           self.maze.block_size, 4)

        self.pacman = Pacman(director.screen, self.maze.pacman,
                             self.maze.block_size)

        self.food = self.maze.food
        self.powers = self.maze.powers

        self.reset()

        old_ticks = pygame.time.get_ticks()

        self.blinky_time = old_ticks
        self.inkey_time = old_ticks
        self.pinky_time = old_ticks
        self.clyde_time = old_ticks

        self.blinky_timer = 5000
        self.inkey_timer = 10000
        self.pinky_timer = 15000
        self.clyde_timer = 20000

    def exit(self):
        self.game_stats.save_scores()

    def reset(self):
        self.game_stats.reset()
        self.maze.load_file("assets/maze.txt")

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
        if self.food or self.powers:
            self.pacman.update()

            for food in self.food:
                if food.rect.colliderect(self.pacman.rect):
                    self.food.remove(food)
                    self.game_stats.score += 10

            for power in self.powers:
                if power.rect.colliderect(self.pacman.rect):
                    self.powers.remove(power)
                    self.game_stats.score += 50
                    self.blinky.set_state('vulnerable')
                    self.inkey.set_state('vulnerable')
                    self.pinky.set_state('vulnerable')
                    self.clyde.set_state('vulnerable')

            pacman = self.pacman.cooToItem()
            blinky = self.maze.grid[pacman[0]][pacman[1]]

            ticks = pygame.time.get_ticks()
            if self.blinky_timer <= ticks - self.blinky_time:
                self.blinky.update(self.maze.grid, blinky)
            if self.inkey_timer <= ticks - self.inkey_time:
                self.inkey.update(self.maze.grid,
                                  self.maze.grid[pacman[0]][pacman[1]])
            if self.pinky_timer <= ticks - self.pinky_time:
                self.pinky.update(self.maze.grid,
                                  self.maze.grid[pacman[0]][pacman[1]])
            if self.clyde_timer <= ticks - self.clyde_time:
                self.clyde.update(self.maze.grid,
                                  self.maze.grid[pacman[0]][pacman[1]])
            self.game_stats.update()

    def render(self):
        self.director.screen.fill(self.background)

        self.game_stats.render()
        self.maze.render()

        for food in self.food:
            food.render()

        for power in self.powers:
            power.render()

        self.blinky.render()
        self.inkey.render()
        self.pinky.render()
        self.clyde.render()

        self.pacman.render()
