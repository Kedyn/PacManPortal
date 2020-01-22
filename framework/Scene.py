import pygame


class Scene:
    # Public:

    def __init__(self, surface):
        self.__surface = surface
        self.__game_objects = pygame.sprite.Group()

    def on_key_down(self, key):
        pass

    def on_key_up(self, key):
        pass

    def on_mouse_button_down(self, button, position):
        pass

    def reset(self):
        pass

    def update(self):
        self.__game_objects.update()

    def draw(self):
        if len(self.__game_objects) > 0:
            self.__game_objects.draw(self.__surface)

    def on_exit(self):
        pass

    # Private
    __surface = None
    __game_objects = None
