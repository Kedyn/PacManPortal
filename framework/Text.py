import pygame


class Text(pygame.sprite.Sprite):
    # Public

    def __init__(self, size, color, text):
        super().__init__()

        self.__size = size
        self.__color = color
        self.__text = text

        self.__font = pygame.font.SysFont(None, size)

        self.__prep_image()

    def set_color(self, color):
        self.__color = color

        center = self.rect.center

        self.__prep_image()

        self.rect.center = center

    # Private

    __size = None
    __color = None
    __text = None
    __font = None

    def __prep_image(self):
        text_image = self.__font.render(self.__text, True, self.__color)

        self.image = text_image

        self.rect = self.image.get_rect()
