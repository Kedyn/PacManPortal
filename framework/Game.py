import pygame

from framework.SceneManager import SceneManager


class Game:
    # Public:

    @staticmethod
    def get_instance():
        if Game.__instance is None:
            Game()

        return Game.__instance

    def get_surface(self):
        return self.__surface

    def log(self, message):
        if self.__debug_mode is True:
            print(message)

    def create(self, resolution, title, frame_rate=60, debug_mode=False):
        self.__resolution = resolution
        self.__title = title
        self.__frame_rate = frame_rate
        self.__debug_mode = debug_mode

        self.__surface = pygame.display.set_mode(self.__resolution)

        pygame.display.set_caption(self.__title)

        self.__clock = pygame.time.Clock()
        self.__running = True

        self.__scene_manager = SceneManager.get_instance()

    def start(self):
        self.__loop()

    # Private:

    __instance = None
    __surface = None

    __resolution = None
    __title = None
    __frame_rate = None
    __debug_mode = None

    __clock = None
    __running = None

    __scene_manager = None

    def __init__(self):
        if Game.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Game.__instance = self

            pygame.init()

            pygame.font.init()

    def __loop(self):
        while self.__running:
            self.__clock.tick(self.__frame_rate)
            self.__events()
            self.__update()
            self.__draw()

    def __events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            elif event.type == pygame.KEYDOWN:
                self.__scene_manager.on_key_down(event.key)
            elif event.type == pygame.KEYUP:
                self.__scene_manager.on_key_up(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__scene_manager.on_mouse_button_down(event.button, event.pos)

    def __update(self):
        self.__scene_manager.update()

    def __draw(self):
        self.__scene_manager.draw()

        pygame.display.flip()
