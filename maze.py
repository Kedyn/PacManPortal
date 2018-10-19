import pygame


class Maze:
    def __init__(self, file, screen):
        self.screen = screen

        with open(file, 'r') as f:
            self.rows = f.readlines()

        self.block_size = 30

    def get_characters(self):
        r, c, b, chars = 1, 1, self.block_size, {}

        chars.update({'fence': []})

        for row in self.rows:
            for block in row:
                if block is 'f':
                    fence = chars['fence']
                    fence.append(r * c)
                elif block is 'c':
                    chars['pacman'] = r * c
                elif block is '1':
                    chars['blinky'] = r * c
                elif block is '2':
                    chars['inkey'] = r * c
                elif block is '3':
                    chars['pinky'] = r * c
                elif block is '4':
                    chars['clyde'] = r * c
                c += 1
            c = 1
            r += 1

        return chars

    def render(self):
        x, y, b = 0, 0, self.block_size

        for row in self.rows:
            for block in row:
                if block is 'x':
                    self.screen.fill((0, 0, 100), pygame.Rect(x, y, b, b))
                elif block is 'n':
                    pygame.draw.circle(self.screen, (100, 100, 0), (int(x + (b / 2)), int(y + (b / 2))), int(b / 8))
                elif block is 'p':
                    pygame.draw.circle(self.screen, (180, 180, 0), (int(x + (b / 2)), int(y + (b / 2))), int(b / 4))
                elif block is 'f':
                    self.screen.fill((100, 100, 100), pygame.Rect(x, y + (b / 4), b, b / 2))
                elif block is 'c':
                    pygame.draw.circle(self.screen, (255, 255, 0), (int(x + (b / 2)), int(y + (b / 2))), int(b / 2))
                x += b
            x = 0
            y += b
