import pygame

from pygame.sprite import Sprite


class Power(Sprite):
    def __init__(self, screen, position, block_size):
        super().__init__()

        self.screen = screen

        self.block_size = block_size

        cols = int(screen.get_rect().right / block_size)

        x = int(position % cols) * block_size
        y = int(position / cols) * block_size

        self.rect = pygame.Rect(0, 0, int(block_size / 2), int(block_size / 2))

        self.rect.center = (int(x + (block_size / 2)),
                            int(y + (block_size / 2)))

    def render(self):
        pygame.draw.circle(self.screen, (180, 180, 0),
                           self.rect.center,
                           int(self.rect.width / 2))
