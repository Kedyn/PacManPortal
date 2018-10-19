import pygame

from pygame.sprite import Sprite


class Pacman(Sprite):
    def __init__(self, screen, position, block_size, maze):
        super().__init__()

        self.screen = screen

        self.cols = int(screen.get_rect().right / block_size)

        self.opened_right = pygame.image.load('assets/pacman_opened.png')
        self.opened_left = pygame.transform.flip(self.opened_right, True,
                                                 False)
        self.opened_up = pygame.transform.rotate(self.opened_left, 270)
        self.opened_down = pygame.transform.flip(self.opened_up, False, True)
        self.closed = pygame.image.load('assets/pacman_closed.png')

        self.image = self.closed

        self.rect = self.image.get_rect()

        self.block_size = block_size

        self.rect.x = int(position % self.cols) * block_size
        self.rect.y = int(position / self.cols) * block_size

        # 0 = no movement, 1 = left, 2 = up, 3 = right, 4 = down
        self.direction = 0
        self.next_direction = 0

        self.maze = maze

        self.portals = []

        self.portal_direction = 0

    def isBrick(self, direction):
        block = (0, 0, 100, 255)
        fence = (100, 100, 100, 255)
        dot = (0, 0, 0, 0)

        if direction is 1:
            dot = self.screen.get_at((self.rect.x - 1,
                                     int(self.rect.y + (self.block_size / 2))))
        elif direction is 2:
            dot = self.screen.get_at((int(self.rect.x + (self.block_size / 2)),
                                      self.rect.y - 1))
        elif direction is 3:
            dot = self.screen.get_at((self.rect.x + self.block_size,
                                     int(self.rect.y + (self.block_size / 2))))
        elif direction is 4:
            dot = self.screen.get_at((int(self.rect.x + (self.block_size / 2)),
                                      self.rect.y + self.block_size))

        if dot == block or dot == fence:
            return True

        return False

    def update(self):
        check = False

        if self.next_direction is 1 or self.next_direction is 3:
            if self.rect.y % self.block_size == 0:
                check = True

        if self.next_direction is 2 or self.next_direction is 4:
            if self.rect.x % self.block_size == 0:
                check = True

        if check:
            if not self.isBrick(self.next_direction):
                self.direction = self.next_direction
                self.next_direction = 0

        if self.isBrick(self.direction):
            self.direction = 0

        if self.direction is 1:
            self.rect.x -= 1
            if self.image is self.closed:
                self.image = self.opened_left
            else:
                self.image = self.closed
        elif self.direction is 2:
            self.rect.y -= 1
            if self.image is self.closed:
                self.image = self.opened_up
            else:
                self.image = self.closed
        elif self.direction is 3:
            self.rect.x += 1
            if self.image is self.closed:
                self.image = self.opened_right
            else:
                self.image = self.closed
        elif self.direction is 4:
            self.rect.y += 1
            if self.image is self.closed:
                self.image = self.opened_down
            else:
                self.image = self.closed
        else:
            self.image = self.closed

    def render(self):
        self.screen.blit(self.image, self.rect)
