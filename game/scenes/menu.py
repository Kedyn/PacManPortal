import pygame

from framework.Scene import Scene
from framework.SceneManager import SceneManager
from framework.Text import Text
from game.characters.Ghost import Ghost, GhostType
from game.constants import *
from game.tools import Direction


class MenuScene(Scene):
    # Public

    def __init__(self, surface, background=(0, 0, 0)):
        super().__init__(surface)

        self.__surface = surface
        self.__game_objects = pygame.sprite.Group()

        self.__background = background

        title = Text(300, REGULAR_TEXT_COLOR, "PACMAN")

        title.rect.centerx = WIDTH / 2
        title.rect.top = 20

        header = Text(200, SPECIAL_TEXT_COLOR, "PORTAL")

        header.rect.centerx = WIDTH / 2
        header.rect.top = 200

        self.__play = Text(80, REGULAR_TEXT_COLOR, "PLAY")

        self.__play.rect.centerx = WIDTH / 2
        self.__play.rect.top = HEIGHT - 240

        self.__high_scores = Text(80, REGULAR_TEXT_COLOR, "HIGH SCORES")

        self.__high_scores.rect.centerx = WIDTH / 2
        self.__high_scores.rect.top = HEIGHT - 120

        self.__blinky = Ghost(GhostType.BLINKY, MENU_CHARACTER_SIZE)
        self.__pinky = Ghost(GhostType.PINKY, MENU_CHARACTER_SIZE)
        self.__inky = Ghost(GhostType.INKY, MENU_CHARACTER_SIZE)
        self.__clyde = Ghost(GhostType.CLYDE, MENU_CHARACTER_SIZE)

        self.__blinky.rect.centery = HEIGHT / 2
        self.__pinky.rect.centery = HEIGHT / 2
        self.__inky.rect.centery = HEIGHT / 2
        self.__clyde.rect.centery = HEIGHT / 2

        self.__game_objects.add(title)
        self.__game_objects.add(header)
        self.__game_objects.add(self.__play)
        self.__game_objects.add(self.__high_scores)
        self.__game_objects.add(self.__blinky)
        self.__game_objects.add(self.__pinky)
        self.__game_objects.add(self.__inky)
        self.__game_objects.add(self.__clyde)

        self.__scene_manager = SceneManager.get_instance()

        self.__animation = 1

        self.__blinky.set_speed(MENU_CHARACTER_SPEED)
        self.__pinky.set_speed(MENU_CHARACTER_SPEED)
        self.__inky.set_speed(MENU_CHARACTER_SPEED)
        self.__clyde.set_speed(MENU_CHARACTER_SPEED)

        self.reset()

    def reset(self):
        self.__blinky.rect.right = 0
        self.__pinky.rect.right = -240
        self.__inky.rect.right = -480
        self.__clyde.rect.right = -720

        self.__blinky.set_direction(Direction.RIGHT)
        self.__pinky.set_direction(Direction.RIGHT)
        self.__inky.set_direction(Direction.RIGHT)
        self.__clyde.set_direction(Direction.RIGHT)

        self.__animation = 1

    def on_mouse_button_down(self, button, position):
        if self.__play.rect.collidepoint(position):
            self.__scene_manager.set_scene("game")
        elif self.__high_scores.rect.collidepoint(position):
            self.__scene_manager.set_scene("high_scores")

    def update(self):
        position = pygame.mouse.get_pos()

        if self.__play.rect.collidepoint(position):
            self.__play.set_color(SPECIAL_TEXT_COLOR)
        else:
            self.__play.set_color(REGULAR_TEXT_COLOR)

            if self.__high_scores.rect.collidepoint(position):
                self.__high_scores.set_color(SPECIAL_TEXT_COLOR)
            else:
                self.__high_scores.set_color(REGULAR_TEXT_COLOR)

        self.__game_objects.update()

        if self.__animation == 1:
            if self.__clyde.rect.left >= WIDTH + 10:
                self.__animation += 1

                self.__blinky.set_direction(Direction.LEFT)
                self.__pinky.set_direction(Direction.LEFT)
                self.__inky.set_direction(Direction.LEFT)
                self.__clyde.set_direction(Direction.LEFT)

    def draw(self):
        self.__surface.fill(self.__background)

        self.__game_objects.draw(self.__surface)

    def on_exit(self):
        return True

    # Private

    __surface = None
    __game_objects = None

    __scene_manager = None

    __background = None
    __animation = None

    __blinky = None
    __pinky = None
    __inky = None
    __clyde = None

    __play = None
    __high_scores = None
