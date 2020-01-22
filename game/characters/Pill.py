import pygame

from game.constants import *


import pygame


class Pill(pygame.sprite.Sprite):
    # Public

    def __init__(self, super_pill=False):
        super().__init__()

        self.__super_pill = super_pill

        size = PILL_SIZE
        color = PILL_COLOR

        if super_pill:
            size = SUPER_PILL_SIZE
            color = SUPER_PILL_COLOR

        radius = int(size / 2)

        self.image = pygame.Surface((size, size))

        self.rect = self.image.get_rect()

        self.radius = radius

        pygame.draw.circle(self.image, color, (radius, radius), self.radius)

    def is_super_pill(self):
        return self.__super_pill

    # Private

    __super_pill = None
