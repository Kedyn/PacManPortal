import pygame

from game.constants import *


class Wall(pygame.sprite.Sprite):
    # Public

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((WIDTH, HEIGHT))

        self.rect = self.image.get_rect()

    def add_block(self, x, y, block_type="normal"):
        color = BLOCK_COLOR

        if block_type == "fence":
            color = FENCE_COLOR

        pygame.draw.rect(self.image, color, pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
