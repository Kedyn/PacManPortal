import pygame


class AssetsManager:
    # Public:

    @staticmethod
    def get_instance():
        if AssetsManager.__instance is None:
            AssetsManager()

        return AssetsManager.__instance

    def add_asset(self, asset_type, name, file):
        if asset_type == "image" and name not in self.__images:
            self.__images[name] = pygame.image.load(file)

    def del_asset(self, asset_type, name):
        if asset_type == "image" and name in self.__images:
            self.__images.pop(name)

    def get_asset(self, asset_type, name):
        if asset_type == "image" and name in self.__images:
            return self.__images[name]

        return None

    # Private:

    __instance = None

    __game = None

    __images = None

    def __init__(self):
        if AssetsManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AssetsManager.__instance = self

            self.__images = {}
