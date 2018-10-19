import pygame

from pygame.sprite import Sprite


class Ghost(Sprite):
    def __init__(self, screen, position, block_size, ghost_type=1):
        super().__init__()

        self.screen = screen

        if ghost_type is 1:
            self.normal = pygame.image.load('assets/blinky_normal.png')
            self.step = pygame.image.load('assets/blinky_step.png')
        elif ghost_type is 2:
            self.normal = pygame.image.load('assets/pinky_normal.png')
            self.step = pygame.image.load('assets/pinky_step.png')
        elif ghost_type is 3:
            self.normal = pygame.image.load('assets/clyde_normal.png')
            self.step = pygame.image.load('assets/clyde_step.png')
        elif ghost_type is 4:
            self.normal = pygame.image.load('assets/inkey_normal.png')
            self.step = pygame.image.load('assets/inkey_step.png')

        self.left = pygame.image.load('assets/left_eyes.png')
        self.up = pygame.image.load('assets/up_eyes.png')
        self.right = pygame.image.load('assets/right_eyes.png')
        self.down = pygame.image.load('assets/down_eyes.png')

        self.image = self.normal
        self.eyes = self.up

        self.rect = self.image.get_rect()

        cols = int(screen.get_rect().right / block_size)

        self.rect.x = int(position % cols) * block_size
        self.rect.y = int(position / cols) * block_size

        self.block_size = block_size
        self.ghost_type = ghost_type

        self.direction = 2

    def render(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.eyes, self.rect)
