import pygame

from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, screen, item, block_size):
        super().__init__()

        self.screen = screen

        x = item['j'] * block_size
        y = item['i'] * block_size

        self.rect = pygame.Rect(0, 0, int(block_size / 4), int(block_size / 4))

        self.rect.center = (int(x + (block_size / 2)),
                            int(y + (block_size / 2)))

    def render(self):
        pygame.draw.circle(self.screen, (100, 100, 0),
                           self.rect.center,
                           int(self.rect.width / 2))
