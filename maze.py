import pygame

from food import Food
from power import Power


class Maze:
    def __init__(self, file, screen):
        self.screen = screen

        self.block_size = 30
        self.load_file(file)

    def load_file(self, file):
        rows = open(file, 'r').read().split('\n')

        self.food = []
        self.powers = []

        self.grid = []
        for i, row in enumerate(rows):
            col_content = []
            for j, col in enumerate(row):
                item = {'i': int(i), 'j': int(j), 'f': 0, 'g': 0, 'h': 0,
                        'type': col, 'neighbors': [], 'previous': None}
                if col is 'c':
                    self.pacman = item
                elif col is '1':
                    self.blinky = item
                elif col is '2':
                    self.inkey = item
                elif col is '3':
                    self.pinky = item
                elif col is '4':
                    self.clyde = item
                elif col is 'n':
                    self.food.append(Food(self.screen, item, self.block_size))
                elif col is 'p':
                    self.powers.append(Power(self.screen, item,
                                       self.block_size))
                col_content.append(item)
            self.grid.append(col_content)

        self.addNeighbors()

    def addNeighbors(self):
        rows = len(self.grid)
        cols = len(self.grid[0])
        non_walkable = ['x']
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j]['type'] not in non_walkable:
                    if i < rows - 1:
                        new_neighbor = self.grid[i + 1][j]
                        if new_neighbor['type'] not in non_walkable:
                            self.grid[i][j]['neighbors'].append(new_neighbor)
                    if i > 0:
                        new_neighbor = self.grid[i - 1][j]
                        if new_neighbor['type'] not in non_walkable:
                            self.grid[i][j]['neighbors'].append(new_neighbor)
                    if j < cols - 1:
                        new_neighbor = self.grid[i][j + 1]
                        if new_neighbor['type'] not in non_walkable:
                            self.grid[i][j]['neighbors'].append(new_neighbor)
                    if j > 0:
                        new_neighbor = self.grid[i][j - 1]
                        if new_neighbor['type'] not in non_walkable:
                            self.grid[i][j]['neighbors'].append(new_neighbor)

    def render(self):
        x, y, b = 0, 0, self.block_size

        for row in self.grid:
            for block in row:
                if block['type'] is 'x':
                    # This is a brick
                    self.screen.fill((0, 0, 100), pygame.Rect(x, y, b, b))
                elif block['type'] is 'f':
                    # fence
                    self.screen.fill((100, 100, 100), pygame.Rect(x, y, b, b))

                x += b
            x = 0
            y += b
