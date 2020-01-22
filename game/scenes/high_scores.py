import pygame

from framework.Scene import Scene
from framework.SceneManager import SceneManager
from framework.Text import Text
from game.constants import *


class HighScoresScene(Scene):
    # Public

    def __init__(self, surface, background=(0, 0, 0)):
        super().__init__(surface)

        self.__surface = surface
        self.__game_objects = pygame.sprite.Group()

        self.__background = background

        self.__scene_manager = SceneManager.get_instance()

        self.__menu = Text(80, REGULAR_TEXT_COLOR, "MENU")

        self.__menu.rect.centerx = WIDTH / 2
        self.__menu.rect.top = HEIGHT - 120

    def reset(self):
        self.__game_objects.empty()

        title = Text(200, REGULAR_TEXT_COLOR, "PACMAN")

        title.rect.centerx = WIDTH / 2
        title.rect.top = 20

        header = Text(150, SPECIAL_TEXT_COLOR, "PORTAL")

        header.rect.centerx = WIDTH / 2
        header.rect.top = 140

        self.__game_objects.add(title)
        self.__game_objects.add(header)

        high_scores = open('assets/high_scores.txt',
                           'r').read().split('\n')

        y = 300

        for score in high_scores:
            if score:
                score_text = Text(50, SPECIAL_TEXT_COLOR, score)

                score_text.rect.centerx = WIDTH / 2
                score_text.rect.top = y

                self.__game_objects.add(score_text)

                y += 50

        self.__game_objects.add(self.__menu)

    def on_mouse_button_down(self, button, position):
        if self.__menu.rect.collidepoint(position):
            self.__scene_manager.set_scene("menu")

    def update(self):
        if self.__menu.rect.collidepoint(pygame.mouse.get_pos()):
            self.__menu.set_color(SPECIAL_TEXT_COLOR)
        else:
            self.__menu.set_color(REGULAR_TEXT_COLOR)

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

    __menu = None
