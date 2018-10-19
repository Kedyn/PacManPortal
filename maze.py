import pygame

from food import Food
from power import Power


class Maze:
    def __init__(self, file, screen):
        self.screen = screen

        rows = []
        with open(file, 'r') as f:
            rows = f.readlines()

        self.rows = []
        for i, row in enumerate(rows):
            col_content = []
            for j, col in enumerate(row):
                item = {'i': i, 'j': j, 'f': 0, 'g': 0, 'h': 0, 'type': col,
                        'neighbors': [], 'previous': None}
                col_content.append(item)
            self.rows.append(col_content)

        self.addNeighbors()

        self.block_size = 30

    def addNeighbors(self):
        rows = len(self.rows)
        cols = len(self.rows[0])
        for i in range(rows):
            for j in range(cols):
                neighbors = self.rows[i][j]['neighbors']

                if i < cols - 1:
                    new_neighbor = self.rows[i + 1][j]
                    if new_neighbor['type'] is not 'x' or \
                            new_neighbor['type'] is not '.':
                        neighbors.append(new_neighbor)
                if i > 0:
                    new_neighbor = self.rows[i - 1][j]
                    if new_neighbor['type'] is not 'x' or \
                            new_neighbor['type'] is not '.':
                        neighbors.append(new_neighbor)
                if j < rows - 1:
                    new_neighbor = self.rows[i][j + 1]
                    if new_neighbor['type'] is not 'x' or \
                            new_neighbor['type'] is not '.':
                        neighbors.append(new_neighbor)
                if j > 0:
                    new_neighbor = self.rows[i][j - 1]
                    if new_neighbor['type'] is not 'x' or \
                            new_neighbor['type'] is not '.':
                        neighbors.append(new_neighbor)

    def get_characters(self):
        r, c, chars = 0, 0, {}

        chars.update({'fence': [], 'food': [], 'power': []})

        for row in self.rows:
            for block in row:
                if block['type'] is 'f':
                    fence = chars['fence']
                    fence.append(r * c)
                elif block['type'] is 'c':
                    chars['pacman'] = r + c
                elif block['type'] is '1':
                    chars['blinky'] = r + c
                elif block['type'] is '2':
                    chars['inkey'] = r + c
                elif block['type'] is '3':
                    chars['pinky'] = r + c
                elif block['type'] is '4':
                    chars['clyde'] = r + c
                elif block['type'] is 'n':
                    food = chars['food']
                    food.append(Food(self.screen, r + c, self.block_size))
                elif block['type'] is 'p':
                    power = chars['power']
                    power.append(Power(self.screen, r + c, self.block_size))
                c += 1
            r += c - 1
            c = 0

        return chars

    def render(self):
        x, y, b = 0, 0, self.block_size

        for row in self.rows:
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
