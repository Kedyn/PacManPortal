import pygame

from pygame.sprite import Sprite


class Ghost(Sprite):
    def __init__(self, screen, position, block_size, ghost_type=1):
        super().__init__()

        self.screen = screen

        cols = int(screen.get_rect().right / block_size)

        self.x = int(position / cols) * block_size
        self.y = int(position % cols) * block_size

        self.block_size = block_size
        self.ghost_type = ghost_type

    def render(self):
        x, y, b = self.x, self.y, self.block_size
        if self.ghost_type is 1:
            self.screen.fill((180, 0, 0), pygame.Rect(x + 2, y + 2, b - 4, b - 4))
        elif self.ghost_type is 2:
            self.screen.fill((255, 140, 0), pygame.Rect(x + 2, y + 2, b - 4, b - 4))
        elif self.ghost_type is 3:
            self.screen.fill((255, 100, 0), pygame.Rect(x + 2, y + 2, b - 4, b - 4))
        elif self.ghost_type is 4:
            self.screen.fill((0, 180, 180), pygame.Rect(x + 2, y + 2, b - 4, b - 4))
