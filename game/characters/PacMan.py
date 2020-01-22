import pygame

from enum import Enum

from framework.AssetsManager import AssetsManager
from game.tools import Direction


class PacMan(pygame.sprite.Sprite):
    # Public

    def __init__(self, block_size):
        super().__init__()

        self.__assets_manager = AssetsManager.get_instance()

        self.__state = "opened"

        self.__direction = Direction.FRONT
        self.__last_direction = Direction.RIGHT

        self.__speed = 1

        self.__block_size = block_size

        self.image = None

        self.__set_image()

        self.rect = self.image.get_rect()

        self.radius = self.rect.width / 2

        self.__state_timer = pygame.time.get_ticks()

    def set_direction(self, direction):
        if direction != self.__direction and not self.__is_blocked(direction):
            if direction == Direction.FRONT:
                self.__last_direction = self.__direction

                self.__state = "opened"
            else:
                self.__last_direction = None

            self.__direction = direction

    def set_next_direction(self, direction):
        self.__next_direction = direction

    def set_speed(self, speed):
        self.__speed = speed

    def set_grid(self, grid):
        self.__grid = grid

    def coo_to_item(self, x, y):
        return (int(y / self.__block_size),
                int(x / self.__block_size))

    def get_position(self):
        return self.coo_to_item(self.rect.x, self.rect.y)

    def update(self):
        check = False

        if self.__next_direction == Direction.LEFT or self.__next_direction == Direction.RIGHT:
            if self.rect.y % self.__block_size == 0:
                check = True

        if self.__next_direction == Direction.UP or self.__next_direction == Direction.DOWN:
            if self.rect.x % self.__block_size == 0:
                check = True

        if check:
            if not self.__is_blocked(self.__next_direction):
                self.set_direction(self.__next_direction)

                self.__next_direction = None

        current_timer = pygame.time.get_ticks()

        if current_timer - self.__state_timer >= 150 and self.__direction != Direction.FRONT:
            if self.__state == "opened":
                self.__state = "closed"
            else:
                self.__state = "opened"

            self.__state_timer = current_timer

        self.__set_image()

        if self.__is_blocked(self.__direction):
            self.set_direction(Direction.FRONT)

        if self.__direction == Direction.LEFT:
            self.rect.x -= self.__speed
        elif self.__direction == Direction.UP:
            self.rect.y -= self.__speed
        elif self.__direction == Direction.RIGHT:
            self.rect.x += self.__speed
        elif self.__direction == Direction.DOWN:
            self.rect.y += self.__speed

    # Private

    __assets_manager = None

    __block_size = None

    __state = None
    __state_timer = None

    __last_direction = None
    __direction = None
    __next_direction = None
    __speed = None

    __grid = None

    def __set_image(self):
        if self.__state == "opened":
            self.image = self.__assets_manager.get_asset("image", "pacman_opened")
        else:
            self.image = self.__assets_manager.get_asset("image", "pacman_closed")

        self.__rotate_image(self.__direction)

        if self.__last_direction is not None:
            self.__rotate_image(self.__last_direction)

        self.image = pygame.transform.scale(self.image, (self.__block_size, self.__block_size))

    def __is_blocked(self, direction):
        if direction != Direction.FRONT:
            item = None

            if direction == Direction.LEFT:
                item = self.coo_to_item(self.rect.left - 1, self.rect.y)
            elif direction == Direction.UP:
                item = self.coo_to_item(self.rect.x, self.rect.top - 1)
            elif direction == Direction.RIGHT:
                item = self.coo_to_item(self.rect.right + 1, self.rect.y)
            elif direction == Direction.DOWN:
                item = self.coo_to_item(self.rect.x, self.rect.bottom + 1)

            if self.__grid[item[0]][item[1]] > 0:
                return True

        return False

    def __rotate_image(self, direction):
        if direction == Direction.LEFT:
            self.image = pygame.transform.rotate(self.image, 180)
        elif direction == Direction.UP:
            self.image = pygame.transform.rotate(self.image, 90)
        elif direction == Direction.DOWN:
            self.image = pygame.transform.rotate(self.image, 270)
