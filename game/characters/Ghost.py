import pygame

from enum import Enum

from framework.AssetsManager import AssetsManager
from game.tools import Direction


class GhostType(Enum):
    BLINKY = 1
    PINKY = 2
    INKY = 3
    CLYDE = 4
    BLUE = 5
    WHITE = 6


class Ghost(pygame.sprite.Sprite):
    # Public

    def __init__(self, ghost_type, block_size):
        super().__init__()

        self.__assets_manager = AssetsManager.get_instance()

        self.__original_type = ghost_type
        self.__ghost_type = ghost_type
        self.__state = "normal"

        self.__direction = Direction.FRONT

        self.__speed = 1

        self.__block_size = block_size

        self.image = None

        self.__set_image()

        self.rect = self.image.get_rect()

        self.__state_timer = pygame.time.get_ticks()
        self.__path = []

    def set_direction(self, direction):
        self.__direction = direction

    def get_direction(self):
        return self.__direction

    def set_speed(self, speed):
        self.__speed = speed

    def get_position(self):
        return (int(self.rect.y / self.__block_size),
                int(self.rect.x / self.__block_size))

    def set_path(self, path):
        self.__path = path

        if len(path) > 0:
            self.__path.pop(0)

    def update(self):
        current_timer = pygame.time.get_ticks()

        if current_timer - self.__state_timer >= 150 and self.__direction != Direction.FRONT:
            if self.__state == "normal":
                self.__state = "step"
            else:
                self.__state = "normal"

            self.__state_timer = current_timer

        if self.__direction != Direction.FRONT:
            if len(self.__path) > 0:
                position = self.get_position()
                next_position = self.__path[0].position

                if next_position[1] < position[1] and next_position[0] == position[0] and\
                        self.rect.y % self.__block_size == 0:
                    self.__direction = Direction.LEFT

                    self.__path.pop(0)
                elif next_position[0] < position[0] and next_position[1] == position[1] and\
                        self.rect.x % self.__block_size == 0:
                    self.__direction = Direction.UP

                    self.__path.pop(0)
                elif next_position[1] > position[1] and next_position[0] == position[0] and\
                        self.rect.y % self.__block_size == 0:
                    self.__direction = Direction.RIGHT

                    self.__path.pop(0)
                elif next_position[0] > position[0] and next_position[1] == next_position[1] and\
                        self.rect.x % self.__block_size == 0:
                    self.__direction = Direction.DOWN

                    self.__path.pop(0)
            else:
                self.__direction = Direction.FRONT

        if self.__direction == Direction.LEFT:
            self.rect.x -= self.__speed
        elif self.__direction == Direction.UP:
            self.rect.y -= self.__speed
        elif self.__direction == Direction.RIGHT:
            self.rect.x += self.__speed
        elif self.__direction == Direction.DOWN:
            self.rect.y += self.__speed

        self.__set_image()

    # Private

    __assets_manager = None

    __original_type = None
    __ghost_type = None

    __block_size = None

    __state = None
    __state_timer = None

    __direction = None
    __speed = None

    __path = None

    def __set_image(self):
        if self.__ghost_type == GhostType.BLINKY:
            if self.__state == "normal":
                self.image = self.__assets_manager.get_asset("image", "blinky_normal")
            else:
                self.image = self.__assets_manager.get_asset("image", "blinky_step")
        elif self.__ghost_type == GhostType.PINKY:
            if self.__state == "normal":
                self.image = self.__assets_manager.get_asset("image", "pinky_normal")
            else:
                self.image = self.__assets_manager.get_asset("image", "pinky_step")
        elif self.__ghost_type == GhostType.CLYDE:
            if self.__state == "normal":
                self.image = self.__assets_manager.get_asset("image", "clyde_normal")
            else:
                self.image = self.__assets_manager.get_asset("image", "clyde_step")
        elif self.__ghost_type == GhostType.INKY:
            if self.__state == "normal":
                self.image = self.__assets_manager.get_asset("image", "inky_normal")
            else:
                self.image = self.__assets_manager.get_asset("image", "inky_step")
        elif self.__ghost_type == GhostType.BLUE:
            if self.__state == "normal":
                self.image = self.__assets_manager.get_asset("image", "blue_normal")
            else:
                self.image = self.__assets_manager.get_asset("image", "blue_step")
        elif self.__ghost_type == GhostType.WHITE:
            if self.__state == "normal":
                self.image = self.__assets_manager.get_asset("image", "white_normal")
            else:
                self.image = self.__assets_manager.get_asset("image", "white_step")

        self.image = pygame.transform.scale(self.image, (self.__block_size, self.__block_size))

        eyes = None

        if self.__direction == Direction.LEFT:
            eyes = self.__assets_manager.get_asset("image", "left_eyes")
        elif self.__direction == Direction.UP:
            eyes = self.__assets_manager.get_asset("image", "up_eyes")
        elif self.__direction == Direction.RIGHT:
            eyes = self.__assets_manager.get_asset("image", "right_eyes")
        elif self.__direction == Direction.DOWN:
            eyes = self.__assets_manager.get_asset("image", "down_eyes")
        elif self.__direction == Direction.FRONT:
            eyes = self.__assets_manager.get_asset("image", "front_eyes")

        eyes = pygame.transform.scale(eyes, (self.__block_size, self.__block_size))

        self.image.blit(eyes, eyes.get_rect())
